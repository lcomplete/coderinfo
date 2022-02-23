#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint, request, g, current_app, url_for, jsonify
from flask import render_template, Response
from ..models import CaptureArticle, CaptureSite

bp = Blueprint('home', __name__)


@bp.route('/', defaults={'siteid': 0, 'page': 1})
@bp.route('/p-<int:page>', defaults={'siteid': 0})
@bp.route('/site-<int:siteid>/', defaults={'page': 1})
@bp.route('/site-<int:siteid>/p-<int:page>')
def index(siteid=0, page=1):
    if page < 1: page = 1

    sites = CaptureSite.query.filter_by(isenabled=1, isdeleted=0).order_by(CaptureSite.sequence).all()

    q_article = CaptureArticle.query.with_entities(CaptureArticle.id, CaptureArticle.site_name,
                                                   CaptureArticle.brief, CaptureArticle.create_date,
                                                   CaptureArticle.short_title,
                                                   CaptureArticle.raw_url,
                                                   CaptureArticle.site_id). \
        filter_by(isshow=1).filter(CaptureArticle.summary != "").order_by(CaptureArticle.create_date.desc())

    if siteid != 0:
        q_article = q_article.filter_by(site_id=siteid)
    page_articles = q_article.paginate(page, 20, False)

    page_url = lambda page: url_for("home.index",
                                    siteid=siteid,
                                    page=page)
    return render_template('index.html', sites=sites, page_articles=page_articles, page_url=page_url, cur_siteid=siteid)


@bp.route('/article/<int:id>')
def article(id):
    article = CaptureArticle.query.filter_by(id=id, isshow=1).first()
    return jsonify(article.get_public())
