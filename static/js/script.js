
$(".menu-trigger").click(function(){
  $(this).addClass("menu-trigger--active");
  $('.menu').show();
  $('.menu__bg').addClass("menu__bg--active");
  $('.menu__container').addClass("menu__container--active");
});

$(".menu__close").click(function(){
  $(".menu-trigger").removeClass("menu-trigger--active");
  $('.menu').hide();
  $('.menu__bg').removeClass("menu__bg--active");
  $('.menu__container').removeClass("menu__container--active");
});