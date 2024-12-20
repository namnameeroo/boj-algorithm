function solution(dirs) {
    let answer = 0;
    const move = {U:[-1,0],D:[1,0],R:[0,1],L:[0,-1]};
    
    // point = [U, D, R, L];
    // map[x][y] = [0,0,0,1];
    // map[a][b] = [0,0,1,0];
    
    
    // map x: 0~5~10
    // map y: 0~5~10
    
    // 현위치 = [U 방문 여부, D 방문 여부, R 방문여부, L 방문여부]
    // history[x좌표][y좌표] = [0,0,0,0];
    const history = new Array(11).fill(0).map(v=>new Array(11)
                                              .fill(0).map(v=>new Array(4)
                                                           .fill(0)));
    
    
    let currentX = 5;
    let currentY = 5;
    
    for (let dir of dirs) {
        let [mX, mY] = getPointByDir(dir, currentX, currentY);
        if (!isValidPoint(mX, mY)) {
            continue;
        }
   
        let dirIdx = getIndexOfDir(dir);
        let reversedDirIdx = getReversedIndexOfDir(dir);
        
        history[currentX][currentY][dirIdx] += 1;
        history[mX][mY][reversedDirIdx] += 1;
        history[currentX][currentY][dirIdx] === 1 && answer++;

        // move
        [currentX, currentY] = [mX, mY];
    }
    

    function getIndexOfDir(dir) {
        return ['U','D','R','L'].indexOf(dir);
    }
    
    function getReversedIndexOfDir(originDir) {
        return ['D','U','L','R'].indexOf(originDir);
    }
    
    function getPointByDir(dir, sx, sy) {
        return [sx+move[dir][0], sy+move[dir][1]];
    }
    
    function isValidPoint(x,y) {
        return (x > -1 && x < 11 && y > -1 && y < 11);
    }
    
    function getDirByPoint(sx, sy, ex, ey) {
        if (sx === ex) {
            return sy < ey ? 'R' : 'L';
        } else {
            return sx < ex ? 'D' : 'U';
        }
    }
    
    
    
    return answer;
}