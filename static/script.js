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

    $('#submit1').click(function(){
        var dt = $('#time').val();
        var input_tz = $('#input_tz').val();
        var output_tz = $('#output_tz').val();

        $.getJSON( "/input-time-converter?dt=" + dt + "&input_tz=" + input_tz + "&output_tz=" + output_tz, function( data ) {
            $('#timeSpan3').text( data.time );
        });
    });

});
