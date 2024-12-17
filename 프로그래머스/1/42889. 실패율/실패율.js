function solution(N, stages) {
    var answer = [];
    // answer[stage] = [stage, 실패율]
    // answer.sort((a,b)=>a[1]-b[1] || a[0]-b[0] ).map(v=>v[1]+1)
    let users = stages.length;
    let pass_challengers = new Array(N+2).fill(0);
    let stage_board = new Array(N+2).fill(0); // stage_board[stage] = user in stage

    
    // 스테이지에 도달한 플레이어 수 배열 생성
    for (let [user, current_stage] of stages.entries()) {
         for (let i = 0; i <= current_stage; i++) {
             // 통과한 모든 스테이지에 +1
             pass_challengers[i]++;
         }
         stage_board[current_stage] += 1;
    }
    
    for (let stage = 1; stage <= N; stage++) {
        let fail_percent = (() => {
            if ( pass_challengers[stage] !==0 ) {
                return stage_board[stage] / pass_challengers[stage]
            }
            return 0
        })()
        answer.push([stage, fail_percent]);
        
    }
    
    answer.sort((a,b)=> -a[1] + b[1] || a[0] - b[0])

    return answer.map(v=>v[0]);
}