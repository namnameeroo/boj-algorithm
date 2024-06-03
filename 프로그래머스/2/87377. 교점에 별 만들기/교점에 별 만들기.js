function solution(line) {
    var answer = [];
    let minX = Number.POSITIVE_INFINITY
    let maxX = Number.NEGATIVE_INFINITY
    let minY = Number.POSITIVE_INFINITY
    let maxY = Number.NEGATIVE_INFINITY
    
    for (let i = 0; i < line.length-1; i++){
        for (let j = i+1; j < line.length; j++) {
            let [a,b,e] = line[i];
            let [c,d,f] = line[j];

            if (a*d == b*c) continue;
            const x = (b*f - e*d)/(a*d - b*c)
            const y = (e*c - a*f)/(a*d - b*c)
            if (x%1 !== 0 || y%1 !== 0) continue;
            minX = Math.min(minX, x)
            maxX = Math.max(maxX, x)
            minY = Math.min(minY, y)
            maxY = Math.max(maxY, y)
            answer.push([x, y]);
        }
    }
    
    
    let result = [];
    let Xsize = maxX-minX+1;
    let Ysize = maxY-minY+1;
    for (let j = 0; j < Ysize; j++) {
        let row = new Array(Xsize).fill('.')
        result.push(row);
    }
    
    for (let [cX, cY] of answer) {
        result[cY-minY][cX-minX] = '*';
    }
    
    return result.map(v=> v.join('')).reverse();
}