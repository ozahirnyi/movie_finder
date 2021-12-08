$('form.favorite').on('submit',function (e){
    e.preventDefault();
	console.log('test')
    $.ajax({
		url: '/favorite/',
		method: 'post',
		data: $(this).serialize(),
		success: function(data){
            console.log('success add')
		}
	});
})

$('form.del_favorite').on('submit',function (e){
    e.preventDefault();
	console.log('test')
    $.ajax({
		url: '/favorite/',
		method: 'DELETE',
		data: $(this).serialize(),
		success: function(data){
            console.log('success delete')
		}
	});
})