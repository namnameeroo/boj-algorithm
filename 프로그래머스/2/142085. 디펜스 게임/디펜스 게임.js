function solution(n, k, enemy) {
    
    let sp = 0;
    let ep = enemy.length;
    let answer = 0;
    
    let tot = 0;
    let enemy_acc = enemy.map(v=>{
        tot += v;
        return tot
    })
    
    
    while (sp < ep) {
        let mid = parseInt((sp+ep)/2);
        let res = goRound(mid, k);
        if (res > 0) {
            ep = mid;
        } else {
            answer = Math.max(answer, mid);
            sp = mid+1;
        }   
    }
    
    function goRound(round_idx, k) {
        let enemies = enemy_acc[round_idx];
        let elst = enemy.slice(0, round_idx+1);
        elst.sort((a,b)=>-b+a);
        while (k > 0) {
            enemies -= elst.pop();
            if (elst.length <= 0) break;
            k--;
        }
        return enemies - n;
    }
        
    return answer+1;
}