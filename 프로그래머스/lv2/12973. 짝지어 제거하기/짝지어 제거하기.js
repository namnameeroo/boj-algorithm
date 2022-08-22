function solution(s)
{
    if (s.length%2 != 0) {
        return 0;
    }else{

        return cycle(s);
    }

}

function cycle(arr){
    let stack = [];

    if (!arr) return 1;
    for (e of arr){
        if (stack[stack.length-1] == e){
            stack.pop();
        }else{
            stack.push(e);
        }
    }

    if (stack.length == 0) return 1;
    if (stack[0]==stack[1]) return 1;
    
    return 0;

}