function solution(board, moves) {
    var answer = 0;
    let bucket = [];
    
    
    // [[0,0,0,0,0],
    //  [0,0,1,0,3],
    //  [0,2,5,0,1],
    //  [4,2,4,4,2],
    //  [3,5,1,3,1]]
    
    // move
    for (let action of moves) {
        grabIt(board, action-1);
        if (hasSame(bucket)) {
            bubblePop(bucket);
        }
    }
    
    // grab
    // bucket 검사
    // bubble pop, cnt++;
    
    // return cnt
    
    
    
    function hasSame() {
        return bucket.length > 1 && bucket.at(-1) === bucket.at(-2);
    }
    
    function bubblePop() {
        if (!bucket || bucket.length < 2 ) return;
        bucket.pop();
        bucket.pop();
        answer+=2;
    }
    
    function grabIt(board, position) {
        for (let i = 0; i < board[0].length; i++) {
            if (board[i][position] !== 0) {
                let item = board[i][position];
                board[i][position] = 0;
                bucket.push(item);
                break;
            }
        }
        return [...bucket];
    }
    
    return answer;
}