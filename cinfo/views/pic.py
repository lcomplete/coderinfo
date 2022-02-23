#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint, request, url_for, abort
from flask import render_template, Response
from sqlalchemy import text

from ..models import *

bp = Blueprint('pic', __name__)


@bp.route('/<type>', defaults={'page': 1})
@bp.route('/<type>/<int:page>')
def index(type, page=1):
    pictype = __conv_type(type)
    if not pictype:
        abort(404)

    # page_pics = FunPic.query.filter_by(pic_type=pictype).order_by(FunPic.id.desc()).paginate(page, 5, False)
    # page_url = lambda x: url_for('pic.index', type=type, page=x)

    return render_template('pic.html', cur_type=type)


def __conv_type(type):
    pictype= None
    if type == 'o_o':
        pictype = 'jandan_pic'
    elif type == 'x_x':
        pictype = 'jandan_ooxx'
    return pictype


@bp.route('/partial')
@bp.route('/partial/<type>')
def partial(type=None):
    pictype = __conv_type(type)
    query = FunPic.query
    if pictype:
        query = query.filter_by(pic_type=pictype)
    pics = query.order_by(text('rand()')).limit(8).all()

    return render_template("pic_partial.html", pics=pics)