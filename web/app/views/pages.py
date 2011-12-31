# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request,redirect

bp = Blueprint('pages', __name__)

#------------------------------------------------------------------------------
@bp.route('/<page>', defaults={'page': 'page'})
def show(page):
    if 'www.' in request.url: return redirect(request.url.replace('www.', ''))

    context = {}
    context['page'] = page

    return render_template('{0}.html'.format(page), c=context)
