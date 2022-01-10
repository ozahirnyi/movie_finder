function add_to_favorites(movie) {
    $.ajax({
        url: '/favorites/',
        type: 'POST',
        data: {
            'movie': JSON.stringify(movie),
        },
        dataType: 'json',
        success: function (json) {
            alert(json);
        }
    });
    return false;
}

function remove_from_favorites(movie_imdbid) {
    $.ajax({
        url: `/favorites/${movie_imdbid}/`,
        type: 'DELETE',
        success: function (json) {
            alert(json);
        }
    });
}
