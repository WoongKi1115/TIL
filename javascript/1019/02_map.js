const numbers = [1, 2, 3, 4, 5]
// 1. map은 순회 + 결과값을 새로운 배열에 추가해서 배열 출력
// const doubleEle = function (number) {
//   return number * 2
// }

// const newArry = numbers.map(doubleEle)

// console.log(newArry)
// // 2.
// const newArry = numbers.map(function (number) {
//     return number * 2
// })

// 3.
const newArry = numbers.map( (number) => { 
  return number * 2
})
console.log(newArry)
// 4.
// const newArry = numbers.map((number) => number * 2)
