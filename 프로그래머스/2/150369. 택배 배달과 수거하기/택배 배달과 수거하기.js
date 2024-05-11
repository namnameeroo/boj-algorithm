function solution(cap, n, deliveries, pickups) {
    let d_list = [];
    let p_list = [];
    
    for (let [idx, d] of deliveries.entries()) {
        for (let cnt = 0; cnt < d; cnt++) {
            d_list.push(idx+1);
        }
    }
    for (let [idx, p] of pickups.entries()) {
        for (let cnt = 0; cnt < p; cnt++) {
            p_list.push(idx+1);
        }
    }
    // console.log(d_list);
    // console.log(p_list);
    let distance = 0;
    while (true) {
        let max_dis = 0;
        for (let i = 0; i < cap; i++) {
            let x = d_list.pop() || 0;
            let y = p_list.pop() || 0;
            max_dis = Math.max(max_dis, x, y);
        }
        
        distance += max_dis*2;
        // console.log({max_dis, d_list, p_list})
        if (max_dis == 0) break;
    }
    
    return distance;
    
}