$(function () {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
        if (event.which == 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        let languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: { lang: languageCode },
            success: function(response) {
                $('#hello').text(response.hello);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching translation:', error);
            }
        });
    }
});
