/*
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
*/

// MAIN DOCUMENT READY FUNTION
$(document).ready(function() {
    
    $('#no').click(function() {
       if($('#no').is(':checked'))
        {
            $('#length').val('0').prop('disabled', true).addClass('no');
            $('#width').val('0').prop('disabled', true).addClass('no');
        }
    });
    
    $('#yes').click(function() {
       if($('#yes').is(':checked'))
        {
            $('#length').val(undefined).prop('disabled', false).removeClass('no');
            $('#width').val(undefined).prop('disabled', false).removeClass('no');
        }
    });
    
});

