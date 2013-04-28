# -*- coding: utf-8 -*-

import datetime
from flask.ext.wtf import Form, Required, Optional, BooleanField, \
    IntegerField, TextField, TextAreaField
from app.views.backpack.utils import slugify

class BaseForm(Form):
    author = TextField(validators=[Required()])
    in_menu = BooleanField(validators=[Optional()])
    visibility = BooleanField()
    order = IntegerField(default=0)
    created = TextField(default=datetime.datetime.now)
    modified = TextField(default=datetime.datetime.now)


class PageForm(BaseForm):
    title = TextField(validators=[Required()])
    slug = TextField()
    teaser = TextAreaField()
    text = TextAreaField(validators=[Required()])

    exclude = ['csrf_token', 'created', 'author']
    editor = ['teaser', 'text']

    def validate_slug(form, field):
        if field.data:
            field.data = slugify(field.data)
        else:
            field.data = slugify(form.data['title'])