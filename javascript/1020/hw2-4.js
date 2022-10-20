const inputs = [
            
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  function solution(K, N, M, chargers) {
    let count = 0
    let mf1 = K
    for ( let i = 1; i <= N; i++) {
        console.log(i)
        mf1 -= 1
        a = []
        for (let j = i; j <= i+mf1; j++) {
            console.log(i, i+mf1)
          if (j in chargers) {
            a.push(j)
          }
        }
        console.log(a)
        if (a.length > 1) {
          continue
        } else if (a.length == 0) {
          count = 0
          console.log(count)
          break
        } else if (i in chargers) {
          mf1 = K
          count += 1
        }
        if ((i + mf1) >= N) {
            console.log(count)
          break
        }
        

    }
  }
  
  for (const input of inputs) {
    solution(input[0], input[1], input[2], input[3])
  }