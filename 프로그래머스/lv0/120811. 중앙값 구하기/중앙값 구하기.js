function solution(array) {
    array.sort((pre,post)=>{
        return pre-post
    });
    let idx = parseInt(array.length/2);
    return array[idx];
}