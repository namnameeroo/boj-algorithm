function solution(n, computers) {
      
    let id = 1;
    const visited = new Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        
        dfs(i, id) && id++;
        // console.log(visited)
        
//         for (let j = i; j < n; j++) {
//             if (i == j) continue;
//             if (visited)
//             dfs(i,j,id);
            
//         }
    }
    
    function dfs(pc, id) {
        
        if (visited[pc] !== 0) return false;
        visited[pc] = id;
        for (let counter = 0; counter < n; counter++) {
            if (counter === pc) continue;
            if (visited[counter] !== 0) continue;
            if (computers[pc][counter] === 0) continue;
            // visited[counter] = id;
            dfs(counter, id);
        }
        return true;
    }
    
    return id-1
}