// Shared browser behavior will be added here.

(function () {
  var settingsBtn = document.getElementById('settings-btn');
  var popup = document.getElementById('settings-popup');
  var closeBtn = document.getElementById('settings-popup-close');
  var themeSwitch = document.getElementById('theme-switch');
  var html = document.documentElement;

  var DARK_ATTR = 'data-theme';
  var DARK_VALUE = 'dark';

  function getPreferredTheme() {
    var stored = localStorage.getItem('theme');
    if (stored === 'dark' || stored === 'light') return stored;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      html.setAttribute(DARK_ATTR, DARK_VALUE);
    } else {
      html.removeAttribute(DARK_ATTR);
    }
    localStorage.setItem('theme', theme);
    if (themeSwitch) themeSwitch.checked = (theme === 'dark');
  }

  function openPopup() {
    var rect = settingsBtn.getBoundingClientRect();

    // Temporarily make it visible (but transparent) so we can measure its size.
    popup.hidden = false;
    popup.style.opacity = '0';
    popup.style.pointerEvents = 'none';

    // Force a layout so offsetWidth/offsetHeight are correct.
    var width = popup.offsetWidth || 232;
    var height = popup.offsetHeight || 108;

    var gap = 10;
    var left = rect.right + gap;
    var top = rect.top;

    // If it overflows the right edge, place it to the left of the button.
    if (left + width > window.innerWidth - 8) {
      left = rect.left - gap - width;
      if (left < 8) {
        left = Math.max(8, rect.left);
        top = rect.bottom + 10;
      }
    }

    // Keep it on-screen vertically.
    if (top + height > window.innerHeight - 8) {
      top = Math.max(8, window.innerHeight - 8 - height);
    }

    popup.style.left = left + 'px';
    popup.style.top = top + 'px';
    popup.style.opacity = '';
    popup.style.pointerEvents = '';
    popup.classList.add('is-open');
    try { settingsBtn.focus(); } catch (e) {}
  }

  function closePopup() {
    popup.classList.remove('is-open');
    // Defer hiding so the exit transition can play.
    setTimeout(function () {
      if (!popup.classList.contains('is-open')) {
        popup.hidden = true;
      }
    }, 180);
    popup.style.left = '';
    popup.style.top = '';
  }

  function onKeyDown(e) {
    if (e.key === 'Escape') { closePopup(); }
  }

  function onPopupClick(e) {
    if (!popup.contains(e.target) && e.target !== settingsBtn) {
      closePopup();
    }
  }

  function initThemeToggle() {
    if (!themeSwitch) return;
    themeSwitch.addEventListener('change', function () {
      applyTheme(themeSwitch.checked ? 'dark' : 'light');
    });
    applyTheme(getPreferredTheme());
  }

  if (settingsBtn && popup) {
    settingsBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (popup.hidden) {
        openPopup();
        document.addEventListener('keydown', onKeyDown);
        document.addEventListener('mousedown', onPopupClick);
      } else {
        closePopup();
        document.removeEventListener('keydown', onKeyDown);
        document.removeEventListener('mousedown', onPopupClick);
      }
    });

    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        closePopup();
        document.removeEventListener('keydown', onKeyDown);
        document.removeEventListener('mousedown', onPopupClick);
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !popup.hidden) {
        closePopup();
        document.removeEventListener('keydown', onKeyDown);
        document.removeEventListener('mousedown', onPopupClick);
      }
    });
  }

  initThemeToggle();
})();
