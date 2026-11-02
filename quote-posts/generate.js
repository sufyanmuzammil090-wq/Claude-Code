// Renders tweet-style quote posts (1080x1350, Instagram 4:5) in two themes.
// Usage: node quote-posts/generate.js
// Optional: drop a square photo at quote-posts/avatar.jpg to replace the initials avatar.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const NAME = 'Dr. Azka Muzammil';
const HANDLE = '@dr.azkamuzammil';
const OUT = path.join(__dirname, '2026-11-02');

const POSTS = [
  ['Your body is not overreacting.', 'It’s reporting.'],
  ['Psychosomatic doesn’t mean it’s all in your head.', 'It means your head and your body are talking to each other.'],
  ['Motivation gets you started.', 'A regulated nervous system is what keeps you going.'],
  ['You don’t have a focus problem.', 'You have a nervous system that hasn’t felt safe in months.'],
  ['Looking successful and feeling calm', 'are two completely different skills.'],
  ['Burnout rarely arrives as a crash.', 'It arrives as “I’m fine, just busy.”'],
  ['Real confidence isn’t a loud voice.', 'It’s a calm body in a difficult room.'],
  ['Perfectionism isn’t high standards.', 'It’s a safety strategy that got too good at its job.'],
  ['Rest isn’t the reward for finishing.', 'It’s what lets you finish well.'],
  ['Understanding yourself', 'is the foundation of improving yourself.'],
];

const THEMES = {
  purple: { bg: '#FFFFFF', light: '#6B3FA0', bold: '#4A1D7A', name: '#1A1023', handle: '#8A7A9A', avatar: 'linear-gradient(135deg,#7B4BC4,#4A1D7A)' },
  black:  { bg: '#FFFFFF', light: '#3A3A3A', bold: '#000000', name: '#000000', handle: '#6E6E6E', avatar: 'linear-gradient(135deg,#2B2B2B,#000000)' },
};

// Instagram-style scalloped verified badge
function badge(size) {
  const pts = [], n = 16, R = 50, r = 44;
  for (let i = 0; i < n * 2; i++) {
    const a = (Math.PI * i) / n - Math.PI / 2, rad = i % 2 ? r : R;
    pts.push(`${(50 + rad * Math.cos(a)).toFixed(2)},${(50 + rad * Math.sin(a)).toFixed(2)}`);
  }
  return `<svg width="${size}" height="${size}" viewBox="0 0 100 100">
    <polygon points="${pts.join(' ')}" fill="#0095F6" stroke="#0095F6" stroke-width="6" stroke-linejoin="round"/>
    <path d="M30 51 L44 64 L70 37" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>`;
}

const avatarPath = path.join(__dirname, 'avatar.jpg');
const avatarImg = fs.existsSync(avatarPath)
  ? `data:image/jpeg;base64,${fs.readFileSync(avatarPath).toString('base64')}` : null;

function html([light, bold], t) {
  const len = light.length + bold.length;
  const fs1 = len > 95 ? 58 : len > 70 ? 64 : 72;
  const avatar = avatarImg
    ? `<img src="${avatarImg}" style="width:100%;height:100%;object-fit:cover">`
    : `<span>AM</span>`;
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1080px;height:1350px;background:${t.bg};font-family:'Inter',sans-serif;
    display:flex;flex-direction:column;justify-content:center;padding:0 110px}
  .head{display:flex;align-items:center;gap:30px;margin-bottom:70px}
  .av{width:150px;height:150px;border-radius:50%;background:${t.avatar};overflow:hidden;
    display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:54px;letter-spacing:2px}
  .name{display:flex;align-items:center;gap:12px;font-size:50px;font-weight:700;color:${t.name};letter-spacing:-0.5px}
  .handle{font-size:40px;color:${t.handle};margin-top:6px}
  .light{font-size:${fs1}px;font-weight:400;color:${t.light};line-height:1.25;margin-bottom:${fs1 * 0.9}px;letter-spacing:-0.5px}
  .bold{font-size:${fs1}px;font-weight:700;color:${t.bold};line-height:1.22;letter-spacing:-0.8px}
  </style></head><body>
  <div class="head"><div class="av">${avatar}</div>
    <div><div class="name">${NAME} ${badge(46)}</div><div class="handle">${HANDLE}</div></div></div>
  <div class="light">${light}</div><div class="bold">${bold}</div>
  </body></html>`;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const [key, theme] of Object.entries(THEMES)) {
    for (let i = 0; i < POSTS.length; i++) {
      await page.setContent(html(POSTS[i], theme));
      await page.evaluate(() => document.fonts.ready);
      const file = path.join(OUT, `post-${String(i + 1).padStart(2, '0')}-${key}.png`);
      await page.screenshot({ path: file });
    }
  }
  await browser.close();
  console.log('done:', OUT);
})();
