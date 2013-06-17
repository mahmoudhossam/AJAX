$('#form').submit(function(event) {
        event.preventDefault();
        $('body #preview').load('/md', {'text': $('#text').val()});
        return true;
});

$('#form #text').keyup(function() {
        $('#form').submit();
});
