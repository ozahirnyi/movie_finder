$('form.favorite').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: '/favorites/',
        type: 'POST',
        data: {
            'movie': $(this).serialize(),
        },
        dataType: 'json',
        success: function (response) {
            if (response.result === 'ok') {
                alert(response.message);
            } else {
                alert('Failed');
            }
        }
    });
})

$('form.del_favorite').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: '/favorites/',
        type: 'DELETE',
        data: {
            'movie_id': $(this).serialize(),
        },
        dataType: 'json',
        success: function (response) {
            if (response.result === 'ok') {
                alert(response.message);
            } else {
                alert('Failed');
            }
        }
    });
})