# -*- coding: utf-8 -*-
import os
from PIL import Image
from flask import current_app as app
from app.base.utils.files import extend_filename


def resize_image(image, width=0, height=0, name_addition='_resized',
                 resize_small_image=False):
    """Resizes an image by given with and/or height"""

    # opens image
    try:
        img = Image.open(image)
    except IOError, e:
        app.logger.error(e)
        return False

    # If image has smaller width than given, than pass resize.
    if resize_small_image:
        if img.size[0] > width:
            return True

    image = extend_filename(image, name_addition)

    # check if only resize on width
    if width and not height:
        widthPercent = (width / float(img.size[0]))
        height = int(float(img.size[1]) * float(widthPercent))
    elif height and not width:
        pass

    img = img.resize((width, height), Image.BILINEAR)

    try:
        img.save(image)
    except IOError, e:
        app.logger.error(e)
        return False
