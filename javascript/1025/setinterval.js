// 코드를 작성해 주세요
// setInterval(f, time) f: 실행하고 싶은 함수, /time : 시간(ms 단위)
setInterval(function() {}, 100)
// 정해진 시간 후에 콜백함수를 한번 실행
// setTimeout(f, time) f: 실ㅎ행하고 싶은 함수 / time : 시간 (ms 단위)
setTimeout(function () {}, 100)
let count = 0
function add() {
    console.log(count + '초')
    count += 1
}
const timer = setInterval(add, 1000)


const btn = document.querySelector("button")
btn.addEventListener('click', function () {
    //반복 중지
    clearInterval(timer)
})

setTimeout(function () {
    console.log('10초 후 중단')
    clearInterval(timer)
}, 10000)

const cases = ["scissors", "rock", "paper"]