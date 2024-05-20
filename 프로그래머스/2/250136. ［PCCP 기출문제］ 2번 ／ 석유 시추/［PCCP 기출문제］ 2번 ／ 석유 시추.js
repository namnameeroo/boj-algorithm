function solution(land) {
    var answer = 0;
    let landQ = new Array(land[0].length).fill(0);
    let visited = new Array(land.length).fill(0).map(v=> new Array(land[0].length).fill(false));
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[0].length; j++) {
            if (land[i][j] !== 1) continue;
            if (visited[i][j]) continue;
            visited[i][j] = true;
            getOils(i, j);
        }
    }
    
    function getOils(x, y) {
        let [minY,maxY] = [y, y];
        let stack = [];
        stack.push([x,y]);
        
        let quantity = 0;
        while (stack.length >= 1) {
            let [r, c] = stack.pop();
            minY = Math.min(minY, c);
            maxY = Math.max(maxY, c);
            quantity++;
            for (let [dx, dy] of [[0,1],[1,0],[-1,0],[0,-1]]) {
                let nr = dx + r;
                let nc = dy + c;
                if (!check(nr, nc) ||
                    visited[nr][nc] ||
                    land[nr][nc] !== 1 ) continue;
                stack.push([nr, nc]);
                visited[nr][nc] = true;
            }
        }
        
        for (let i = minY; i <= maxY; i++) {
            landQ[i] += quantity;
        }
    }
    function check(x,y) {
        if (x < 0 || x >= land.length) return false;
        if (y < 0 || y >= land[0].length) return false;
        return true;
    }
    
    
    return Math.max(...landQ);
}