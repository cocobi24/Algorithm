const gcd = (a, b) => {
  return b === 0 ? a : gcd(b, a % b)
}
  
/**
 * @param {string} expression
 * @return {string}
 */
const fractionAddition = function(expression) {
  let n = expression.length;
  let num = 0, den = 1;
  let i = 0;
  while (i < n) {
    let isNegative = false;
    let curnum = 0;
    let curden = 0;

    if (expression[i] === '-' || expression[i] === '+') {
      if (expression[i] === '-') {
        isNegative = true;
      }
      i++;
    }

    while (i < n && expression[i] >= '0' && expression[i] <= '9') {
      let number = parseInt(expression[i]);
      curnum = curnum * 10 + number;
      i++;
    }

    if (isNegative) {
      curnum *= -1;
    }

    i++;
    while (i < n && expression[i] >= '0' && expression[i] <= '9') {
      let number = parseInt(expression[i]);
      curden = curden * 10 + number;
      i++;
    }

    num = num * curden + curnum * den;
    den = den * curden;
  }

  let g = gcd(Math.abs(num), den);
  num = Math.floor(num / g);
  den = Math.floor(den / g);
  return num + "/" + den;
};