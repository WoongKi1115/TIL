// // 코드를 작성해 주세요
const cases = ["scissors", "rock", "paper"]
const player1img = document.querySelector("#player1-img")
const player2img = document.querySelector("#player2-img")
const scissorsbutton = document.querySelector('#scissors-button')
const rockbutton = document.querySelector('#rock-button')
const paperbutton = document.querySelector('#paper-button')
let countA = 0
let countB = 0
const rsp_game = (player1, player2) =>

const buttonclick = (rsp) => event => {
    scissorsbutton.disabled = true
    rockbutton.disabled = true
    paperbutton.disabled = true
    let i = 0
    const timer = setInterval(function() {
        i = (i+1)%3
        player2img.src = `./img/${cases[i]}.png`
        player1img.src = `./img/${rsp}.png`
    }, 100)
    setTimeout( function() {
        clearInterval(timer);
        randomIdx = Math.floor(Math.random() * 3)
        player2img.src = `./img/${cases[randomIdx]}.png`
        scissorsbutton.disabled = false
        rockbutton.disabled = false
        paperbutton.disabled = false
    }, 3000)
}
scissorsbutton.addEventListener('click', buttonclick('scissors'))
rockbutton.addEventListener('click', buttonclick('rock'))
paperbutton.addEventListener('click', buttonclick('paper'))
