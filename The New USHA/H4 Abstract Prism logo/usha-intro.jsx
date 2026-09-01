// USHA animated logo intro — scenes: Spark → Assemble → Pulse → Lockup
const { SceneStage, useScene, Easing, useTweaks, TweaksPanel, TweakSection, TweakRadio, TweakToggle } = window;

const NAVY = '#0D1B2A', PAPER = '#F8F9FA', YELLOW = '#FFB703';
const rnd = (i, salt) => { const x = Math.sin(i * 127.1 + salt * 311.7) * 43758.5453; return x - Math.floor(x); };
const darkMap = { '#00a8cc': '#33dbff', '#0d1b2a': '#7ce4ff', '#00d2ff': '#5fe0ff', '#3b0b59': '#9d4edd', '#2a073f': '#8a3fc7', '#e09e00': '#ffb703', '#7ce4ff': '#a8eeff', '#6c1fa0': '#9d4edd' };
const bright = c => darkMap[c] || c;
const clamp01 = v => Math.max(0, Math.min(1, v));
// ease helpers driven by scene progress
const seg = (p, a, b, ease) => { const t = clamp01((p - a) / (b - a)); return ease ? ease(t) : t; };
const backOut = t => { const s = 1.70158; t -= 1; return t * t * ((s + 1) * t + s) + 1; };

function useLayout(vert) {
  const W = vert ? 1080 : 1920, H = vert ? 1920 : 1080;
  const D = window.USHA_DOTS.map;
  const mw = vert ? 900 : 1150;
  const s = mw / D.w, mh = D.h * s;
  return { W, H, D, s, mw, mh };
}

function MapDots({ vert, mapProg, waveT, cx, cy, scale }) {
  // mapProg: 0..1 assembly; waveT: -0.4..1.4 wave position (null = off)
  const { W, H, D, s, mw, mh } = useLayout(vert);
  const ox = (cx ?? W / 2) - mw / 2, oy = (cy ?? H / 2) - mh / 2;
  return (
    <g transform={scale && scale !== 1 ? `translate(${cx ?? W / 2},${cy ?? H / 2}) scale(${scale}) translate(${-(cx ?? W / 2)},${-(cy ?? H / 2)})` : undefined}>
      {D.dots.map((d, i) => {
        const tx = ox + d.x * s, ty = oy + d.y * s;
        let x = tx, y = ty, r = d.r * s, op = 1, fill = bright(d.c);
        if (mapProg !== null && mapProg < 1) {
          const delay = 0.55 * (d.x / D.w) + 0.2 * rnd(i, 1);
          const t = clamp01((mapProg - delay * 0.9) / (1 - delay * 0.9));
          const e = backOut(clamp01(t * 1.05));
          const a = rnd(i, 2) * Math.PI * 2, dist = (0.35 + rnd(i, 3) * 0.65) * (vert ? 900 : 1100) * (1 - e);
          x = tx + Math.cos(a) * dist * 0.15 + (W / 2 - tx) * (1 - e);
          y = ty + Math.sin(a) * dist * 0.15 + (H / 2 - ty) * (1 - e);
          r = d.r * s * Math.max(0.001, e);
          op = clamp01(t * 3);
        }
        if (waveT !== null && waveT !== undefined) {
          const dn = d.x / D.w;
          const g = Math.exp(-Math.pow((dn - waveT) * 7, 2));
          r = r * (1 + 0.45 * g);
        }
        return <circle key={i} cx={x} cy={y} r={r} fill={fill} opacity={op} />;
      })}
    </g>
  );
}

function Spark({ vert }) {
  const { localTime, progress } = useScene();
  const { W, H } = useLayout(vert);
  const p = progress;
  const grow = seg(p, 0, 0.45, Easing.elasticOut || backOut);
  const breathe = 1 + 0.12 * Math.sin(p * Math.PI * 3) * (1 - p);
  const r = 10 + 40 * grow * breathe;
  const rings = [0.25, 0.55].map((st, k) => {
    const t = seg(p, st, 1);
    return <circle key={k} cx={W / 2} cy={H / 2} r={50 + t * (vert ? 420 : 520)} fill="none" stroke={YELLOW} strokeWidth={2.5 * (1 - t)} opacity={0.7 * (1 - t)} />;
  });
  const orbits = Array.from({ length: 10 }, (_, i) => {
    const t = seg(p, 0.45, 1);
    const a = i / 10 * Math.PI * 2 + p * 1.2;
    const dist = 90 + t * 60;
    return <circle key={'o' + i} cx={W / 2 + Math.cos(a) * dist} cy={H / 2 + Math.sin(a) * dist} r={5 + rnd(i, 7) * 6} fill={['#00D2FF', '#9D4EDD', YELLOW, '#7CE4FF'][i % 4]} opacity={t} />;
  });
  return (
    <g>
      {rings}
      <circle cx={W / 2} cy={H / 2} r={r} fill={YELLOW} />
      {orbits}
    </g>
  );
}

function Assemble({ vert }) {
  const { progress } = useScene();
  return <MapDots vert={vert} mapProg={Easing.cubicInOut ? Easing.cubicInOut(progress) : progress} waveT={null} />;
}

function Pulse({ vert }) {
  const { progress } = useScene();
  const { W, H } = useLayout(vert);
  const waveT = -0.3 + progress * 1.7;
  const zoom = 1 + 0.04 * Math.sin(progress * Math.PI);
  return (
    <g>
      <MapDots vert={vert} mapProg={null} waveT={waveT} scale={zoom} />
      <rect x={0} y={0} width={W} height={H} fill="none" />
    </g>
  );
}

function Lockup({ vert, scene }) {
  const { progress } = useScene();
  const { W, H, mw, mh } = useLayout(vert);
  const p = progress;
  const shift = seg(p, 0, 0.35, Easing.cubicInOut || null);
  const mapScale = 1 - 0.28 * shift;
  const mapCy = vert ? H * 0.5 - (H * 0.17) * shift : H * 0.5 - (H * 0.14) * shift;
  const word = (scene && scene.word) || 'USHA';
  const sub = (scene && scene.sub) || 'UNITED STATES HYDROGEN ALLIANCE';
  const wordSize = vert ? 150 : 170;
  const wordY = vert ? H * 0.72 : H * 0.76;
  const letters = word.split('').map((ch, i) => {
    const t = seg(p, 0.3 + i * 0.06, 0.55 + i * 0.06, backOut);
    const dy = (1 - t) * 90;
    return (
      <text key={i} x={W / 2 + (i - (word.length - 1) / 2) * wordSize * 0.82} y={wordY + dy}
        fontFamily="Unbounded, sans-serif" fontWeight="800" fontSize={wordSize} fill={PAPER}
        textAnchor="middle" opacity={t}>{ch}</text>
    );
  });
  const subT = seg(p, 0.62, 0.85);
  const ruleT = seg(p, 0.5, 0.75, Easing.cubicInOut || null);
  return (
    <g>
      <MapDots vert={vert} mapProg={null} waveT={null} cy={mapCy} scale={mapScale} />
      <g>{letters}</g>
      <rect x={W / 2 - (mw * 0.32) * ruleT} y={wordY + (vert ? 52 : 56)} width={mw * 0.64 * ruleT} height={3} fill={YELLOW} />
      <text x={W / 2} y={wordY + (vert ? 108 : 116)} fontFamily="'Space Grotesk', sans-serif" fontWeight="600"
        fontSize={vert ? 30 : 32} letterSpacing={vert ? 8 : 10} fill="#00D2FF" textAnchor="middle" opacity={subT}>
        {sub}
      </text>
    </g>
  );
}

function SealGroup({ cx, cy, size, rot, pulse, idp }) {
  const D = window.USHA_DOTS.h;
  const INK = '#F8F9FA', ACC = '#FFB703';
  const hs = 150 / D.w, hx = 200 - (D.w * hs) / 2, hy = 200 - (D.h * hs) / 2;
  const RING = ['#5fe0ff', ACC, '#9d4edd', '#33dbff', '#a8eeff'];
  return (
    <g transform={`translate(${cx - size / 2},${cy - size / 2}) scale(${size / 400})`}>
      <defs>
        <path id={idp + 't'} d="M 200,362 a 162,162 0 1,1 0.01,0" fill="none" />
        <path id={idp + 'b'} d="M 200,52 a 148,148 0 1,0 0.01,0" fill="none" />
      </defs>
      <circle cx={200} cy={200} r={192} fill="none" stroke={INK} strokeWidth={3} />
      <circle cx={200} cy={200} r={130} fill="none" stroke={INK} strokeWidth={1.5} />
      <g transform={`rotate(${rot} 200 200)`}>
        {Array.from({ length: 60 }, (_, i) => { const a = i / 60 * Math.PI * 2; return <circle key={i} cx={200 + Math.cos(a) * 180} cy={200 + Math.sin(a) * 180} r={i % 5 === 0 ? 3.4 : 1.6} fill={i % 5 === 0 ? ACC : RING[i % RING.length]} />; })}
      </g>
      <text fontFamily="'Space Grotesk', sans-serif" fontWeight="700" fontSize="19.5" letterSpacing="5" fill={INK} textAnchor="middle">
        <textPath href={'#' + idp + 't'} startOffset="50%">UNITED STATES HYDROGEN ALLIANCE</textPath>
      </text>
      <text fontFamily="'Space Grotesk', sans-serif" fontWeight="700" fontSize="19.5" letterSpacing="6" fill={ACC} textAnchor="middle">
        <textPath href={'#' + idp + 'b'} startOffset="50%">• H₂ •</textPath>
      </text>
      <g transform={`translate(${hx},${hy}) scale(${hs})`}>
        {D.dots.map((d, i) => <circle key={i} cx={d.x} cy={d.y} r={d.r * (1 + 0.3 * (pulse || 0) * Math.sin(i * 0.7))} fill={bright(d.c)} />)}
      </g>
    </g>
  );
}

function Badge({ vert }) {
  const { progress } = useScene();
  const { W, H } = useLayout(vert);
  const p = progress;
  const sc = 0.2 + 0.8 * seg(p, 0, 0.4, backOut);
  const size = Math.min(W, H) * 0.62;
  return (
    <g opacity={seg(p, 0, 0.12)}>
      <g transform={`translate(${W / 2},${H / 2}) scale(${sc}) translate(${-W / 2},${-H / 2})`}>
        <SealGroup cx={W / 2} cy={H / 2} size={size} rot={p * 30} pulse={Math.sin(p * Math.PI)} idp="bdg" />
      </g>
    </g>
  );
}

function QRPlaceholder({ x, y, size }) {
  const n = 21, cell = size / n;
  const cells = [];
  const finder = (fx, fy) => fx < 7 && fy < 7 || fx > n - 8 && fy < 7 || fx < 7 && fy > n - 8;
  for (let gy = 0; gy < n; gy++) for (let gx = 0; gx < n; gx++) {
    if (finder(gx, gy)) continue;
    if (rnd(gx * 31 + gy, 9) > 0.52) cells.push(<rect key={gx + '-' + gy} x={x + gx * cell} y={y + gy * cell} width={cell * 0.92} height={cell * 0.92} fill="#0D1B2A" />);
  }
  const fnd = (fx, fy) => (
    <g key={fx + ',' + fy}>
      <rect x={x + fx * cell} y={y + fy * cell} width={cell * 7} height={cell * 7} fill="#0D1B2A" />
      <rect x={x + (fx + 1) * cell} y={y + (fy + 1) * cell} width={cell * 5} height={cell * 5} fill="#FFFFFF" />
      <rect x={x + (fx + 2) * cell} y={y + (fy + 2) * cell} width={cell * 3} height={cell * 3} fill="#0D1B2A" />
    </g>
  );
  return (
    <g>
      <rect x={x - 18} y={y - 18} width={size + 36} height={size + 36} rx={14} fill="#FFFFFF" />
      {cells}{fnd(0, 0)}{fnd(n - 7, 0)}{fnd(0, n - 7)}
    </g>
  );
}

function VideoSlot({ x, y, w, h, label, t }) {
  return (
    <g opacity={t} transform={`translate(${(1 - t) * 90},0)`}>
      <rect x={x} y={y} width={w} height={h} rx={16} fill="#16283C" stroke="#33dbff" strokeWidth={2} strokeOpacity={0.4} />
      <circle cx={x + w / 2} cy={y + h / 2} r={Math.min(w, h) * 0.14} fill="#FFB703" />
      <path d={`M ${x + w / 2 - Math.min(w, h) * 0.045} ${y + h / 2 - Math.min(w, h) * 0.07} l ${Math.min(w, h) * 0.12} ${Math.min(w, h) * 0.07} l ${-Math.min(w, h) * 0.12} ${Math.min(w, h) * 0.07} Z`} fill="#0D1B2A" />
      <text x={x} y={y - 16} fontFamily="'Space Grotesk', sans-serif" fontWeight="700" fontSize={26} letterSpacing={6} fill="#00D2FF">{label}</text>
    </g>
  );
}

function Outro({ vert }) {
  const { progress } = useScene();
  const { W, H } = useLayout(vert);
  const p = progress;
  const t1 = seg(p, 0.08, 0.35, backOut), t2 = seg(p, 0.2, 0.47, backOut);
  const qt = seg(p, 0.35, 0.6);
  const st = seg(p, 0, 0.25, backOut);
  if (!vert) {
    return (
      <g>
        <g opacity={st}><SealGroup cx={220} cy={210} size={280} rot={p * 25} pulse={Math.sin(p * Math.PI)} idp="out" /></g>
        <text x={110} y={430} fontFamily="Unbounded, sans-serif" fontWeight="800" fontSize={44} fill={PAPER} opacity={st}>WATCH NEXT</text>
        <VideoSlot x={640} y={170} w={600} h={338} label="MOST POPULAR" t={t1} />
        <VideoSlot x={640} y={600} w={600} h={338} label="UP NEXT" t={t2} />
        <g opacity={qt}>
          <QRPlaceholder x={1370} y={330} size={330} />
          <text x={1535} y={750} fontFamily="'Space Grotesk', sans-serif" fontWeight="700" fontSize={26} letterSpacing={8} fill="#FFB703" textAnchor="middle">SCAN FOR MORE</text>
        </g>
        <text x={110} y={950} fontFamily="'Space Grotesk', sans-serif" fontWeight="600" fontSize={28} letterSpacing={10} fill="#00D2FF" opacity={qt}>USHYDROGENALLIANCE</text>
      </g>
    );
  }
  return (
    <g>
      <g opacity={st}><SealGroup cx={W / 2} cy={250} size={340} rot={p * 25} pulse={Math.sin(p * Math.PI)} idp="out" /></g>
      <VideoSlot x={110} y={520} w={860} h={484} label="MOST POPULAR" t={t1} />
      <VideoSlot x={110} y={1120} w={860} h={484} label="UP NEXT" t={t2} />
      <g opacity={qt}>
        <QRPlaceholder x={W / 2 - 130} y={1655} size={260} />
        <text x={W / 2} y={1625} fontFamily="'Space Grotesk', sans-serif" fontWeight="700" fontSize={26} letterSpacing={8} fill="#FFB703" textAnchor="middle">SCAN FOR MORE</text>
      </g>
    </g>
  );
}

function SceneSvg(Inner) {
  return function Wrapped(props) {
    const vert = props.vert;
    const W = vert ? 1080 : 1920, H = vert ? 1920 : 1080;
    return (
      <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{ position: 'absolute', inset: 0 }}>
        <Inner {...props} />
      </svg>
    );
  };
}

window.UshaIntro = function UshaIntro() {
  const [t, setTweak] = useTweaks(window.TWEAK_DEFAULTS);
  const vert = t.format === '9:16';
  const W = vert ? 1080 : 1920, H = vert ? 1920 : 1080;
  const wrap = Inner => {
    const C = SceneSvg(Inner);
    return props => <C {...props} vert={vert} />;
  };
  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#101318' }}>
      <SceneStage key={t.format} width={W} height={H} bg={NAVY} scenes={window.OM_SCENES} playback={window.OM_PLAYBACK}>
        {{ Badge: wrap(Badge), Spark: wrap(Spark), Assemble: wrap(Assemble), Pulse: wrap(Pulse), Lockup: wrap(Lockup), Outro: wrap(Outro) }}
      </SceneStage>
      <TweaksPanel>
        <TweakSection label="Format" />
        <TweakRadio label="Aspect" value={t.format} options={['16:9', '9:16']} onChange={v => setTweak('format', v)} />
        <TweakSection label="Editor" />
        <TweakToggle label="Motion editor" value={t.motionEditor} onChange={v => setTweak('motionEditor', v)} />
      </TweaksPanel>
    </div>
  );
};
