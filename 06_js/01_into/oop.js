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
}

const person3 = new Person('John', 35) // <-- constructor function

console.log(person3)        // { name: 'John', age: 35 }
console.log(typeof person3) // object






