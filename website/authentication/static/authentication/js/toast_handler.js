'use strict';

$(document).ready(function () {
    $.each($('.toast'), function () {
        let errorField = $(this).attr('data-error-field')
        if (errorField){
            $('#' + errorField).addClass('is-invalid')
        }

        $(this).addClass('show')
    });

    if ( $('.toast' ).attr('data-error-field') ){
        $.each($('input'), function(){
            if( !$(this).hasClass('is-invalid') ){
                $(this).addClass('is-valid')
            }
        });
    }

    $('.toast .btn-close').click(function () {
        $(this).parent().parent().removeClass('show')
    });
});