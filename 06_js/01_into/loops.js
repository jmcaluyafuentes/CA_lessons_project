// Main Topic: Loops
console.log('Main Topic: Loops')

// -----------------------------------------
// Topic: While loop
console.log('------------------------------')
console.log('Topic: While loop')

// In Python
// count = 5
// while count > 0:
//      print(count)
//      count -= 1

let count = 4           // ?? why this is declared 'let' when it is decremented inside the while loop?
while (count > 0){
    console.log(count)
    count --
}

// -----------------------------------------
// Topic: While loop
console.log('------------------------------')
console.log('Topic: While loop - Example 2')

let count1 = 4           // ?? why this is declared 'let' when it is decremented inside the while loop?
while (count1 > 0){
    console.log(count1--) // shorter method
}

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop')

// Python
// for i in range(10):
//      print(i)

// In JS, it is 3-part for loop
// initializer: runs once only, before the first iteration
// condition: will be tested before every iteration. It determines if another iteration will takes place or not
// post-iteration: will be evaluated after every iteration before the next condition will be tested again

// for (initializer; condition; post-iteration) {}

for (let i=0; i<10; ++i){
    console.log(i)
}

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 2')

const numbers = [1, 2, 5, 44, 37]

for (let i=0; i < numbers.length; i++){
    console.log(numbers[i])
}

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 3')

const numbers1 = [1, 2, 5, 44, 37]
let res = []
for (let i=0; i < numbers.length; i++){
    res.push(`${i+1}. ${numbers[i]}`)
}

console.log(res)

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 4 - Fibonacci sequence')

const fib = [1]
for (let prev=1, next=1; next <= 100; temp=next, next=prev+next, prev=temp){
    fib.push(next)
}

console.log(fib)

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 5 - iterate an array')

const favFoods = ['pizza', 'pasta', 'tacos']

// Python
// for food in favFoods:
//      print(food)

for (let food of favFoods) { // keyword 'of' to get the element
    console.log(food)
}

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 6 - iterate an array')

// Python
// for food in favFoods:
//      print(food)

for (let food in favFoods) { // keyword 'in' to get the index
    console.log(food)
}

// -----------------------------------------
// Topic: For loop
console.log('------------------------------')
console.log('Topic: For loop - Example 7 - iterate an array')

// Python
// for food in favFoods:
//      print(food)

favFoods.forEach((food, index) => { // Callback function
    console.log(`${index+1}. ${food}`)
})

favFoods.forEach(food => console.log(food)) // There is no significance performance difference between for loop and forEach





