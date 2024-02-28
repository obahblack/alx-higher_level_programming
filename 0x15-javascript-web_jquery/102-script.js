$(document).ready(function() {
    $('#btn_translate').click(function() {
        let languageCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
            .done(function(response) {
                $('#hello').text(response.hello);
            })
            .fail(function(xhr, status, error) {
                console.error('Error fetching translation:', error);
            });
    });
});
