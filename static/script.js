$( document ).ready( function(){

    $('#getTimeBtn').click(function(){
        $.getJSON( "/get-time", function( data ) {
            $('#timeSpan1').text( data.time );
        });
    });

    $('#submit').click(function(){
        var timezone = $('#timezone').val();

        $.getJSON( "/time-converter?tz=" + timezone, function( data ) {
            $('#timeSpan2').text( data.time );
        });
    });

});
