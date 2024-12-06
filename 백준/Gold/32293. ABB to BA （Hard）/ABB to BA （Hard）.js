const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const ABB = "ABB";
let [N, ...cases] = input;

for (let i = 0; i < N * 2; i += 2) {
    let letters = cases[i + 1];
    let result = getResult(letters);
    console.log(result);
}


function getResult(letters) {
  let target = letters;
  while (target && target.includes("ABB")) {
    target = changeABB(target);
  }
  return target;
}

function changeABB(target) {
  let long = target.length;
  let stack = [];
  for (let i = 0; i < long; i++) {
    stack.push(target[i]);
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


