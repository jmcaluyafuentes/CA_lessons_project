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
// Topic: Function
console.log('------------------------------')
console.log('Topic: Function')

// Python
// def add(x, y):
//     return x + y

function add(x, y) {
    return x + y
}

console.log(add(10, 7)) // 17

function subtract(x, y) { return x + y } // JS does not require indentation unlike Python where indentation is part of syntax.
                                         // This format is only advisable for a single expression

console.log(subtract(10, 7)) // 3

// -----------------------------------------
// Topic: Arrow Function
console.log('------------------------------')
console.log('Topic: Arrow Function')


const multiply = (x, y) => { return x * y } // Inline anonymous function
console.log(multiply) // [Function: multiply] <-- This is only referring to multiply as a function, it is not calling the function
console.log(multiply(2, 3)) // 6


// Shortcut for arrow function
const division = (x, y) =>  x / y // <-- Can only do this if the code is a single return statement
console.log(division(10, 5)) // 2

// Shortcut for arrow function - if only one parameter
const multiplyByTwo = x => x * 2
console.log(multiplyByTwo(2)) // 4

// -----------------------------------------
// Day 2: Tuesday 3/7/24
// Topic: Map method
console.log('------------------------------')
console.log('Day 2: Tuesday 3/7/24')
console.log('------------------------------')
console.log('Topic: Functions are first class objects')
console.log('Topic: Map method')

const square = x => x ** 2

console.log(square(10)) // 100

const numbers = [1, 2, 3, 4]
const result = numbers.map(square) 
console.log(result) // [1, 4, 9, 16]

const result1 = numbers.map(x => x ** 2)
console.log(result1) // [1, 4, 9, 16]

// -----------------------------------------
// Topic: Destructure
console.log('------------------------------')
console.log('Topic: Functions are first class objects')
console.log('Example 2.1 -- hardcode but prone to error')

const people = ['Matt', 'John', 'Mary', 'Kate']

const name1 = people[0]
const name2 = people[1]

console.log(name1, name2) // Matt John

// -----------------------------------------
// Topic: Destructure
console.log('------------------------------')
console.log('Topic: Functions are first class objects')
console.log('Example 2.2 -- descriptive identifiers but still prone to error')

const people1 = ['Matt', 'John', 'Mary', 'Kate']

const first = people[0] // identifiers are more descriptive
const second = people[1]

console.log(first, second) // Matt John

// -----------------------------------------
// Topic: Destructure
console.log('------------------------------')
console.log('Topic: Functions are first class objects')
console.log('Example 2.3 -- Destructure') // To prevent errors in hardcoding identifiers

const people2 = ['Matt', 'John', 'Mary', 'Kate']

const [first2, second2] = people

console.log(first2, second2) // Matt John 

// -----------------------------------------
// Topic: Destructure
console.log('------------------------------')
console.log('Topic: Functions are first class objects')
console.log('Example 2.3 -- Destructure - example 2') // To prevent errors in hardcoding identifiers

const people3 = ['Matt', 'John', 'Mary', 'Kate']

const [first3, second3, ...foo] = people // '...' is called rest operator

console.log(first3, second3, foo) // Matt John [ 'Mary', 'Kate' ]

// -----------------------------------------
// Topic: Concatenate arrays
console.log('------------------------------')
console.log('Topic: Concatenate arrays - wrong way')

const bobBirds = ['Robin', 'Crow']
const sallyBirds = ['Bluejay', 'Cardinal']

// Python: bobBirds + sallyBirds

const allBirds = bobBirds + sallyBirds // <-- + coercized the arrays into strings

console.log(allBirds) // Robin,CrowBluejay,Cardinal 
console.log(typeof allBirds) // string

// -----------------------------------------
// Topic: Concatenate arrays
console.log('------------------------------')
console.log('Topic: Concatenate arrays')

const bobBirds1 = ['Robin', 'Crow']
const sallyBirds1 = ['Bluejay', 'Cardinal']

// Python: bobBirds + sallyBirds

const allBirds1 = bobBirds1.concat(sallyBirds1) // <-- + coercized the arrays into strings

console.log(allBirds1) // [ 'Robin', 'Crow', 'Bluejay', 'Cardinal' ]
console.log(typeof allBirds1) // object

// -----------------------------------------
// Topic: Concatenate arrays and spread operator
console.log('------------------------------')
console.log('Topic: Concatenate arrays - using spread or expansion operator')

const bobBirds2 = ['Robin', 'Crow']
const sallyBirds2 = ['Bluejay', 'Cardinal']

// Python: bobBirds + sallyBirds

const allBirds2 = bobBirds2.concat(sallyBirds2) // <-- + coercized the arrays into strings

console.log(...allBirds2) // Robin Crow Bluejay Cardinal
console.log(typeof allBirds2) // object

// -----------------------------------------
// Topic: Concatenate arrays and spread operator (method 2)
console.log('------------------------------')
console.log('Topic: Concatenate arrays - using spread or expansion operator - Method 2')
console.log('***This technique will be useful in React JS***')

const bobBirds3 = ['Robin', 'Crow']
const sallyBirds3 = ['Bluejay', 'Cardinal']

// Python: bobBirds + sallyBirds

const allBirds3 = [...bobBirds3, ...sallyBirds3] // <-- '+' coercized the arrays into strings

console.log(allBirds3) // [ 'Robin', 'Crow', 'Bluejay', 'Cardinal' ]
console.log(typeof allBirds3) // object

// -----------------------------------------
// Topic: Concatenate arrays and spread operator (method 2)
console.log('------------------------------')
console.log('Topic: Concatenate arrays - using spread or expansion operator - Method 2 - Example 2')
console.log('***This technique will be useful in React JS***')

const bobBirds4 = ['Robin', 'Crow'] // What we're declaring const is the object itself and not the values. 
                                    // Array are data structures and not data types
                                    // You cannot change an array into another data structure if declared as const
                                    // If you want also the contents of an array to be immutable or cant change, you can make it freeze
const sallyBirds4 = ['Bluejay', 'Cardinal']

// Python: bobBirds + sallyBirds

const allBirds4 = [...bobBirds4, 'Bulba', ...sallyBirds4, 'Pickachu'] // <-- + coercized the arrays into strings

console.log(allBirds4) // [ 'Robin', 'Crow', 'Bulba', 'Bluejay', 'Cardinal', 'Pickachu' ]
console.log(typeof allBirds4) // object

// -----------------------------------------
// Topic: Concatenate arrays and spread operator (method 2)
console.log('------------------------------')
console.log('Another example')

const me = {name: 'Matt', age: 51, favouriteColor: 'red'}
const address = {city: 'Brisbase', state: 'QLD'}

const thisPerson = {...me, ...address}

console.log(typeof thisPerson) // object
console.log(thisPerson)     //{
                            //    name: 'Matt',
                            //    age: 51,
                            //    favouriteColor: 'red',
                            //    city: 'Brisbase',
                            //    state: 'QLD'
                            //  }               

// -----------------------------------------
// Topic: Concatenate arrays and spread operator (method 2)
console.log('------------------------------')
console.log('Another example')

const me1 = {name: 'Matt', age: 51, favouriteColor: 'red'}
const address1 = {city: 'Brisbase', state: 'QLD'}

const thisPerson1 = {...me, ...address, city: 'Melbourne'}

console.log(typeof thisPerson1) // object
console.log(thisPerson1)    //{
                            //    name: 'Matt',
                            //    age: 51,
                            //    favouriteColor: 'red',
                            //    city: 'Melbourne',       <-- value of city has been updated
                            //    state: 'QLD'
                            //  }







