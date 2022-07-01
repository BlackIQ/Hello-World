/* Typescript Interface */

// Note below example
function getUserInfo(firstName: string, lastName: string, age: number): string {
    let infoText = `Hi, I'm ${firstName} ${lastName} and I'm ${age} years old !`;

    return infoText
}

// You can rewrite above example by interface like so:
interface UserInfo {
    firstName: string
    lastName: string
    age: number
}

function getPrimaryUserInfo(info: UserInfo): string {
    let infoText = `Hi, I'm ${info.firstName} ${info.lastName} and I'm ${info.age} years old !`;

    return infoText;
}


/**
 * An interface is one of another typescript types
 * You can create an interface in typescript by `interface` keyword as you saw in above
 * You can increase useability and readability of your code by using interfaces
 * Let's define a bit complex interface:
 */
interface FullNameRequirements {
    firstName: string
    lastName: string
}
interface User {
    fName: string
    lName: string
    age: number

    // This is how to can define a property with function type
    getFullName: (data: FullNameRequirements) => string
}

let user: User = {
    fName: "Morteza",
    lName: "Heydari",
    age: 24,
    getFullName: (data) => {
        return `${data.firstName} ${data.lastName}`
    }
}
user.getFullName({firstName: user.fName, lastName: user.lName})


// Optional and Readonly property
interface Country {
    name: string
    populity: number

    // You can make a property optional by a question mark like so:
    coordinates?: {latitude: number, longitude: number}
    
    // Notice: You can set value for optional properties or not but if you don't set value for required value you will get error
    
    // You can make a property by `readonly` keyword like so:
    readonly flag?: () => void
}


// Inheritance
interface Human {
    gender: "male" | "female"
    
    firstName: string
    lastName: string

    height?: number
    wieght?: number
}

interface SystemUser extends Human {
    id: number
    username: string
    password: string
    email?: string
    phone?: string
}

let superAdmin: SystemUser = {
    id: 1,
    username: 'M.H',
    password: '12345',
    firstName: 'Morteza',
    lastName: 'Heydari',
    gender: 'male',
    email: 'mortezaheydarime@gmail.com',
    
}
// or:
let admin = {} as SystemUser;
admin.id = 1;
admin.username = 'M.H';
admin.password = '12345';
admin.firstName = 'Morteza';
admin.lastName = 'Heydari';
admin.gender = 'male';
admin.email = 'mortezaheydarime@gmail.com';