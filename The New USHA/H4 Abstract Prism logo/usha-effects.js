// USHA effects — favicon animator, cursor glow, magnetic buttons, ripple, scroll reveal, all via data-attributes.
(function () {
  const GOLD = '#FFB703', CYAN = '#00D2FF', PURPLE = '#9D4EDD', NAVY = '#0D1B2A', ICE = '#F8F9FA';

  // ---- Animated favicon: dotted-H pulse, 8 frames @140ms ----
  const HGRID = []; // 4-col H on 8x9 grid (cols 0,1,6,7 + crossbar rows 3-5)
  for (let r = 0; r < 9; r++) for (let c = 0; c < 8; c++) {
    if (c < 2 || c > 5 || (r > 2 && r < 6)) HGRID.push([c, r]);
  }
  const HCOLORS = i => [CYAN, '#00A8CC', GOLD, PURPLE][i % 4];
  let favTimer = null, favPhase = 0, favLink = null;
  function drawFav(phase) {
    const cv = document.createElement('canvas'); cv.width = cv.height = 32;
    const ctx = cv.getContext('2d');
    ctx.fillStyle = NAVY; ctx.beginPath(); ctx.arc(16, 16, 16, 0, 7); ctx.fill();
    HGRID.forEach(([c, r], i) => {
      const pulse = 1 + 0.4 * Math.sin(phase + i * 0.5);
      ctx.fillStyle = HCOLORS(i);
      ctx.beginPath(); ctx.arc(6 + c * 2.9, 4.5 + r * 2.6, 1.05 * pulse, 0, 7); ctx.fill();
    });
    return cv.toDataURL('image/png');
  }
  window.USHAFavicon = {
    start() {
      if (favTimer) return;
      favLink = document.querySelector('link[rel="icon"]');
      if (!favLink) { favLink = document.createElement('link'); favLink.rel = 'icon'; document.head.appendChild(favLink); }
      favTimer = setInterval(() => { favPhase += 0.55; favLink.href = drawFav(favPhase); }, 140);
    },
    stop() { clearInterval(favTimer); favTimer = null; if (favLink) favLink.href = drawFav(0); },
    toggle() { favTimer ? this.stop() : this.start(); },
    running() { return !!favTimer; }
  };

  // ---- Cursor glow: [data-usha-glow] — radial spotlight follows the mouse ----
  document.addEventListener('mousemove', e => {
    const el = e.target.closest && e.target.closest('[data-usha-glow]');
    document.querySelectorAll('[data-usha-glow].__glowing').forEach(g => { if (g !== el) { g.classList.remove('__glowing'); g.style.backgroundImage = ''; } });
    if (!el) return;
    const r = el.getBoundingClientRect();
    const x = e.clientX - r.left, y = e.clientY - r.top;
    const color = el.getAttribute('data-usha-glow') || 'rgba(0,210,255,0.22)';
    el.classList.add('__glowing');
    el.style.backgroundImage = `radial-gradient(220px circle at ${x}px ${y}px, ${color}, transparent 70%)`;
  }, true);

  // ---- Magnetic: [data-usha-magnet] — element leans toward the cursor, springs back ----
  document.addEventListener('mousemove', e => {
    const el = e.target.closest && e.target.closest('[data-usha-magnet]');
    document.querySelectorAll('[data-usha-magnet].__mag').forEach(m => { if (m !== el) { m.classList.remove('__mag'); m.style.transform = ''; m.style.transition = 'transform 0.35s cubic-bezier(0.2,0.8,0.3,1.2)'; } });
    if (!el) return;
    const r = el.getBoundingClientRect();
    const dx = (e.clientX - (r.left + r.width / 2)) / r.width, dy = (e.clientY - (r.top + r.height / 2)) / r.height;
    el.classList.add('__mag');
    el.style.transition = 'transform 0.12s ease-out';
    el.style.transform = `translate(${dx * 8}px, ${dy * 6}px)`;
  }, true);

  // ---- Ripple: [data-usha-ripple] — gold dot expands from the click point ----
  document.addEventListener('click', e => {
    const el = e.target.closest && e.target.closest('[data-usha-ripple]');
    if (!el) return;
    const r = el.getBoundingClientRect();
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    el.style.overflow = 'hidden';
    const dot = document.createElement('span');
    const size = Math.max(r.width, r.height) * 2.2;
    dot.style.cssText = `position:absolute;border-radius:50%;pointer-events:none;background:${el.getAttribute('data-usha-ripple') || 'rgba(13,27,42,0.25)'};width:${size}px;height:${size}px;left:${e.clientX - r.left - size / 2}px;top:${e.clientY - r.top - size / 2}px;transform:scale(0);opacity:0.9;transition:transform 0.55s ease-out, opacity 0.6s ease-out`;
    el.appendChild(dot);
    requestAnimationFrame(() => { dot.style.transform = 'scale(1)'; dot.style.opacity = '0'; });
    setTimeout(() => dot.remove(), 650);
  }, true);

  // ---- Scroll reveal: [data-usha-reveal] fades+rises on entry; values: up|left|right|scale ----
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.style.opacity = '1'; en.target.style.transform = 'none'; io.unobserve(en.target); } });
  }, { threshold: 0.15 });
  function prep(el) {
    if (el.__revealPrepped) return; el.__revealPrepped = true;
    const kind = el.getAttribute('data-usha-reveal') || 'up';
    const t = { up: 'translateY(28px)', left: 'translateX(-28px)', right: 'translateX(28px)', scale: 'scale(0.94)' }[kind] || 'translateY(28px)';
    el.style.opacity = '0'; el.style.transform = t;
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s cubic-bezier(0.2,0.8,0.3,1)';
    io.observe(el);
  }
  function scan() { document.querySelectorAll('[data-usha-reveal]').forEach(prep); }
  new MutationObserver(scan).observe(document.documentElement, { childList: true, subtree: true });
  if (document.readyState !== 'loading') scan(); else document.addEventListener('DOMContentLoaded', scan);
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('[data-usha-reveal]').forEach(el => { el.style.opacity = '1'; el.style.transform = 'none'; });
  }
})();
