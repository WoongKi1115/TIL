// function palindrome(str) {
//     let reverse = ''
//     for (let i = str.length-1; i>=0 ; i--) {
//         reverse = reverse + str[i]
//     }
//     console.log(reverse == str)
//   }
// palindrome('level')
// palindrome('Hi')

const tom = {
    name: 'Tom',
    introduce() {
      console.log('Hi, my name is' + this.name)
    }
  }
tom.introduce()