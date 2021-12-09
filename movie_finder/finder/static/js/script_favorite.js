$('form.favorite').on('submit', function (e) {
    e.preventDefault();
    alert($(this).serialize())
    $.ajax({
        url: '/favorites/',
        method: 'POST',
        data: {"movie_to_favorites": $(this).serialize()},
        success: function (data) {
            console.log('success add')
        }
    });
})

$('form.del_favorite').on('submit', function (e) {
    e.preventDefault();
    alert($(this).serialize())
    $.ajax({
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        url: '/favorites/',
        method: 'DELETE',
        data: {"movie_to_favorites": $(this).serialize()},
        success: function (data) {
            console.log('success delete')
        }
    });
})