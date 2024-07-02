// Topic: Variable and Constant
console.log('------------------------------')
console.log('Topic: Variable and Constant')

const maxTemp = 28
console.log(maxTemp)
// maxTemp = 30
// console.log(maxTemp)


// -----------------------------------------
// Topic: Scope
console.log('------------------------------')
console.log('Topic: Scope')

x = 'Sarah'

{
    console.log(x)
    y = 5  // JS is interpreting it as var y = 5, thus it is global scope
}

console.log(y) // 5

z = 'Sarah'

{
    let z = 5
}

// console.log(z) <-- this will not return an error is y is let


// -----------------------------------------
// Topic: Index, slice
console.log('------------------------------')
console.log('Topic: Index, slice')

let str = 'Hello World!'
console.log(str.indexOf('l'))
console.log(str.slice(2, 5)) // 'llo' 
console.log(str[str.length-1]) // Gets the character of last index
console.log(str.replace('l', '---')) // 'Hell--- World' <-- It only replaces the first instance of 'l'
console.log(str.replaceAll('l', '---')) // 'Hell--- W---rld' <-- It replaces all instances of 'l'
console.log(str) // The replace method above is non-destructive


// -----------------------------------------
// Topic: String interpolation
console.log('------------------------------')
console.log('Topic: String interpolation')

// Python: print(f'Hello, {firstName}')
let firstName = 'John'
console.log(`Hello, ${firstName}!`) // Use backticks, no keyword 'f' and ${ }

console.log(`Hello, ${5 + 10}!`) // Anything valid expressions can go inside the { }


// -----------------------------------------
// Topic: String interpolation
console.log('------------------------------')
console.log('Topic: String interpolation - Example 2')

const item = 'laptop';
const price = 1200;

const receipt = `Item: ${item}
Price: $${price}
Thank you for your purchase!`;

console.log(receipt);


// -----------------------------------------
// Topic: Basic Arithmetic
console.log('------------------------------')
console.log('Topic: Basic Arithmetic')

console.log(3 / 2) // 1.5 <-- floating point division
console.log(Math.floor(3 / 2)) // 1 <-- truncate or round down
console.log(Math.ceil(3 / 2)) // 2 <-- roundup

console.log(typeof Math.floor(3 / 2)) // number <-- there is no int or float in JS

let a = 5
console.log(a)
// Increment x in Python: a += 1
a += 1 // 6
a++ // 6 <-- 'Post Increment' <-- This expression is not available in Python
console.log(a)
--a // 5 <-- 'Pre Increment'
console.log(a)

// -----------------------------------------
// Difference between pre and post increment
console.log('------------------------------')
console.log('Topic: Difference between pre and post increment')

let b = 10
console.log(b++) // 10 <-- It retrieves the value of b and outputs it in console before incrementing it

let c = 10
console.log(++c) // 11

// -----------------------------------------
// Topic: Boolean
console.log('------------------------------')
console.log('Topic: Boolean')

console.log(123 == 123) // true <-- loose equality (the value must be equal, the type does not matter)
console.log('123' == 123) // true <-- type coercion, JS will implicitly cast the other value so that it can do the comparison

console.log('123' === 123) // false <-- strict equality (the value and type must be equal) <-- JS will skip the type coercion

// Note: Cannot do type casting in JS


// -----------------------------------------
// Topic: Literal Object
console.log('------------------------------')
console.log('Topic: Literal Object')

// Python dict: person = {"name": "John"}

let person = {name: "John"} // <-- name is not a string but a symbol. Unlike in Python, name is enclosed in "name"
console.log(typeof person) // object
console.log(person['name']) // John
console.log(person.name) // John <-- We accessed the property using dot notation


let person1 = {
    name: 'Mark',
    age: 15,
    address: {
        street: '51A',
        suburb: 'Forrest Hill'
    }
}
console.log(person1.name, person1.age, person1.address.street) // Mark 15 51A


// -----------------------------------------
// Topic: Array
console.log('------------------------------')
console.log('Topic: Array')

// Python: x = [1, 2, 3, 3.1416]

let d = [1, 2, 3, 3.1416, true, 'Hello']
console.log(d) // [1, 2, 3, 3.1416, true, 'Hello']
console.log(d[0]) // 1
console.log(d[d.length-1]) // Hello


// -----------------------------------------
// Topic: Array
console.log('------------------------------')
console.log('Topic: Function')

// Python
// def add(x, y):
//     return x + y

function add(x, y) {
    return x + y
}

console.log(add(10, 7)) // 17

// -----------------------------------------
// Topic: Array
console.log('------------------------------')
console.log('Topic: Arrow Function')

function subtract(x, y) { return x + y } // JS does not require indentation unlike Python where indentation is part of syntax.
                                         // This format is only advisable for a single expression

console.log(subtract(10, 7)) // 3


const multiply = (x, y) => { return x * y } // Inline anonymous function
console.log(multiply) // [Function: multiply] <-- This is only referring to multiply as a function, it is not calling the function
console.log(multiply(2, 3)) // 6


// Shortcut for arrow function
const division = (x, y) =>  x / y // <-- Can only do this if the code is a single return statement
console.log(division(10, 5)) // 2

// Shortcut for arrow function - if only one parameter
const multiplyByTwo = x => x * 2
console.log(multiplyByTwo(2)) // 4
