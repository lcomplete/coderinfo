#coding=utf-8

import urllib2,re
from lxml import etree
from urlparse import urlparse,urljoin
from HTMLParser import HTMLParser

def get_page_resp(url):
    req=urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36')
    result = urllib2.urlopen(req).read()
    return result


def get_article_links(html,url,limit):
    doc= etree.HTML(html)
    a_elements= doc.xpath('//a')
    links=[]
    for a in a_elements:
        text = get_innertext(a)
        if isarticle_link(a,text):
            href=a.attrib.get("href",'')
            links.append({
                "url": href if href.find('http')==0 else urljoin(url,href),
                "text": text
            })
            if 0 < limit <= len(links):
                break
    return links


def get_innertext(a):
    text= a.xpath('string()')
    return text


def isarticle_link(a,text):
    href=a.attrib.get("href",'')
    if text==None or href==None:
        return False
    charlen= width_len(text)
    if charlen<10 or href.find('#')==0 or href.find('javascript:')==0:
        return False
    path = urlparse(href).path
    if path=='' or path=="/":
        return False

    base = 0.5
    if path.find('?')>0:
        base += 0.1 if re.match(r'\?.*id.*',path,re.I) else -0.1
    elif re.match(r'^/[^/]+/?$',path):
        base-=0.3
    if a.attrib.get('title','') !='':
        base+=0.2
    if(text.endswith('...')):
        base+=0.4
    if re.match(r'/[^/]*-[^/]*/?$',path):
        base+=0.1
    if re.match(r'\d{4,}',path):
        base+=0.1
    if re.match(r'^[a-z]+$',text,re.I):
        base-=0.4
    positive_chars = ['”.*“','（.*）','(.*)','#.*#','[.*]','【.*】','：',':','——','，',',',r'\?',
                      '？','《.*》','！','!',r'\d+\.html?']
    for pos_char in positive_chars:
        if re.match(pos_char,text,re.I):
            base+=0.2
    positive_links = ['article','detail','/p/']
    for pos_link in positive_links:
        if re.match(pos_link,path,re.I):
            base+=0.2
    base += charlen-10 / 26.
    return base>=1


def width_len(str):
    '''计算字符串长度 两个ascii字符算一个字符'''
    length = len(str)
    utf8_length = len(str.encode('utf-8'))
    length = (utf8_length - length)/2 + length
    return length / 2

def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    >>> str_text=strip_tags("<font color=red>hello</font>")
    >>> print str_text
    hello
    """
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    html= ''.join(result)
    html= re.sub(r'\s+',' ',html)
    html=re.sub(r'\n+','\n',html)
    return html

def extract_brief(text,min_length,max_length):
    paragraphs = text.split('\n')
    result= []
    length = 0
    for pa in paragraphs:
        cur_len=len(pa)
        to_len=cur_len+length
        if to_len<min_length:
            result.append(pa)
        elif to_len>max_length:
            result.append(pa[0:max_length-length])
        else:
            result.append(pa)
            break
        length=to_len
    return '\n'.join(result)