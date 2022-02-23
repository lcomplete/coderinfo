#coding=utf-8

from capture.dbhelper import get_db
from readability import Document
from capture.htmlhelper import get_page_resp, get_article_links, strip_tags, extract_brief
from datetime import datetime, timedelta
import logging, traceback
from newspaper import Config,Article


class SiteCapture(object):
    def __init__(self, config):
        self.config = config
        self.url = config['site_url']
        self.site_id = config['id']
        self.limit = config['article_limit']
        self.site_name = config['site_name']

    def crawl(self):
        links = self.get_article_links()
        links.reverse()
        for link in links:
            article = self.capture_article(link['url'], link['text'])
            if article:
                self.__save_article(article)

    def get_article_links(self):
        html = get_page_resp(self.url)
        links = get_article_links(html, self.url, self.limit)
        return links

    def capture_article(self, link_url, link_text):
        try:
            article = self.get_exist_article(link_url)
            if not article:
                article = {
                    "raw_url": link_url,
                    "site_id": self.site_id,
                    "create_date": datetime.now(),
                    "isshow": True,
                    "site_name": self.site_name
                }
            elif article.update_date + timedelta(days=1) > datetime.now():
                return

            article["update_date"] = datetime.now()
            html = get_page_resp(link_url)

            # readability
            # article["summary"] = Document(html, url=link_url).summary(html_partial=True)
            # plain_text = strip_tags(article["summary"])
            # title = Document(html).short_title()
            # if not title or title == '':
            #     title = link_text
            # article["short_title"] = title

            #newspaper
            config = Config()
            config.keep_article_html = True
            news= Article(link_url, config=config, memoize_articles=False, language='zh')
            news.download(html)
            news.parse()
            article["short_title"] = news.title
            article["summary"] = news.article_html
            plain_text = strip_tags(news.meta_description)

            if len(plain_text) >= 200:
                article["brief"] = extract_brief(plain_text, 150, 200)
            else:
                article["brief"] = plain_text
            return article
        except:
            logging.error(u"抓取 %s 失败, traceback: %s", link_url, traceback.print_exc())

    def get_exist_article(self, link_url):
        with get_db() as db:
            article = db.get('select * from capture_article where raw_url= %s and site_id= %s', link_url, self.site_id)
            return article

    def __save_article(self, article):
        with get_db() as db:
            if article.has_key("id"):
                db.execute('''update capture_article set short_title= %s, summary= %s, update_date = %s,
                        brief= %s, isshow= %s where id= %s ''',
                           article["short_title"], article["summary"], article["update_date"], article["brief"],
                           article["id"]
                )
            else:
                db.execute('''insert into capture_article
                (short_title,summary,raw_url,site_id,create_date,update_date,isshow,brief,site_name)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                           article["short_title"], article["summary"], article["raw_url"], article["site_id"],
                           article["create_date"], article["update_date"], article["isshow"], article["brief"],
                           article["site_name"]
                )


