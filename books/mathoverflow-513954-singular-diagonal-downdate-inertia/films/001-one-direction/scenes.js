/* 同一数学故事：秩一分块、连通族与分散尾部。所有画面只依赖当前场景时间。 */
'use strict';
function sceneAlpha(S) { return clamp(S.u / 0.6) * clamp((S.d - S.u) / 0.5); }
function sceneTitle(S, en, zh) {
  const a = sceneAlpha(S);
  txt(en, W / 2, 210, {size: 43, fam: F.disp, w: 700, align: 'center', c: C.white, a});
  txt(zh, W / 2, 265, {size: 33, fam: F.zh, align: 'center', c: C.cyan, a});
}
function formula(s, x, y, a, size = 46, c = C.white) { txt(s, x, y, {size, fam: F.math, align: 'center', c, a}); }
function diagEntries(x, y, vals, a, focus = -1) {
  vals.forEach((v, i) => {
    const c = i === focus ? C.now : C.cyan;
    chip(x + i * 165, y, 135, 105, String(v), c, a, 48, F.math);
  });
}
SCENES.example = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'computed']]);
  sceneTitle(S, 'ONE NEW ZERO DIRECTION', '原有零方向，加一个新零方向');
  panel(260, 340, 1400, 365, a, C.cyan, 'A SINGULAR EXAMPLE');
  diagEntries(550, 445, ['−2', '0', '3'], a, 0);
  txt('A', 340, 460, {size: 42, fam: F.math, c: C.white, a});
  arrow(1110, 445, 1410, 445, C.now, at(S, 2, 1) * a, 4);
  formula('Δ = −2', 1250, 525, a, 40);
  diagEntries(550, 610, ['0', '0', '3'], at(S, 2, 1) * a, 0);
  txt('M', 340, 625, {size: 42, fam: F.math, c: C.white, a: at(S, 2, 1) * a});
};
SCENES.blocks = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'lean']]);
  sceneTitle(S, 'ISOLATE A SCALAR BLOCK', '把一个非零标量块置零');
  panel(210, 340, 630, 330, a, C.cyan, 'BEFORE');
  panel(1080, 340, 630, 330, a, C.cyan, 'AFTER');
  box(270, 400, 300, 200, C.cyan, a); formula('C', 420, 520, a, 76);
  box(620, 500, 150, 100, C.now, a); formula('Δ', 695, 565, a, 64, C.now);
  box(1140, 400, 300, 200, C.cyan, a); formula('C', 1290, 520, a, 76);
  box(1490, 500, 150, 100, C.cyan, a); formula('0', 1565, 565, a, 64);
  arrow(870, 505, 1050, 505, C.now, at(S, 2, 1) * a, 4);
  formula('Δ > 0: one positive removed     Δ < 0: one negative removed', W / 2, 760, at(S, 3, 1) * a, 34);
};
SCENES.kernel = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'lean'], [2, null, 'argued']]);
  sceneTitle(S, 'THE OLD KERNEL AND ONE NEW LINE', '旧核与一条新直线');
  panel(250, 340, 1420, 380, a, C.cyan, 'DIRECT SUM');
  formula('ker M = ker A ⊕ span{x}', W / 2, 455, a, 64);
  formula('Mv = 0   ⇒   A(v − tx) = 0', W / 2, 565, at(S, 1, 0.8) * a, 49);
  formula('nullity + 1     rank − 1', W / 2, 660, at(S, 2, 0.8) * a, 46, C.argued);
};
SCENES.family = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'argued']]);
  sceneTitle(S, 'A NEGATIVE COORDINATE CANNOT HAND OVER', '连通性锁定同一个负坐标');
  panel(230, 340, 1460, 390, a, C.argued, 'CONNECTED DOMAIN');
  line(340, 515, 1580, 515, C.cyan, a, 6);
  for (let i = 0; i < 7; i++) {
    const px = 380 + i * 190; dot(px, 515, 16, 'c', a);
    txt('j', px, 470, {size: 38, fam: F.math, c: C.now, align: 'center', a});
  }
  formula('Uj = {y : dj(y) < 0}', W / 2, 615, at(S, 2, 0.8) * a, 43);
  formula('disjoint + open + closed + cover  ⇒  one whole region', W / 2, 685, at(S, 2, 0.8) * a, 34, C.argued);
};
SCENES.sphere = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'argued'], [3, null, 'computed']]);
  sceneTitle(S, 'THREE COORDINATES BEAT TWO', '三个坐标打败所有二坐标向量');
  formula('h(t) = (3t − t³) / 2', W / 2, 350, at(S, 1, 0.8) * a, 50);
  panel(230, 405, 650, 300, a, C.cyan, 'AT MOST TWO');
  panel(1040, 405, 650, 300, a, C.cyan, 'THREE COORDINATES');
  formula('min R² = 80 / 81', 555, 525, at(S, 2, 0.8) * a, 48);
  formula('p = (4/5, 1/10, 1/10)', 1365, 500, at(S, 3, 0.8) * a, 38);
  formula('R² = 13689 / 13885', 1365, 585, at(S, 3, 0.8) * a, 43);
  formula('13689 / 13885 < 80 / 81', W / 2, 770, at(S, 3, 0.8) * a, 44, C.now);
};
SCENES.tail = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'argued']]);
  sceneTitle(S, 'THE TAIL APPROACHES THE INFIMUM', '越来越分散的尾部逼近下确界');
  formula('R² ≥ (3 − a²)² / (9 − 6a² + a³)', W / 2, 350, a, 46);
  const ast = 6 - 3 * Math.sqrt(3);
  const m = Math.min(24, 2 + Math.floor(at(S, 2, Math.max(2, S.d * 0.45)) * 22));
  const bx = 300, by = 650, width = 1300;
  line(bx, by, bx + width, by, C.dim, a, 2);
  fillBox(bx, by - ast * 280, 115, ast * 280, C.now, a);
  const tailW = Math.min(80, 1000 / m - 5), step = 1100 / m;
  for (let i = 0; i < m; i++) fillBox(bx + 180 + i * step, by - (1 - ast) / m * 700, tailW, (1 - ast) / m * 700, C.cyan, a);
  formula('a*', bx + 57, 705, a, 36, C.now);
  formula('m = ' + m + '     each tail mass = (1 − a*) / m', 1130, 710, a, 34);
  formula('inf R² = 16(17 − 9√3) / 23   —   not attained finitely', W / 2, 800, at(S, 3, 0.8) * a, 34, C.argued);
};
SCENES.close = S => {
  const a = sceneAlpha(S); badgeQ(S, [[0, null, 'argued']]);
  sceneTitle(S, 'ONE BLOCK. ONE FIXED INDEX. A DIFFUSE TAIL.', '一个块，一个固定指标，一段分散尾部');
  panel(260, 340, 1400, 440, a, C.cyan, 'MATHEMATICS AND SOURCES');
  txt('Lucid: questions and hyperplane mechanism', W / 2, 415, {size: 34, fam: F.disp, align: 'center', c: C.white, a});
  txt('user1551: earlier inertia proof', W / 2, 470, {size: 34, fam: F.disp, align: 'center', c: C.white, a});
  txt('Haobo Ma · Chrono AI, Singapore', W / 2, 555, {size: 31, fam: F.disp, align: 'center', c: C.cyan, a: at(S, 1, 0.8) * a});
  txt('Wenlin Zhang · NUS and Chrono AI, Singapore', W / 2, 605, {size: 31, fam: F.disp, align: 'center', c: C.cyan, a: at(S, 1, 0.8) * a});
  txt('Version 2 · DOI 10.5281/zenodo.23920598', W / 2, 690, {size: 30, fam: F.mono, align: 'center', c: C.white, a});
  txt('Exact matrix declarations + complete written proofs in the book', W / 2, 745, {size: 29, fam: F.disp, align: 'center', c: C.argued, a: at(S, 2, 0.8) * a});
};
FILM.poster = () => {
  txt('ONE DIRECTION, A DIFFUSE TAIL', W / 2, 260, {size: 63, fam: F.disp, w: 700, align: 'center', c: C.white});
  txt('一个方向与分散的尾部', W / 2, 340, {size: 46, fam: F.zh, align: 'center', c: C.cyan});
  panel(260, 410, 1400, 300, 1, C.cyan, 'THE MATHEMATICAL MECHANISM');
  formula('diag(C, Δ)  →  diag(C, 0)', W / 2, 520, 1, 65);
  formula('one large coordinate + a diffuse tail', W / 2, 630, 1, 43, C.argued);
  txt('Haobo Ma · Wenlin Zhang', W / 2, 805, {size: 38, fam: F.disp, align: 'center', c: C.white});
};
