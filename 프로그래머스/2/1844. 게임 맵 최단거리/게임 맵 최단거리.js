class Queue {
    constructor() {
        this.front = 0;
        this.rear = 0;
        this.items = [];
    }
    
    pop() {
        const result = this.items[this.front];
        this.front++;
        return result;
    }
    
    push(e) {
        this.items.push(e);
        this.rear++;
    }
    
    isEmpty() {
        return this.front === this.rear;
    }
}

function solution(maps) {
    
    
    
    const rs = maps.length;
    const cs = maps[0].length;
    if (maps[0][0] === 0) return -1;
    if (maps[rs-1][cs-1] === 0) return -1;
    
    const visited = new Array(rs).fill(0).map(v=>new Array(cs).fill(false));
    
    

    
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    visited[0][0] = true;
    const q = new Queue();
    q.push([0,0,1]);
    
    while (q && !q.isEmpty()) {
        const [r, c, dist] = q.pop();
        if (r === rs-1 && c === cs-1) {
            return dist;
        }
        
        for (let i = 0; i < 4; i++) {
            let next_r = r + dx[i];
            let next_c = c + dy[i];
            
            if (!isInRange(next_r, next_c)) continue;
            if (maps[next_r][next_c] === 0) continue;
            if (visited[next_r][next_c]) continue;
            visited[next_r][next_c] = true;
            q.push([next_r, next_c, dist+1]);
        }
        
    }
    
    
    
    function isInRange(a, b) {
        if (a < 0 || a >= rs || b < 0 || b >= cs) {
            return false;
        }
        return true;
    }
    
    return -1;
}