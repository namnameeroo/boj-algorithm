function solution(N, counters_info) {
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
  // reverse

  counters_info = counters_info.reverse();
  const answer = [];
  let arrows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let max_score = -1;

  dfs(0, N);

  // 종료 조건
  // 1. 남은 화살이 0개 일 때,
  // 2. 과녘 번호가 11 이상일 때

  // 라이언의 화살 현황
  function dfs(score_idx, arrow_res) {
    if (arrow_res < 1 || score_idx > 10) {
      let result = getDiffScore(arrows);
      if (result > max_score) {
        arrows[0] += arrow_res;
        answer.push([...arrows]);
        arrows[0] -= arrow_res;
        max_score = result;
      }
      return;
    }

    let need_arrow_cnt = counters_info[score_idx] + 1;
    let temp = arrows[score_idx];
    if (arrow_res >= need_arrow_cnt) {
      arrows[score_idx] = need_arrow_cnt;
      dfs(score_idx + 1, arrow_res - need_arrow_cnt);
    }
    arrows[score_idx] = temp;
    dfs(score_idx + 1, arrow_res);
  }

  function getDiffScore(ryan) {
    let rs = 0;
    let as = 0;
    for (let i = 0; i < 11; i++) {
      if (ryan[i] > counters_info[i]) {
        rs += i;
      } else if (ryan[i] === counters_info[i]) {
        continue;
      } else {
        as += i;
      }
    }
    const score_diff = rs - as;
    return score_diff > 0 ? score_diff : -1;
  }

  // 필요한 점수, 필요한 화살
  // 필요한 점수, 갖고 있는 화살

  // for문 돌면서 점수 계산

  let final = [-1];
  for (let ans of answer) {
    let result = getDiffScore(ans);
    if (result >= max_score && result != -1) {
      max_score = result;
      final = [...ans.reverse()];
    }
  }
  

  return final;
}
