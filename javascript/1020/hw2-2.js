for (let i = 0 ; i <= 4; i++) {
    let star = ''
    for (let j = i; j <= 3; j++) {
        star += ' '
    }
    for (let k = 0 ; k < (2*i+1); k++ ) {
        star += '*'
    }
    console.log(star)
}