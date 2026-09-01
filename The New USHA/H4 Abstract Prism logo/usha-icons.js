// USHA icon suite — 24×24 grid, stroke 1.8 round, currentColor, one gold accent dot where marked.
(function () {
  const A = '#FFB703'; // accent dot color (overridable via ushaIconSvg opts)
  const S = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"';
  const dot = (x, y, r, c) => `<circle cx="${x}" cy="${y}" r="${r || 1.7}" fill="${c || A}" stroke="none"/>`;
  window.USHA_ICONS = {
    'h2': `<path ${S} d="M6 5v14M14 5v14M6 12h8"/>` + dot(18.5, 17.5, 2),
    'bolt': `<path ${S} d="M13 2 5 14h6l-1 8 8-12h-6l1-8z"/>`,
    'molecule': `<circle ${S} cx="7" cy="12" r="3"/><circle ${S} cx="17" cy="6.5" r="2.4"/><circle ${S} cx="17" cy="17.5" r="2.4"/><path ${S} d="M9.7 10.5 14.8 7.6M9.7 13.5l5.1 2.9"/>` + dot(7, 12, 1.3),
    'drop': `<path ${S} d="M12 3C12 3 6 10 6 14.5a6 6 0 0 0 12 0C18 10 12 3 12 3z"/>` + dot(12, 15, 1.6),
    'flame': `<path ${S} d="M12 3c1.2 3 5 5.2 5 9.8A5 5 0 0 1 7 12.8c0-1.8.8-3.2 1.9-4.6.5 1 1.3 1.6 2.1 1.8C10.6 7.6 10.9 5.2 12 3z"/>`,
    'atom': `<ellipse ${S} cx="12" cy="12" rx="9" ry="3.6"/><ellipse ${S} cx="12" cy="12" rx="9" ry="3.6" transform="rotate(60 12 12)"/><ellipse ${S} cx="12" cy="12" rx="9" ry="3.6" transform="rotate(120 12 12)"/>` + dot(12, 12, 1.8),
    'tank': `<rect ${S} x="8" y="3" width="8" height="18" rx="4"/><path ${S} d="M8 8.5h8"/>` + dot(12, 15, 1.6),
    'pipeline': `<path ${S} d="M2 9h13a4 4 0 0 1 0 8H9"/><path ${S} d="M6 6.5v5M2 6.5v5" transform="translate(0 0)"/>` + dot(9, 17, 1.6),
    'truck': `<rect ${S} x="2" y="7" width="11" height="8"/><path ${S} d="M13 10h4l3 3v2h-7z"/><circle ${S} cx="6.5" cy="17.5" r="1.8"/><circle ${S} cx="16.5" cy="17.5" r="1.8"/>` + dot(7.5, 11, 1.4),
    'pump': `<rect ${S} x="4" y="4" width="9" height="16" rx="1.5"/><path ${S} d="M6.5 8h4M13 9.5h2.6v6.5a1.9 1.9 0 0 0 3.8 0V9l-2.2-2.2"/>`,
    'factory': `<path ${S} d="M3 21V10l5 3v-3l5 3v-3l8 4v7H3z"/><path ${S} d="M5 8V4h2.5v5.5"/>` + dot(17, 17.5, 1.5),
    'anchor': `<circle ${S} cx="12" cy="5" r="2"/><path ${S} d="M12 7v13M5 12H3a9 9 0 0 0 18 0h-2"/>`,
    'capitol': `<path ${S} d="M5 21h14M6 21v-6h12v6M8 15v-4h8v4M12 5.5 16 11H8z"/>` + dot(12, 3.6, 1.5),
    'document': `<path ${S} d="M7 3h7l4 4v14H7z"/><path ${S} d="M14 3v4h4M10 12h5M10 16h5"/>`,
    'chart': `<path ${S} d="M4 4v16h16"/><path ${S} d="M8 16v-4M12.5 16V8M17 16v-6"/>` + dot(12.5, 5.6, 1.6),
    'globe': `<circle ${S} cx="12" cy="12" r="9"/><ellipse ${S} cx="12" cy="12" rx="4" ry="9"/><path ${S} d="M3.6 9.2h16.8M3.6 14.8h16.8"/>`,
    'pin': `<path ${S} d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/>` + dot(12, 10, 1.9),
    'calendar': `<rect ${S} x="4" y="5" width="16" height="16" rx="2"/><path ${S} d="M4 10h16M8 3v4M16 3v4"/>` + dot(12, 15.5, 1.6),
    'mail': `<rect ${S} x="3" y="5" width="18" height="14" rx="2"/><path ${S} d="M3.5 7.5 12 13.5l8.5-6"/>`,
    'user': `<circle ${S} cx="12" cy="8" r="3.5"/><path ${S} d="M5 20a7 7 0 0 1 14 0"/>`,
    'users': `<circle ${S} cx="9" cy="9" r="3"/><path ${S} d="M3.5 20a5.5 5.5 0 0 1 11 0"/><path ${S} d="M15.5 6.6a3 3 0 0 1 0 4.9M17 14.5a5.5 5.5 0 0 1 3.5 5.1"/>`,
    'search': `<circle ${S} cx="11" cy="11" r="6"/><path ${S} d="M15.6 15.6 21 21"/>`,
    'gear': `<circle ${S} cx="12" cy="12" r="3.2"/><path ${S} d="M12 2.8v3M12 18.2v3M2.8 12h3M18.2 12h3M5.5 5.5l2.1 2.1M16.4 16.4l2.1 2.1M18.5 5.5l-2.1 2.1M7.6 16.4l-2.1 2.1"/>`,
    'download': `<path ${S} d="M12 3v12M7 10l5 5 5-5M4 21h16"/>`,
    'external': `<path ${S} d="M14 3h7v7M21 3l-9 9M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>`,
    'play': `<path ${S} d="M8 5v14l11-7z"/>`,
    'check': `<path ${S} d="M4 12.5 10 18 20 6"/>`,
    'close': `<path ${S} d="M5.5 5.5l13 13M18.5 5.5l-13 13"/>`,
    'plus': `<path ${S} d="M12 5v14M5 12h14"/>`,
    'arrow-right': `<path ${S} d="M3 12h17M14 5.5 20.5 12 14 18.5"/>`,
    'chevron-down': `<path ${S} d="M5 9l7 7 7-7"/>`,
    'menu': `<path ${S} d="M4 6h16M4 12h16M4 18h11"/>` + dot(19.2, 18, 1.6),
    'info': `<circle ${S} cx="12" cy="12" r="9"/><path ${S} d="M12 11v5.5"/>` + dot(12, 7.6, 1.4),
    'alert': `<path ${S} d="M12 3.5 2.5 20h19L12 3.5z"/><path ${S} d="M12 10v4.5"/>` + dot(12, 17.2, 1.3),
    'shield': `<path ${S} d="M12 3l8 3v6c0 5-3.8 7.9-8 9-4.2-1.1-8-4-8-9V6z"/><path ${S} d="M8.5 12l2.4 2.4L15.5 9.5"/>`,
    'star': `<path ${S} d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/>`,
    'qr': `<rect x="4" y="4" width="6" height="6" fill="currentColor" rx="1"/><rect x="14" y="4" width="6" height="6" fill="currentColor" rx="1"/><rect x="4" y="14" width="6" height="6" fill="currentColor" rx="1"/><rect x="14" y="14" width="2.6" height="2.6" fill="currentColor"/><rect x="17.4" y="17.4" width="2.6" height="2.6" fill="${A}"/><rect x="14" y="17.4" width="2.6" height="2.6" fill="currentColor" opacity="0.45"/>`
  };
  window.ushaIconSvg = function (name, opts) {
    opts = opts || {};
    const size = opts.size || 24, color = opts.color || '#0D1B2A';
    let inner = window.USHA_ICONS[name] || '';
    if (opts.accent) inner = inner.split('#FFB703').join(opts.accent);
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="${size}" height="${size}" style="color:${color};display:block">${inner}</svg>`;
  };
})();
