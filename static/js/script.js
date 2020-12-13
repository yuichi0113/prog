// ハンバーガーメニュー
$(function() {
    $('.hamburger').click(function() {
        $(this).toggleClass('active');
 
        if ($(this).hasClass('active')) {
            $('.globalMenuSp').addClass('active');
        } else {
            $('.globalMenuSp').removeClass('active');
        }
    });
});

// ログインアニメ
$(function() {
	setTimeout(function(){
		$('.start p').fadeIn(500);
	},300); //0.3秒後にロゴをフェードイン
	setTimeout(function(){
		$('.start').fadeOut(500);
	},1500); //1.5秒後にフェードアウト
});