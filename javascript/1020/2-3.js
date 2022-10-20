const defaultColors = ['red', 'green', 'blue'];
const favoriteColors = ['navy', 'black', 'gold', 'white', ...defaultColors]

console.log(favoriteColors)

// 3-2
const info1 = { name: 'Tom', age: 30 }
const info2 = {...info1, isMarried: true, balance: 3000 }
console.log(info2)