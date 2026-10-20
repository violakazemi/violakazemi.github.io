/* Portfolio analytics events for Umami (cloud.umami.is).
   Page views, referrers, UTM tags and time on page are tracked by Umami itself.
   This file adds: scroll depth on each page, and clicks on resume / email / social links. */
(function () {
  function send(name, data) {
    try {
      if (window.umami && typeof window.umami.track === 'function') {
        window.umami.track(name, data);
      }
    } catch (e) {}
  }

  var page = location.pathname.replace(/\.html$/, '') || '/';

  /* Scroll depth: fires once per page at 50% and 90%. */
  var marks = [50, 90];
  var sent = {};
  var ticking = false;
  function checkScroll() {
    ticking = false;
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    if (max <= 0) return;
    var pct = (window.scrollY / max) * 100;
    marks.forEach(function (m) {
      if (pct >= m && !sent[m]) {
        sent[m] = true;
        send('scroll-' + m, { page: page });
      }
    });
  }
  window.addEventListener('scroll', function () {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(checkScroll);
    }
  }, { passive: true });

  /* Link clicks: resume, email, LinkedIn, Behance, Dribbble. */
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var name = null;
    if (/\.pdf($|\?)/i.test(href)) name = 'resume-download';
    else if (/^mailto:/i.test(href)) name = 'email-click';
    else if (/linkedin\.com/i.test(href)) name = 'linkedin-click';
    else if (/behance\.net/i.test(href)) name = 'behance-click';
    else if (/dribbble\.com/i.test(href)) name = 'dribbble-click';
    if (name) send(name, { page: page });
  });
})();
