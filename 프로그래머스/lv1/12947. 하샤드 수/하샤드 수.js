function solution(x) {
    var answer =false ;
    let tot = 0;
    for (s of String(x)){
        tot += parseInt(s);
    }

    if (x%tot==0){
        answer = true;
    }
    
    
    return answer;
}