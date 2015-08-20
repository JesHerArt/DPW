/*
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
*/

// MAIN DOCUMENT READY FUNTION
$(document).ready(function() {
    
    //function used to add a class to the length/width inputs 
    //if 'no' is selected for backyard
    $('#no').click(function() {
       if($('#no').is(':checked'))
        {
            $('#length').val('0').addClass('no');
            $('#width').val('0').addClass('no');
        }
    });
    
    //function used to remove a class to the length/width inputs 
    //if 'yes' is selected for backyard
    $('#yes').click(function() {
       if($('#yes').is(':checked'))
        {
            $('#length').val(undefined).removeClass('no');
            $('#width').val(undefined).removeClass('no');
        }
    });
    
    //when button is clicked it will refresh the page
    //for a new dog suggestion on the results page
    $('#again').click(function() {
        location.reload();
    });
    
});

