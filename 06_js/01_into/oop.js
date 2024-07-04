// Main Topic: Loops
console.log('Main Topic: OOP')
console.log('Date: 4/7/24 Thursday')

// -----------------------------------------
// Topic: Object
console.log('------------------------------')
console.log('Topic: Objects')

const person = {
    name: 'John',
    age: 34
}

console.log(person)         // { name: 'John', age: 34 }
console.log(typeof person)  // object

// -----------------------------------------
// Topic: Object
console.log('------------------------------')
console.log('Topic: Objects - Example 2')

// Python:
// class Person:    
//      def __init__(self, name, age):          // __init__ is the constructor
//          self.name = name
//          self.age = age
//
// person = Person('John', 35)

const person1 = {} // In the background: const person1 = new Object() <-- constructor function
person1.name = 'John'
person1.age = 35

console.log(person1)        // { name: 'John', age: 35 }
console.log(typeof person1) // object

// -----------------------------------------
// Topic: Object
console.log('------------------------------')
console.log('Topic: Objects - Example 2.2')

// Python:
// class Person:
//      def __init__(self, name, age):
//          self.name = name
//          self.age = age
//
// person = Person('John', 35)

const person2 = new Object() // <-- constructor function
person2.name = 'John'
person2.age = 35

console.log(person2)        // { name: 'John', age: 35 }
console.log(typeof person2) // object

// -----------------------------------------
// Topic: Object
console.log('------------------------------')
console.log('Topic: Objects - Example 2.3 - Create own constructor function')

// Python:
// class Person:
//      def __init__(self, name, age):
//          self.name = name
//          self.age = age
//
// person = Person('John', 35)

function Person(name, age) {    // Person (capital letter) is a convention for constructor function
    this.name = name
    this.age = age

    this.greet = () => {
        console.log(`${name} is ${age} years old.`) // The name and age are referring to the parameters and not the attributes from this.name and this.age
    }
}

const person3 = new Person('John', 35) // <-- constructor function

person3.greet()                        // John is 35 years old.

person3.age = 36
person3.greet()                        // John is 35 years old. <-- the age was not change in the greet method
console.log(person3.age)                // John is 36 years old.

// -----------------------------------------
// Topic: Object
console.log('------------------------------')
console.log('Topic: Objects - Example 2.3.1 - Create own constructor function - The corrected method in greet')

// Python:
// class Person:
//      def __init__(self, name, age):
//          self.name = name
//          self.age = age
//
// person = Person('John', 35)

function Person1(name, age) {    // Person (capital letter) is a convention for constructor function
    this.name = name
    this.age = age

    this.greet = () => {
        console.log(`${this.name} is ${this.age} years old.`) // Now, the name and age are referring to the attributes from this.name and this.age
    }                                                         // The issue is there are my instances of the object, the greet method will be replicated in each instance
}

const person4 = new Person1('John', 35) // <-- constructor function

person4.greet()                        // John is 35 years old.

person4.age = 36
person4.greet()                        // John is 35 years old. <-- the age was not change in the greet method
console.log(person4.age)                // John is 36 years old.

// -----------------------------------------
// Topic: Class
console.log('------------------------------')
console.log('Topic: Class - Example 2.3.2 - Create own constructor function - The corrected method in greet - Resolve the issue by use of a class')

// Python:
// class Person:
//      def __init__(self, name, age):
//          self.name = name
//          self.age = age
//
// person = Person('John', 35)

// function Person2(name, age) {    // Person (capital letter) is a convention for constructor function
//     this.name = name
//     this.age = age

//     this.greet = () => {
//         console.log(`${this.name} is ${this.age} years old.`) // Now, the name and age are referring to the attributes from this.name and this.age
//     }
// }

class Person2 {
    constructor(name, age) { // Constructor function (with keyword 'constructor') inside a class. Remove the keyword 'function'
        this.name = name
        this.age = age
    }

    greet() { // Remove the 'function' keyword
        console.log(`${this.name} is ${this.age} years old.`) // If we forget to add the 'this' keyword, it will catch an error 'ReferenceError: name is not defined'
    }                                                         // The parameters name and age in constructor function are scope within it. The greet method must use 'this' to access them.
}                                                             // The greet method will only have one in memory and is shared by instances of the class.

const person5 = new Person2('John', 35) // <-- constructor function

person5.greet()                        // John is 35 years old.

person5.age = 36
person5.greet()                        // John is 35 years old. <-- the age was not change in the greet method
console.log(person5.age)                // John is 36 years old.

// -----------------------------------------
// Topic: Class
console.log('------------------------------')
console.log('Topic: Class - Example (Rectangle) - with error')

class Rectangle {
    constructor(width, height) {
        this.width = width
        this.height = height
    }

    area() {
        return this.width * this.height
    }                                                         
}                                                             

const rect = new Rectangle(10, 20)
rect.area = 5
// console.log(rect.area()) // TypeError: rect.area is not a function

// ~~ Review the explanation in recorded class video


// -----------------------------------------
// Topic: Class
console.log('------------------------------')
console.log('Topic: Class - Example (Rectangle) 2 - corrected')

class Rectangle1 {
    constructor(width, height) {
        this.width = width
        this.height = height
    }

    get area() { // Adding a keyword 'get' makes it a get property
        return this.width * this.height
    }                                                         
}                                                             

const rect1 = new Rectangle1(10, 20)
rect1.area = 5 // It will change the area since area is getter
console.log(rect1.area) // 200

rect1.width = 5
console.log(rect1.area) // 100

rect1.width = 'hi'
console.log(rect1.area) // NaN <-- Not a Number

// -----------------------------------------
// Topic: Class
console.log('------------------------------')
console.log('Topic: Class - Example (Rectangle) 2 - corrected 2')

class Rectangle2 {
    #width      // Declare the private in the class
    #height

    constructor(width, height) {
        this.#width = width // '#' sets width as a private
        this.#height = height
    }

    get width() { return this.#width}

    set width(value) {
        if (typeof value === 'number') {
            this.#width = value
        } else {
            // Raise exception
            console.log('Invalid value - must be a number')
        }
    }

    get area() { // Adding a keyword 'get' makes it a get property
        return this.#width * this.#height
    }                                                         
}                                                             

const rect2 = new Rectangle2(10, 20)
rect2.area = 5 // It will change the area since area is getter
console.log(rect2.area) // 200

rect2.width = 5
console.log(rect2.area) // 100

rect2.width = 'hi' // Invalid value - must be a number <-- Error

// -----------------------------------------
// Topic: Class
console.log('------------------------------')
console.log('Topic: Class - Inheritance')

class Rectangle3 {
    #width      // Declare the private in the class
    #height

    constructor(width, height) {
        this.#width = width // '#' sets width as a private
        this.#height = height
    }

    get width() { return this.#width}

    set width(value) {
        if (typeof value === 'number') {
            this.#width = value
        } else {
            // Raise exception
            console.log('Invalid value - must be a number')
        }
    }

    get area() { // Adding a keyword 'get' makes it a get property
        return this.#width * this.#height
    }                                                         
}     

// Python
// class Square(Rectangle)

class Square extends Rectangle3 { // Keyword 'extends' for class inheritance
    #width  // Declare it in child class since it is private in superclass
    #height
    
    constructor(size=5) { // default parameter
        super(size, size) // This calls the super constructor and passes the value size into width and height
    }
}

const rect4 = new Square(10) // positional parameter
console.log(rect4.area) // 100

const rect5 = new Square()
console.log(rect5.area) // 25

const rect6 = new Square(size=6) // keyword parameter
console.log(rect6.area) // 36



