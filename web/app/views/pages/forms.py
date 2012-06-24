# -*- coding: utf-8 -*-

import datetime
from flaskext.wtf import Form, Required, Optional, BooleanField, \
    IntegerField, TextField, TextAreaField

class BaseForm(Form):
    author = TextField(validators=[Required()])
    in_menu = BooleanField(validators=[Optional()])
    visibility = BooleanField()
    order = IntegerField(default=0)
    created = TextField(default=datetime.datetime.now)
    modified = TextField(default=datetime.datetime.now)


class PageForm(BaseForm):
    title = TextField(validators=[Required()])
    slug = TextField(validators=[Required()])
    teaser = TextAreaField()
    text = TextAreaField(validators=[Required()])

    exclude = ['csrf_token', 'created', 'author']
    editor = ['teaser', 'text']
