$('form.favourite').on('submit',function (e){
    e.preventDefault();
	console.log('test')
    $.ajax({
		url: '/',
		method: 'post',
		data: $(this).serialize(),
		success: function(data){
            console.log('success')
		}
	});
})

$('form.del_favorite').on('submit',function (e){
    e.preventDefault();
	console.log('test')
    $.ajax({
		url: '/',
		method: 'DELETE',
		data: $(this).serialize(),
		success: function(data){
            console.log('success')
		}
	});
})