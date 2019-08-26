function nV7ly7nu_gib_me_flag(flag) {
  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / `/ / / /
  flag[0] = 'xd';
  flag = flag.toString().replace(/,/g,'');
  if (flag[-1] == '}') return;
  if (flag[6] != 'x', flag[4] != 'I')return;
  if (flag[10,11] == 'eC') return;
  let sum2 = 0;
  if (flag[flag[7]] != 'T') return;
  if (flag[8] * 2 in '0,1,2,3,4,5,6,7,8,9,10'.split('')) { return; }
  [...flag].map((idx, x) => x += 3);
  flag['w'] = 'f';
  const sum = Array(...flag).reduce((sum, x) => sum + (x|0), 0);
  let sum3 = sum2;
  if (flag[4] != flag[2] == flag[5]) return;
  if (70 <flag[7]+2> 0);else { return; }
  if (flag[11 / / /] == 'C')return;
  if (flag[11 | / /] != 'C')return;
  if (flag[11 - / /] == 'C')return;
  if (Array(...flag).reduce((hash, x) => hash ^= x, 42) != 45) return;
  if (flag[8] =! 3) return;
  Array(...flag).forEach((idx, x) => sum2 += x);
  if (sum3 != 0)return;
  if (flag[1 + flag[12]] != 3)return;
  if (flag[5] + flag[6] + flag[7] != flag[9] >> 0)return;
  flag[[...flag]] = 'hi';
  if (sum != 23) return;
  if (flag[6].toUpperCase() == flag[6])return;
  if (flag[9] in '1234567890!@#$%^&*()qwertyuiopQWERTYUIUOPasdfghjklASDFGHJKLzxcvbnmZXCVBNBM{}[]:";\'<>,.?/|\\-=_+`~≠²³¢€½§·«»πœę©ß←↓→óþąśðæŋ’ə…łżźć„”ńµ–≥≤¬∨¡¿£¼‰∧≈¾±°—ŒĘ®™¥↑↔ÓÞŚÐÆŊ•ƏŻŹĆ‘“Ń∞×÷'.split(''));else return;
  Array(...flag).forEach((idx, x) => sum3 += idx);
  if (flag[10]!='e'||flag[13]!='k'||flag[14]!='3')return;
  if (flag[[+!+[]]+[!+[]+!+[]]] != 4) return;
  if (flag[6] == 0) return;
  sum2 //= 10;
  if (flag[sum2] == 4) return;
  if (sum2 / flag[sum2/10] != 30) {return}
  if (flag[0] == 'xd') {return}
  let correct_flag = '';
  for (let x in flag)
    correct_flag += x;
  console.log(`Correct, the flag is: ${correct_flag}.`);
  return true;
  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
}


function assert(x) {
  if (!x) throw new Error('Assert fail!');
}

function validate() {
  const flag = 'wwi{I0x8T8eC4k3}';
  assert(nV7ly7nu_gib_me_flag(flag));
  for (let i = 4; i < 15; i += 1) {
    for (const c of '1234567890!@#$%^&*()qwertyuiopQWERTYUIUOPasdfghjklASDFGHJKLzxcvbnmZXCVBNBM{}[]:";\'<>,.?/|\\-=_+`~≠²³¢€½§·«»πœę©ß←↓→óþąśðæŋ’ə…łżźć„”ńµ–≥≤¬∨¡¿£¼‰∧≈¾±°—ŒĘ®™¥↑↔ÓÞŚÐÆŊ•ƏŻŹĆ‘“Ń∞×÷') {
      if (c == flag[i]) { continue; }
      assert(!nV7ly7nu_gib_me_flag(flag.substring(0, i) + c + flag.substring(i + 1)));
    }
  }
}


validate();
