$(document).ready( function() {
    var request;
            
    $("#yamlForm").submit(function(event) {
        if(request) {
            request.abort();
        }

        var form = $(this);

        var inputs = form.find("textarea");

        var serializedData = form.serialize();

        inputs.prop("disabled", true);

        request = $.ajax({
            url: "./prsr.py",
            type: "post",
            datatype: "json",
            data: serializedData
        });

        request.done(function(response, textStatus, jqXHR) {
            $('textarea#formattedText').val(response.data);
        });

        request.fail(function(jqXHR, textStatus, errorThrown) {
            console.error("The following error occured: " + textStatus, errorThrown );
        });

        request.always(function() {
            inputs.prop("disabled", false);
        });

        event.preventDefault();
    });
});
