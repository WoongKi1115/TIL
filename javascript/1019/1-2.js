function palindrome(str) {
  str = String(str)
  pal = ''
  for (let i = str.length; i === 0; i--) {
    pal = pal + str[i]
  }
  console.log(pal)
  if (str === pal) {
    console.log('true')
  } else {
    console.log('false')
  }
}

console.log(palindrome(level))