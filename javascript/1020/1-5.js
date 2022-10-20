const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

for (let i = 0; i <= participantNums.length-1; i++) {
    for (let j = 0; j <= participantNums[i].length-1; j++) {
        let flag = false
        for (let k = j+1; k <= participantNums[i].length-1; k++) {
            if (participantNums[i][j] === participantNums[i][k]) {
                flag = true
                break   
            } 
        }
        if (flag === false) {
            console.log(participantNums[i][j])
            break
        }
    }
}