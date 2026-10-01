// ---------------------------------------------------------------------------
// Display settings: text size + increase contrast.
// Device settings apply first (prefers-contrast); a choice here overrides them
// and is remembered across pages. A tiny script in each page's <head> applies
// the saved choice before the page paints, so there's no flash.
// ---------------------------------------------------------------------------
(function () {
  var root = document.documentElement;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };
  var mqContrast = window.matchMedia ? window.matchMedia('(prefers-contrast: more)') : null;
  var nav = document.querySelector('.global-header nav');
  if (!nav) return;

  var wrap = document.createElement('div');
  wrap.className = 'display-control';
  wrap.innerHTML =
    '<button type="button" class="display-toggle" aria-expanded="false" aria-controls="display-panel">' +
      '<span class="display-toggle__glyph" aria-hidden="true">Aa</span>' +
      '<span class="display-toggle__word">Display</span>' +
    '</button>' +
    '<div class="display-panel" id="display-panel" role="dialog" aria-modal="false" aria-labelledby="display-panel-title" hidden>' +
      '<h2 class="display-panel__title" id="display-panel-title">Display</h2>' +
      '<fieldset class="display-group">' +
        '<legend>Text size</legend>' +
        '<div class="segmented">' +
          '<input type="radio" name="vk-text" id="vk-text-default" value="default"><label for="vk-text-default"><span aria-hidden="true">A</span><span class="visually-hidden">Default</span></label>' +
          '<input type="radio" name="vk-text" id="vk-text-large" value="large"><label for="vk-text-large"><span aria-hidden="true">A</span><span class="visually-hidden">Large</span></label>' +
          '<input type="radio" name="vk-text" id="vk-text-larger" value="larger"><label for="vk-text-larger"><span aria-hidden="true">A</span><span class="visually-hidden">Larger</span></label>' +
        '</div>' +
      '</fieldset>' +
      '<div class="display-switch">' +
        '<label class="display-switch__label" for="vk-contrast">Increase contrast<span class="display-switch__hint">Darker text and clearer borders</span></label>' +
        '<input type="checkbox" role="switch" class="switch" id="vk-contrast">' +
      '</div>' +
      '<button type="button" class="display-reset">Use my device settings</button>' +
    '</div>';
  nav.appendChild(wrap);

  var toggle = wrap.querySelector('.display-toggle');
  var panel = wrap.querySelector('.display-panel');
  var radios = wrap.querySelectorAll('input[name="vk-text"]');
  var contrast = wrap.querySelector('#vk-contrast');
  var reset = wrap.querySelector('.display-reset');

  function currentText() { return root.getAttribute('data-text') || 'default'; }
  function contrastOn() {
    var c = root.getAttribute('data-contrast');
    if (c === 'more') return true;
    if (c === 'standard') return false;
    return !!(mqContrast && mqContrast.matches);
  }
  function sync() {
    for (var i = 0; i < radios.length; i++) radios[i].checked = radios[i].value === currentText();
    contrast.checked = contrastOn();
  }
  sync();
  if (mqContrast && mqContrast.addEventListener) mqContrast.addEventListener('change', sync);

  for (var i = 0; i < radios.length; i++) {
    radios[i].addEventListener('change', function (e) {
      var v = e.target.value;
      if (v === 'default') { root.removeAttribute('data-text'); store.del('vk-text'); }
      else { root.setAttribute('data-text', v); store.set('vk-text', v); }
    });
  }
  contrast.addEventListener('change', function () {
    var v = contrast.checked ? 'more' : 'standard';
    // If the choice matches the device setting, drop the override so future device changes still apply.
    var device = !!(mqContrast && mqContrast.matches);
    if (contrast.checked === device) { root.removeAttribute('data-contrast'); store.del('vk-contrast'); }
    else { root.setAttribute('data-contrast', v); store.set('vk-contrast', v); }
  });
  reset.addEventListener('click', function () {
    root.removeAttribute('data-text'); root.removeAttribute('data-contrast');
    store.del('vk-text'); store.del('vk-contrast');
    sync();
    var checked = wrap.querySelector('input[name="vk-text"]:checked');
    if (checked) checked.focus();
  });

  function open() {
    panel.hidden = false;
    toggle.setAttribute('aria-expanded', 'true');
    sync();
    var checked = wrap.querySelector('input[name="vk-text"]:checked') || radios[0];
    checked.focus();
  }
  function close(returnFocus) {
    if (panel.hidden) return;
    panel.hidden = true;
    toggle.setAttribute('aria-expanded', 'false');
    if (returnFocus) toggle.focus();
  }
  toggle.addEventListener('click', function () { panel.hidden ? open() : close(true); });
  wrap.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' || e.key === 'Esc') { e.preventDefault(); close(true); }
  });
  document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) close(false); });
  wrap.addEventListener('focusout', function (e) {
    if (e.relatedTarget && !wrap.contains(e.relatedTarget)) close(false);
  });
})();

// ---------------------------------------------------------------------------
// Gentle scroll reveal. Content stays visible if this never runs, and anything
// already on screen is always shown (no chance of stuck, hidden content).
// ---------------------------------------------------------------------------
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
  var t;
  function sweep() {
    var vh = window.innerHeight;
    targets.forEach(function (el) { if (!el.classList.contains('is-visible') && el.getBoundingClientRect().top < vh) show(el); });
  }
  window.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(sweep, 120); }, { passive: true });
  window.addEventListener('load', sweep);
})();

// ---------------------------------------------------------------------------
// Copy-to-clipboard chips: <button class="copy-chip" data-copy="text">.
// The label swaps to "Copied", screen readers hear it, and it resets after 2s.
// ---------------------------------------------------------------------------
(function () {
  var chips = document.querySelectorAll('.copy-chip[data-copy]');
  if (!chips.length) return;
  var live = document.createElement('span');
  live.className = 'visually-hidden'; live.setAttribute('aria-live', 'polite');
  document.body.appendChild(live);

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text).catch(function () { return legacy(text); });
    return legacy(text);
  }
  function legacy(text) {
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy') ? resolve() : reject(); } catch (e) { reject(e); }
      document.body.removeChild(ta);
    });
  }

  Array.prototype.forEach.call(chips, function (chip) {
    var label = chip.querySelector('.copy-chip__label');
    var original = label ? label.textContent : '';
    var timer;
    chip.addEventListener('click', function () {
      copy(chip.getAttribute('data-copy')).then(function () {
        chip.classList.add('is-copied');
        if (label) label.textContent = 'Copied';
        live.textContent = ''; setTimeout(function () { live.textContent = 'Email address copied'; }, 50);
        if (navigator.vibrate) navigator.vibrate(10); // light haptic tick on Android
        clearTimeout(timer);
        timer = setTimeout(function () { chip.classList.remove('is-copied'); if (label) label.textContent = original; }, 2000);
      }, function () {
        live.textContent = 'Copy failed. The address is ' + chip.getAttribute('data-copy');
      });
    });
  });
})();
