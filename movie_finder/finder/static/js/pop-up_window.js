$('input.delete_from_favorite').click(function (event) {
    $('#myOverlay').fadeIn(297, function () {
        $('#myModal')
            .css('display', 'block')
            .animate({opacity: 1 }, 198);
    });
});

$('#myModal__close, #myModal').click(function () {
    $('#myModal').animate({opacity: 0}, 198,
        function () {
            $(this).css('display', 'none');
        });

});
// $(function(){
// 	$("#del_mov").delay(5000).fadeOut(300);
// });