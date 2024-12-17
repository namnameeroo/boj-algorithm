function solution(arr1, arr2) {
    var answer = [[]];
    // x,y a,b
    let [xl, yl] = [arr1.length, arr1[0].length];
    let [al, bl] = [arr2.length, arr2[0].length];
    let board = new Array(xl).fill(0).map(v => new Array(bl).fill(0))
    for (let r = 0; r < xl; r++) {
        for (let c = 0; c < bl; c++) {
            for (let mid = 0; mid < yl; mid++) {
                board[r][c] += arr1[r][mid] * arr2[mid][c];
            }
        }
    }
    
    return board;
}