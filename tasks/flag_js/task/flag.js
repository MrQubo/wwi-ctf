function nV7ly7nu_gib_me_flag(flag) {
  flag[0] = 'xd';
  if (flag[-1] == '}') return;
  if (flag[10,11] == 'eC') return;
  let sum2 = 0;
  if (flag[flag[7]] != 'T') return;
  if (flag[8] * 2 in '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18'.split(',')) return;
  Array(...flag).map(x => x += 3);
  flag['w'] = 'f';
  const sum = Array(...flag).reduce((sum, x) => sum + (x|0), 0);
  let sum3 = sum2;
  if (flag[4] != flag[2] != flag[0]) return;
  if (80 > flag[7] + 2 > 0) return;
  if (flag[11] != 'C') return;
  Array(...flag).forEach((idx, x) => sum2 += x);
  if (sum3 != 0) return;
  if (flag[1 + flag[12]] != 3) return;
  if (sum != 15) return;
  if (flag[9] in '1234567890!@#$%^&*()qwertyuiopQWERTYUIUOPasdfghjklASDFGHJKLzxcvbnmZXCVBNBM{}[]:";\'<>,.?/|\\-=_+`~'.split('')) { return; }
  Array(...flag).forEach((idx, x) => sum3 += idx);
  if (sum2 / sum != 8) { return; }
  let correct_flag = '';
  for (let x in flag)
    correct_flag += x;
  console.log(`Correct, the flag is: ${correct_flag}.`);
}
