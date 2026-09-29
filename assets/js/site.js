// Gentle scroll reveal. Content stays visible if this script never runs,
// and anything already on screen is always shown (no chance of stuck, hidden content).
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js');
  var targets = Array.prototype.slice.call(document.querySelectorAll('.section h2, .work-card, .card, .reveal'));
  function show(el) { el.classList.add('is-visible'); }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { show(e.target); io.unobserve(e.target); } });
  }, { threshold: 0 });
  targets.forEach(function (el) {
    el.classList.add('reveal');
    var i = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
    el.style.transitionDelay = Math.min(i, 3) * 70 + 'ms';
    io.observe(el);
  });
  // Safety net: after any scroll pause, show everything above the bottom of the screen.
  var t;
  function sweep() {
    var vh = window.innerHeight;
    targets.forEach(function (el) { if (!el.classList.contains('is-visible') && el.getBoundingClientRect().top < vh) show(el); });
  }
  window.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(sweep, 120); }, { passive: true });
  window.addEventListener('load', sweep);
})();
