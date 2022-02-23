#!/usr/bin/env python
# coding: utf-8

from ..extensions import db

class CaptureSite(db.Model):
    __tablename__ = 'capture_site'

    id = db.Column(db.Integer, primary_key= True)
    site_url =db.Column(db.String(128))
    site_name =db.Column(db.String(45))
    article_limit =db.Column(db.Integer)
    interval_minute= db.Column(db.Integer)
    isenabled = db.Column(db.Integer)
    isdeleted = db.Column(db.Integer)
    capture_class = db.Column(db.String(45))
    capture_date = db.Column(db.DateTime)
    failed_date = db.Column(db.DateTime)
    sequence = db.Column(db.Integer)

    def __repr__(self):
        return '<CaptureSite %r>' % self.site_name