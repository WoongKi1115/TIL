const arr = [1, 2, 3, 4, 5]
// some : 하나만 통과해도 true 출력 빈 배열은 false
// every : 전부 통과해야 true 출력. 빈 배열은 True

// 1. 
const result = arr.some(function (elem) {
    return elem % 2 === 0
})

// // 2.
// const result = arr.some((elem) => {
//     return elem % 2 === 0
// })
// const result = arr.some((elem) => elem % 2 === 0)
console.log(result)

// 1. 
// const result = arr.every(function (elem) {
//     return elem % 2 === 0
// })

// // 2.
// const result = arr.every((elem) => {
//     return elem % 2 === 0
// })
// const result = arr.every((elem) => elem % 2 === 0)
console.log(result)