<<<<<<< HEAD
// ハンバーガーメニュー
$(function() {
    const hum = $('#hamburger, .close')
    const nav = $('.sp-nav')
    hum.on('click', function(){
       nav.toggleClass('toggle');
    });
 });
// ハンバーガーメニュー
=======
// mappage

$.fn.stairwayNav = function (options) {

    var defaults = {
        stairs: 3
    };
    this.options = $.extend({}, defaults, options);
    var stairs = this.options.stairs;

    var allLinks = this.find("a");

    allLinks
        .mouseenter(function () {
            $(this).addClass("active-1");
            var index = $(this).index(),
                i, bef, aft;
            for (i = 1; i < stairs; i++) {

                bef = index - i;
                aft = index + i;

                allLinks.eq(aft).addClass("active-" + (i + 1));
                if (bef > 0) {
                    allLinks.eq(bef).addClass("active-" + (i + 1));
                }
            }
        })
        .mouseleave(function () {
            allLinks.removeClass("active-1 active-2 active-3 active-4");
        });
    return this;
};
$(function () {
    $('.hamburger').click(function () {
        $(this).toggleClass('active');

        if ($(this).hasClass('active')) {
            $('.globalMenuSp').addClass('active');
        } else {
            $('.globalMenuSp').removeClass('active');
        }
    });
});
>>>>>>> 1a1a9b6e8c2fcfdedd7f100452eec2ee50c72f8c
