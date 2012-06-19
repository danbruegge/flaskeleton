# -*- coding: utf-8 -*-

import datetime
from flaskext.wtf import Form, Required, BooleanField, IntegerField, \
    TextField, TextAreaField, DateTimeField, FormField, ListWidget

class BaseForm(Form):
    author = TextField('Autor', validators=[Required()])
    in_menu = BooleanField(u'in Menü')
    visibility = BooleanField('Sichtbarkeit')
    order = IntegerField('Sortierung', default=0)
    created = DateTimeField(default=datetime.datetime.now)
    modified = DateTimeField(u'Zuletzt geändert', default=datetime.datetime.now)


class PageForm(BaseForm):
    title = TextField('Titel', validators=[Required()])
    slug = TextField(validators=[Required()])
    teaser = TextAreaField()
    text = TextAreaField(validators=[Required()])

    exclude = ['csrf_token', 'created', 'author']
    editor = ['teaser', 'text']
