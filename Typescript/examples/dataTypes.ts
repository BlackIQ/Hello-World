/**
 * Here is a complete exmaple of typescript data types
 */


/* =============================== Brief Examples =============================== */

let name: string = "Morteza" // string data type
let isAlive: boolean = true // boolean data type
let rand: number = 124 // number data type

let obj: object = {} // object data type
let arr: any[] = [] // array of elements via any data type
let tpl: [string, number] = ["test", 10] // tuple data type

let empt: null = null // null data type
let und: undefined = undefined // undefined data type
let vd: void = undefined // void data type

let an: any = "any" // any data type



/// String Data Type
let fullName: string = "Morteza Heydari"
let color = "dodgerblue"
let multiLineTxt: string = `
The first line of string
The seconds line of string
The third line of string
`


/// Number Data Type
let age: number = 24
let bgNum: bigint = 100n
let negNum: number = -1000


/// Object Data Type
let userInfo: {firstName: string, lastName: string, age: number, fullName: (a: string, b: string) => string} = {
    firstName: 'Morteza',
    lastName: 'Heydari',
    age: 24,
    fullName: function(fName: string, lastName: string) {
        return `${fName} ${lastName}`
    }
}


/// Array Data Type
let strGroup: string[] = ["number_1", "number_2", "number_3", "number_4"] // An array of strings
let numGroup: number[] = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512] // An array of numbers
let mixedGroup: any[] = ["mixed", 123, false, null, {year: 2021, bornIn: 1997}, ["this", "is", "another", "member"]] // A mixed array

// type {firtName: string, lastName: string}[] is an array of {firtName: string, lastName: string} object that you can write it also like so:
let diffArr: Array<{firtName: string, lastName: string}> = [
    {firtName: 'Morteza', lastName: 'Heydari'},
    {firtName: 'Ali', lastName: 'Mousavi'},
    {firtName: 'Ahmad', lastName: 'Azad'}
] // Array<elemType> is called generics


/// Tuple Data Type : Tuple is a fixed sized array that all elements' types are specified
let fixedArr: [string, boolean, undefined, number] = ["tuple", true, undefined, Infinity]



/* ===== Notes ===== */
// If you try to change one of the types, you will get an error unless than any data type. like this:
let strTyped: string = "Try to change my type"
strTyped = 10 // Now you will see the error

let anyTyped: any = "Now you can change my type !"
anyTyped = true // Type of anyTyped variable is changed to boolean
anyTyped = 200 // And now type of the anyTyped variable is changed to number




// =*=*=*=*=*=*=*=*=*=*=*=*=* Author: Morteza Heydari - Good Luck *=*=*=*=*=*=*=*=*=*=*=*=*= \\