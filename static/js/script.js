// ハンバーガーメニュー
$(function() {
  
    const spBreakPoint = 670;
    let headerTop = 40;
    let headerHeight = 0;

    if ($(window).width() > spBreakPoint) {
      headerHeight = 620;
    } else {
      headerHeight = 355;
    }

    $(window).on('scroll', function () {
      if ($(window).width() > spBreakPoint) {
        if ($(this).scrollTop() > headerTop) {
          $('.header__nav').addClass('position-change');
        } else {
          $('.header__nav').removeClass('position-change');
        }
      }
      if ($(this).scrollTop() > headerHeight) {
        $('.header__nav').addClass('color-chnage');
      } else {
        $('.header__nav').removeClass('color-chnage');
      }

      let workDescTop = $('#work__desc').offset().top;
      if ($(this).scrollTop() > (workDescTop - 50)) {
        $('.work').addClass('arrow_display');
      }
    });

    /*** ハンバーガーメニューの表示/非表示 ***/
    $('.hamburger-menu').on('click', function() {
      $('.hamburger-menu').toggleClass('active');
      $('.header-menu').toggleClass('height-change');
    });
    $('.header__menu__item').on('click', function() {
      $('.hamburger-menu').removeClass('active');
      $('.header-menu').toggleClass('height-change');
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