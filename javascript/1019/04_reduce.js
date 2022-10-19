const numbers = [90, 80, 70, 100]

// 총합 function 부분은 콜백함수
// const sumNum = numbers.reduce(function (result, number) {
//     return result + number
// }, 0)

// // result 는 누적 값
// reduce(a, b)
// b는 누적될 값(result의 초기 값을 의미. )

const sumNum = numbers.reduce((result, number) => {
    return result + number
}, 0)
console.log(sumNum)