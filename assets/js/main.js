

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$wrapper = $('#wrapper'),
		$header = $('#header'),
		$banner = $('#banner');

	// Breakpoints.
		breakpoints({
			xlarge:    ['1281px',   '1680px'   ],
			large:     ['981px',    '1280px'   ],
			medium:    ['737px',    '980px'    ],
			small:     ['481px',    '736px'    ],
			xsmall:    ['361px',    '480px'    ],
			xxsmall:   [null,       '360px'    ]
		});

	/**
	 * Applies parallax scrolling to an element's background image.
	 * @return {jQuery} jQuery object.
	 */
	$.fn._parallax = (browser.name == 'ie' || browser.name == 'edge' || browser.mobile) ? function() { return $(this) } : function(intensity) {

		var	$window = $(window),
			$this = $(this);

		if (this.length == 0 || intensity === 0)
			return $this;

		if (this.length > 1) {

			for (var i=0; i < this.length; i++)
				$(this[i])._parallax(intensity);

			return $this;

		}

		if (!intensity)
			intensity = 0.25;

		$this.each(function() {

			var $t = $(this),
				on, off;

			on = function() {

				$t.css('background-position', 'center 100%, center 100%, center 0px');

				$window
					.on('scroll._parallax', function() {

						var pos = parseInt($window.scrollTop()) - parseInt($t.position().top);

						$t.css('background-position', 'center ' + (pos * (-1 * intensity)) + 'px');

					});

			};

			off = function() {

				$t
					.css('background-position', '');

				$window
					.off('scroll._parallax');

			};

			breakpoints.on('<=medium', off);
			breakpoints.on('>medium', on);

		});

		$window
			.off('load._parallax resize._parallax')
			.on('load._parallax resize._parallax', function() {
				$window.trigger('scroll');
			});

		return $(this);

	};

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Clear transitioning state on unload/hide.
		$window.on('unload pagehide', function() {
			window.setTimeout(function() {
				$('.is-transitioning').removeClass('is-transitioning');
			}, 250);
		});

	// Fix: Enable IE-only tweaks.
		if (browser.name == 'ie' || browser.name == 'edge')
			$body.addClass('is-ie');

	// Scrolly.
		$('.scrolly').scrolly({
			offset: function() {
				return $header.height() - 2;
			}
		});

	// Tiles.
		var $tiles = $('.tiles > article');

		$tiles.each(function() {

			var $this = $(this),
				$image = $this.find('.image'), $img = $image.find('img'),
				$link = $this.find('.link'),
				x;

			// Image.

				// Set image.
					$this.css('background-image', 'url(' + $img.attr('src') + ')');

				// Set position.
					if (x = $img.data('position'))
						$image.css('background-position', x);

				// Hide original.
					$image.hide();

			// Link.
				if ($link.length > 0) {

					$x = $link.clone()
						.text('')
						.addClass('primary')
						.appendTo($this);

					$link = $link.add($x);

					$link.on('click', function(event) {

						var href = $link.attr('href');

						// Prevent default.
							event.stopPropagation();
							event.preventDefault();

						// Target blank?
							if ($link.attr('target') == '_blank') {

								// Open in new tab.
									window.open(href);

							}

						// Otherwise ...
							else {

								// Start transitioning.
									$this.addClass('is-transitioning');
									$wrapper.addClass('is-transitioning');

								// Redirect.
									window.setTimeout(function() {
										location.href = href;
									}, 500);

							}

					});

				}

		});

	// Header.
		if ($banner.length > 0
		&&	$header.hasClass('alt')) {

			$window.on('resize', function() {
				$window.trigger('scroll');
			});

			$window.on('load', function() {

				$banner.scrollex({
					bottom:		$header.height() + 10,
					terminate:	function() { $header.removeClass('alt'); },
					enter:		function() { $header.addClass('alt'); },
					leave:		function() { $header.removeClass('alt'); $header.addClass('reveal'); }
				});

				window.setTimeout(function() {
					$window.triggerHandler('scroll');
				}, 100);

			});

		}

	// Banner.
		$banner.each(function() {

			var $this = $(this),
				$image = $this.find('.image'), $img = $image.find('img');

			// Parallax.
				$this._parallax(0.275);

			// Image.
				if ($image.length > 0) {

					// Set image.
						$this.css('background-image', 'url(' + $img.attr('src') + ')');

					// Hide original.
						$image.hide();

				}

		});

	// Menu.
		var $menu = $('#menu'),
			$menuInner;

		$menu.wrapInner('<div class="inner"></div>');
		$menuInner = $menu.children('.inner');
		$menu._locked = false;

		$menu._lock = function() {

			if ($menu._locked)
				return false;

			$menu._locked = true;

			window.setTimeout(function() {
				$menu._locked = false;
			}, 350);

			return true;

		};

		$menu._show = function() {

			if ($menu._lock())
				$body.addClass('is-menu-visible');

		};

		$menu._hide = function() {

			if ($menu._lock())
				$body.removeClass('is-menu-visible');

		};

		$menu._toggle = function() {

			if ($menu._lock())
				$body.toggleClass('is-menu-visible');

		};

		$menuInner
			.on('click', function(event) {
				event.stopPropagation();
			})
			.on('click', 'a', function(event) {

				var href = $(this).attr('href');

				event.preventDefault();
				event.stopPropagation();

				// Hide.
					$menu._hide();

				// Redirect.
					window.setTimeout(function() {
						window.location.href = href;
					}, 250);

			});

		$menu
			.appendTo($body)
			.on('click', function(event) {

				event.stopPropagation();
				event.preventDefault();

				$body.removeClass('is-menu-visible');

			})
			.append('<a class="close" href="#menu">Close</a>');

		$body
			.on('click', 'a[href="#menu"]', function(event) {

				event.stopPropagation();
				event.preventDefault();

				// Toggle.
					$menu._toggle();

			})
			.on('click', function(event) {

				// Hide.
					$menu._hide();

			})
			.on('keydown', function(event) {

				// Hide on escape.
					if (event.keyCode == 27)
						$menu._hide();

			});

		// Carousel dot pagination scroll sync and click navigation
		var $tilesContainer = $('.tiles');
		var $dots = $('.carousel-indicators .dot');
		var $prevBtn = $('.carousel-nav-btn.prev-btn');
		var $nextBtn = $('.carousel-nav-btn.next-btn');

		if ($tilesContainer.length > 0) {
			$tilesContainer.on('scroll', function() {
				var scrollLeft = $tilesContainer.scrollLeft();
				var maxScrollLeft = $tilesContainer[0].scrollWidth - $tilesContainer.width();
				
				// Sync dots
				if ($dots.length > 0 && maxScrollLeft > 0) {
					var index = Math.round((scrollLeft / maxScrollLeft) * ($dots.length - 1));
					$dots.removeClass('active');
					$dots.eq(index).addClass('active');
				}

				// Toggle prev button visibility
				if (scrollLeft > 15) {
					$prevBtn.css({ 'opacity': '1', 'pointer-events': 'auto' });
				} else {
					$prevBtn.css({ 'opacity': '0', 'pointer-events': 'none' });
				}

				// Toggle next button visibility
				if (scrollLeft < maxScrollLeft - 15) {
					$nextBtn.css({ 'opacity': '1', 'pointer-events': 'auto' });
				} else {
					$nextBtn.css({ 'opacity': '0', 'pointer-events': 'none' });
				}
			});

			if ($dots.length > 0) {
				$dots.on('click', function() {
					var index = $(this).data('slide');
					var maxScrollLeft = $tilesContainer[0].scrollWidth - $tilesContainer.width();
					var scrollToVal = $dots.length > 1 ? (index / ($dots.length - 1)) * maxScrollLeft : 0;
					$tilesContainer.animate({ scrollLeft: scrollToVal }, 300);
				});
			}

			$nextBtn.on('click', function() {
				var scrollAmount = $tilesContainer.width() * 0.75;
				$tilesContainer.animate({ scrollLeft: $tilesContainer.scrollLeft() + scrollAmount }, 300);
			});

			$prevBtn.on('click', function() {
				var scrollAmount = $tilesContainer.width() * 0.75;
				$tilesContainer.animate({ scrollLeft: $tilesContainer.scrollLeft() - scrollAmount }, 300);
			});
		}

	document.addEventListener('DOMContentLoaded', () => {
    // 1. THE MASTER QUEUE: Define your project order here once.
    // To add a new project tomorrow, just add "new-project.html" to this list!
   // 1. THE MASTER QUEUE: Define your clean URLs here (NO .html)
const projects = [
    "museum", 
    "golaab", 
    "tomaan", 
    "promptlab-carbon"
];

// 2. Find out what page the user is currently looking at
let currentPage = window.location.pathname.split('/').pop(); 

// Safeguard: If testing locally on your computer, strip the .html out
currentPage = currentPage.replace('.html', '');

// 3. Find where this page sits in the master queue
const currentIndex = projects.indexOf(currentPage);

// 4. If we are on a project page, calculate the next and previous pages
if (currentIndex !== -1) {
    
    // This math seamlessly loops the queue from start to finish and back again
    const prevIndex = (currentIndex - 1 + projects.length) % projects.length;
    const nextIndex = (currentIndex + 1) % projects.length;

    // 5. Inject the clean links into the HTML buttons
    const prevBtn = document.getElementById('btn-prev-project');
    const nextBtn = document.getElementById('btn-next-project');

    if (prevBtn) prevBtn.href = projects[prevIndex];
    if (nextBtn) nextBtn.href = projects[nextIndex];
}
