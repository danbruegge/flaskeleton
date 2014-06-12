# -*- coding: utf-8 -*-


def load_context_processors(app):
    """Load all base context_processors.
    """

    @app.context_processor
    def utility_processor():
        def get_slug(path, pos=0):
            try:
                slug = path.split('/')[pos + 1]
            except IndexError:
                slug = ''

            return slug

        return dict(get_slug=get_slug)
