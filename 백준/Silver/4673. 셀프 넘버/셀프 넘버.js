// let self = [];
let generator = [];
for (let i = 1; i < 10001; i++) {
    if (!generator.includes(i)) {
        // self.push(i);
        console.log(i);
    }
    generator.push(sum(i));
}

function sum(num) {
    let tot = 0;
    for (let l of String(num)) {
        tot += parseInt(l);
    }
    return tot + parseInt(num);
}
