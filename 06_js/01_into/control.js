// Main Topic: Control structure
console.log('Main Topic: Control structure')

// -----------------------------------------
// Topic: if statement
console.log('------------------------------')
console.log('Topic: if statement')

//Python
// age = 16
// if age >= 18:
//      print('Adult')
// elif age >= 13:
//      print('Teen')
// else:
//      print('Child')

const age = 16

if (age >= 18){            // <-- the condition must have paranthesis
    console.log('Adult')   
} else if (age >= 13){      // <-- in Python this is "elif"
    console.log('Teen')
} else {
    console.log('Child')
}

// -----------------------------------------
// Topic: ternary statement
console.log('------------------------------')
console.log('Topic: ternary statement')

// Python
// message = 'Allowed' if age >= 18 else 'Not Allowed'

const message = age >= 18 ? 'Allowed' : 'Not Allowed'
console.log(message)

// -----------------------------------------
// Topic: switch statement
console.log('------------------------------')
console.log('Topic: switch statement')

// Python
// match name:
//      case 'Matt' | 'Matty':  <-- to match multiple values in one case
//          pass
//      case 'Mary':
//          pass
//      case _:                 <-- catches all
//          pass

const favBird = 'Crow' // try the value Raven, Ibis

switch (favBird) {
    case 'Raven':
    case 'Crow':
        console.log('You like crows!')
        break       // add break to stop the fall through
    case 'Magpie':
        console.log('You like magpies!')
        break
    default:        // to catch all unmatched cases
        console.log('I don\'t know that bird!')
}

// Output:
// You like crows!
// You like magpies! <-- fall through happened to the next block/s

// in Python, once found the match, it will stop the executing the next block/s
// in JS, once found the match, it will still search for the next block/s












