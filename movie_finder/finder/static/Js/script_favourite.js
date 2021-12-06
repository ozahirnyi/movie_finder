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