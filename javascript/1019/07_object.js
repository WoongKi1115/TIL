const myInfo = {
    name: 'jack',
    phonenumber: '123456',
    'samsung product': {
        buds: 'Buds pro',
        galaxy: 'S99',
    }, 
}

console.log(myInfo.name)
console.log(myInfo['name'])
// key 이름에 띄어쓰기 같은 구분자가 있다면 .으로는 접근 불가
// 대괄호로 접근해야함(아래처럼)
console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].galaxy)

// 메서드명 축약
const obj = {
    name: 'jack',
    greeting() {
        console.log('hi!')
    }
}
console.log(obj.name)
console.log(obj.greeting())

const key = 'ssafy'
const value = ['한국', '미국', '일본']

const myObj = {
    [key]: value,
}

console.log(myObj)
console.log(myObj.ssafy)





const jsonData = {
    coffee: 'Americano',
    iceCream: 'Cooki and cream',
}

// Object => json json은 문자열 형태
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson)

// json => Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)