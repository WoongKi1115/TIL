// function add(num1, num2) {
//   return num1 + num2    
// }

// console.log(add(2, 7))

// // 익명함수
// const sub = function (num1, num2) {
//   return num1 - num2
// }

// console.log(sub(2,7))

// const greeting = function (name = 'Annoymous') {
//   return `Hi ${name}`
// }

// console.log(greeting())

// 매개변수가 인자보다 많아도 에러가 안뜨고 출력됨

// function (num) {return num ** 3}
// (num) => {return num ** 3}
// ((num) => num ** 3)(2)

const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers[numbers.length-1])

numbers.reverse( )
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop( )
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))

console.log(numbers.join( ))
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))