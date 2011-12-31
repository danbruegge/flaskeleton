# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g

bp = Blueprint('install', __name__)

#------------------------------------------------------------------------------
@bp.route('/install')
def install():
    context = {}

    return render_template('install.html', c=context)
