const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  console.log(Recursion(line));
  rl.close();
}).on("close", () => {
  process.exit();
});

const Recursion = (num) => {
  if (num == 0 || num == 1) return num;
  return Recursion(num - 1) + Recursion(num - 2);
};
