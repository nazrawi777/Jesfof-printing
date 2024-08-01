(function($) {
    'use strict';
	
	// Mobile Menu
    $('.mobile-menu nav').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
		meanMenuOpen: "<span></span> <span></span> <span></span>",
        onePage: false,
    });	

    // sticky
    var wind = $(window);
    var sticky = $('#sticky-header');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

    // Loder  //
    $(function () {
      $('body').addClass('loaded');
    });

    // accordion js
        jQuery(document).ready(function($) {
            "use strict";

            $(".accordion > li:eq(0) a").addClass("active").next().slideDown();

            $(".accordion a").click(function (j) {
                var dropDown = $(this).closest("li").find("p");

                $(this).closest(".accordion").find("p").not(dropDown).slideUp();

                if ($(this).hasClass("active")) {
                    $(this).removeClass("active");
                } else {
                    $(this).closest(".accordion").find("a.active").removeClass("active");
                    $(this).addClass("active");
                }

                dropDown.stop(false, true).slideToggle();

                j.preventDefault();
            });

        });

     // Case Study Active
    $('.portfolio-list').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 10000,
        dots: false,
        nav: false,
        navText: ["<i class='fa fa-long-arrow-left''></i>", "<i class='fa fa-long-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1000: {
                items: 5
            },
            1920: {
                items: 5
            }
        }
    })

    // Case Study Active
    $('.portfolio-list2').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 10000,
        dots: false,
        nav: false,
        navText: ["<i class='fa fa-long-arrow-left''></i>", "<i class='fa fa-long-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1000: {
                items: 3
            },
            1920: {
                items: 3
            }
        }
    })

     // brand Active
    $('.brand-list').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 10000,
        dots: true,
        nav: false,
        navText: ["<i class='fa fa-long-arrow-left''></i>", "<i class='fa fa-long-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
            1000: {
                items: 5
            },
            1920: {
                items: 5
            }
        }
    })   
  
  // table tabs
         
     $(document).ready(function() { 

        (function ($) { 
            $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
            
            $('.tab ul.tabs li a').click(function (g) { 
                var tab = $(this).closest('.tab'), 
                index = $(this).closest('li').index();
                
                tab.find('ul.tabs > li').removeClass('current');
                $(this).closest('li').addClass('current');
                
                tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
                tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
                
                g.preventDefault();
            } );
        })(jQuery);

    });
	/*---------------------
    WOW active js 
    --------------------- */
    new WOW().init();

    // counterUp
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

	
	 // Venubox

    $('.venobox').venobox({

        numeratio: true,

        infinigall: true

    });

    // <!--top button java script  -->
        
        $(window).on('scroll', function () {
            var scrolled = $(window).scrollTop();
            if (scrolled > 300) $('.go-top').addClass('active');
            if (scrolled < 300) $('.go-top').removeClass('active');
        });

        $('.go-top').on('click', function () {
            $("html, body").animate({
                scrollTop: "0"
            }, 1200);
        });

     // button count
        var num;

        $('.button-count1:first-child').click(function(){
          num = parseInt($('input:text').val());
          if (num > 1) {
            $('input:text').val(num - 1);
        }
        if (num == 2) {
            $('.button-count1:first-child').prop('disabled', true);
        }
        if (num == 10) {
            $('.button-count:last-child').prop('disabled', false);
        }
    });

        $('.button-count:last-child').click(function(){
          num = parseInt($('input:text').val());
          if (num < 10) {
            $('input:text').val(num + 1);
        }
        if (num > 0) {
            $('.button-count1:first-child').prop('disabled', false);
        }
        if (num == 9) {
            $('.button-count:last-child').prop('disabled', true);
        }
    });

     /* Portfolio Isotope  */
    $('.image_load').imagesLoaded(function() {

        if ($.fn.isotope) {

            var $portfolio = $('.image_load');

            $portfolio.isotope({

                itemSelector: '.grid-item',

                filter: '*',

                resizesContainer: true,

                layoutMode: 'masonry',

                transitionDuration: '0.8s'

            });
            $('.menu-filtering li').on('click', function() {

                $('.menu-filtering li').removeClass('current_menu_item');

                $(this).addClass('current_menu_item');

                var selector = $(this).attr('data-filter');

                $portfolio.isotope({

                    filter: selector,

                });

            });

        };
    });
	/*--------------------------
     scrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    })






    
})(jQuery);