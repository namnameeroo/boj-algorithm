function solution(a, b) {
    let answer = parseInt(a.toString() + b.toString());
    
    return answer>=parseInt(2*a*b) ? answer : 2*a*b;
}