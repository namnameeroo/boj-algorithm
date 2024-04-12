function solution(numbers) {
    var answer = [];
    for (let num of numbers) {
        let t = getTarget(num)
        answer.push(t)
    }
    return answer;
}

function getTarget(num) {
    let candi = [];
    // console.log({numbi : num.toString(2)})
    let biNum = '0'+num.toString(2)
    
    // if (num%2===0) return num+1
    // 1111 => 10111
    // 1011 => 1111
    
    
    let target = '';
    let zIdx = 0;
    for (let i = biNum.length-1; i > 0; i--) {
        if (biNum[i] == 0) {
            zIdx = i;
            break;
        }
    }
    
    target = [...biNum];
        target[zIdx] = '1';
        if (zIdx !== biNum.length-1) {
            target[zIdx+1] = '0';            
        }
        return parseInt(target.join(''),2);
}