function solution(picks, minerals) {
    if (minerals.length == 0) return 0
    let tool_cnt = picks.reduce((acc,v)=>acc+v,0);
    if (tool_cnt * 5 < minerals.length) {
        minerals = minerals.slice(0,tool_cnt*5+1);
    }
    let score = {'diamond' : 25, 'iron' : 5, 'stone' : 1}
    let need = [];
    for (let i = 0; i < minerals.length; i += 5) {
        let part = minerals.slice(i, i+5);
        need.push([i, part.reduce((acc, v) => acc + score[v],0)]);
    }
    need.sort((a,b)=> +b[1] - a[1]);
    let needHP = 0;
    for (let [idx, ] of need) {
        if (picks[0] > 0) {
            picks[0]--;
            getMinerals(idx, 'diamond');
        } else if (picks[1] > 0) {
            picks[1]--;
            getMinerals(idx, 'iron');
        } else if (picks[2] > 0) {
            picks[2]--;
            getMinerals(idx, 'stone');
        } 
    }
    
    function getMinerals(startIdx, tool) {
        for (let m of minerals.slice(startIdx, startIdx+5)) {
            let cal = score[m] / score[tool];
            if (cal <= 1) {
                needHP++;
            } else {
                needHP += cal;
            }
        }
        
    }
    return needHP;
}