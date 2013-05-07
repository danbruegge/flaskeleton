$(function () {
    'use strict';

    if ($('html').hasClass('lt-ie10')) {
        var $placeholder = $('[placeholder]');

        $placeholder.each(function () {
            var $that = $(this);
            if ($that.val() === '') {
                $that.val($that.attr('placeholder'));
            }
        });

        $placeholder.focusin(function () {
            var $that = $(this);

            if ($that.val() === $that.attr('placeholder')) {
                $that.val('');
            }
        }).focusout(function () {
            var $that = $(this);

            if ($that.val() == '') {
                $that.val($that.attr('placeholder'));
            }
        });
    }
});
