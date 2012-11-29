BACKPACK
========

Backpack is an utility collection and a admin area embedded in a
flask-blueprint.

Backpack provides:
* standard css for a admin backend (for example, form styles)
* templates to wrap around a normal blueprint template (for example, base
  template)


Current TODO
------------
* update styles with lesscss
* add responsive
* add richt text editor - http://www.wymeditor.org/


Ideas
-----
* write method/function?! that read the a special dict in a mongodb collection
  what represent the structure of the form elements.

  example collection of a news entry:

        {
            '_id': ObectId(...),
            'title': '...',
            'date': '...',
            'text': '...',
            'form': {
                'title': {
                    'form element': 'textField',
                    'options...': 'more options'
                }
                'text': {
                    'form element': 'textareaField',
                    'options...': 'more options'
                }
            }
        }
* the function or method reads the "form" entry an builds the wtforms form
