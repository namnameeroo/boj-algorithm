const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const ABB = "ABB";
let [N, ...cases] = input;

for (let i = 0; i < N * 2; i += 2) {
    let long = cases[i];
    let letters = cases[i + 1];
    let result = outer(long, letters);
    console.log(result);
}

function outer(long, letters) {
  let target = letters; // string
  let local_long = long;
  while (true) {
    target = getResult(local_long, target);
    local_long = target.length;
    if (!target.includes(ABB) || local_long < 3) {
      break;
    }
  }
  return target;
}

function getResult(long, letters) {
  let stack = [];
  for (let i = 0; i < long; i++) {
    stack.push(letters[i]);
    if (stack.length >= 3 && stack.slice(-3).join("") === ABB) {
      stack.pop();
      stack.pop();
      stack.pop();
      stack.push("B");
      stack.push("A");
    }
  }

  return stack.join("");
}


