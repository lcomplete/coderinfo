#!/usr/bin/env python
# coding: utf-8

from ..extensions import db
from serialize import AutoSerialize

class CaptureArticle(db.Model, AutoSerialize):
    __tablename__ = 'capture_article'

    id = db.Column(db.Integer, primary_key = True)
    short_title = db.Column(db.String(128))
    summary = db.Column(db.Text)
    brief = db.Column(db.Text)
    raw_url = db.Column(db.String(256))
    site_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    isshow = db.Column(db.Integer)
    site_name = db.Column(db.String(45))

    def __repr__(self):
        return '<CaptureArticle %r>' % self.short_title