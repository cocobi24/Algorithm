// 실행: ctr + alt + n
const fs = require('fs');
const input = fs.readFileSync('./input.in').toString().trim().split("\n");
const T = Number(input[0]); // 테스트 케이스의 수

// 공 나누기가 가능한지 구하는 함수
function isDivide(N, K) {
  if (N !== 1 && N <= K) {
    return "NO";
  }

  const boxes = new Array(K).fill(0);
  for (let i = 0; i < K; i++) {
    if (i === K - 1) {
      boxes[i] = N;
      N -= N;
    } else {
      boxes[i] = i + 1;
      N -= i + 1;
    }
  }

  for (let i = K - 1; i >= 0; i--) {
    const ballsToAssign = Math.floor(N / (i + 1));
    if (ballsToAssign >= boxes[i]) {
      return "NO";
    }
    boxes[i] += ballsToAssign;
    N -= ballsToAssign;
  }

  return "YES";
}

for (let i = 1; i < T+1; i++) {
  const [N, K] = input[i].trim().split(" ").map(Number);
  const result = isDivide(N, K);
  console.log(result);
}