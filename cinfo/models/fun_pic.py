#!/usr/bin/env python
# coding: utf-8

from ..extensions import db
from serialize import AutoSerialize

class FunPic(db.Model, AutoSerialize):
    __tablename__ = 'fun_pic'

    id = db.Column(db.Integer, primary_key=True)
    oo = db.Column(db.Integer)
    xx = db.Column(db.Integer)
    pic_urls = db.Column(db.String(1024))
    pic_type = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<FunPic %r>' % self.id