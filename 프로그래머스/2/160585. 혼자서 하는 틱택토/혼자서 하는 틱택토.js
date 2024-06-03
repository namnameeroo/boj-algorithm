function solution(board) {
    // 선공 O, 후공 X
    // O_cnt+1 == X_cnt or O_cnt == X_cnt
    // Oline > Xline or Oline < Xline 
    let os = 0;
    let xs = 0;
    
    for (let b of board) {
        os += (b.match(/O/g) ?? []).length;
        xs += (b.match(/X/g) ?? []).length;
    }
    
    if (os < xs || os - xs > 1) return 0
    
    let O_cnt = checkLines("O");
    let X_cnt = checkLines("X");
    
    
    
    function checkLines (symbol) {
        let lines = 0;
        const complete = symbol.repeat(3);
        for (let i of [0,1,2]) {
            if (board[i]===complete) {
                lines++;
            }
        }
        // if (lines > 1) return 
        for (let j of [0,1,2]) {
            let col = '';
            for (let i of [0,1,2]) {
                if (board[i][j] !== symbol) break;
                col += board[i][j];
            }
            
            if (col === complete) {
                lines++;
            }
        }

        let l_cross = '';
        let r_cross = '';
        
        for (let x of [0,1,2]) {
            l_cross += board[x][x];
            r_cross += board[x][2-x];
        }
        if (l_cross === complete) lines++;
        if (r_cross === complete) lines++;
        return lines;   
    }
    
    if (O_cnt > 0 && X_cnt > 0) return 0;
    if (O_cnt > 0 && os===xs) return 0
    if (X_cnt > 0 && os>xs) return 0
    return 1;
}