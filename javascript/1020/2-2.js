const users = [
    { name: 'John', age: 31, isMarried: true, balance: 100, },
    { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
    { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
    { name: 'Robert', age: 27, isMarried: false, balance: 400, },
    { name: 'Tom', age: 35, isMarried: true, balance: 500, },
  ]
  // 1.
  const names = users.forEach((user) => {
    return console.log(user.name)
  });

  // 2.
  const married = users.filter((user) => {
    if (user.isMarried === true) {
      return console.log(user.name)
    }
  })

  // 3.
  const tom = users.find((user) => {
    return user.name === 'Tom'
  })

  // 4.
  const newUsers = users.map((user) => {
    return user.isAlive = true
  })
  console.log(newUsers)

  // 5.
  totalBalance = users.reduce((totalbalance, user) => {
    return totalbalance + user.balance
  }, 0)
  console.log(totalBalance)