// TASK 1: Write a code that will create variables and initialize them with values of Boolean, Number, BigInt, String, and undeefined types using (when possible) literals and constructor functions.

let b1;
let b2 = Boolean(true);

let n1 = 50;
let n2 = Number(50);

let bi1 = 50n;
let bi2 = BigInt(50);

let s1 = "Hello";
let s2 = String("Hello");

let u1 = undefined;

// TASK 2: Print all values and all types of those values. Try to use string interpolation to display the value and type at the same time with a single call.

console.log(`b1: ${b1}, type: ${typeof b1}`);
console.log(`b2: ${b2}, type: ${typeof b2}`);
console.log(`n1: ${n1}, type: ${typeof n1}`);
console.log(`n2: ${n2}, type: ${typeof n2}`);
console.log(`bi1: ${bi1}, type: ${typeof bi1}`);
console.log(`bi2: ${bi2}, type: ${typeof bi2}`);
console.log(`s1: ${s1}, type: ${typeof s1}`);
console.log(`s2: ${s2}, type: ${typeof s2}`);
console.log(`u1: ${u1}, type: ${typeof u1}`);

// TASK 3: Carry out a chain of conversions. Create a Boolean from a BigInt created from a Number that was created from a String. Start with the value "1234".

let s3 = "1234";
let n3 = Number(s3);
let bi3 = BigInt(n3);
let b3 = Boolean(bi3);

console.log(`s: ${s3}, type: ${typeof s3}`);

// TASK 4: Try adding two values of the same type and check the result type. Try it for all primitive types.

let b4 = true + false;
let n4 = 50 + 50;
let bi4 = 50n + 50n;
let s4 = "Hello" + " World";
let u4 = undefined + undefined;

console.log(`b: ${b4}, type: ${typeof b4}`);
console.log(`n: ${n4}, type: ${typeof n4}`);  
console.log(`bi: ${bi4}, type: ${typeof bi4}`);
console.log(`s: ${s4}, type: ${typeof s4}`);
console.log(`u: ${u4}, type: ${typeof u4}`);

// TASK 5: Try adding two values of different types and check the result.

let a = true + 50;      // boolean + num
//let b = true + 50n;   // boolean + bigInt -> ERROR
let c = true + "50";    // boolean + string

let d = 50 +true;       // num + boolean
//let e = 50 + 50n;     // num + bigInt -> ERROR
let f = 50 + "50";      // num + string

let g = 50n + "50";     //bigInt + string
//let h = 50n + 50;     //bigInt + num -> ERROR
//let i = 50n + true;   //bigInt + boolean -> ERROR

let j = "50" + 50;      // string + num
let k = "50" + 50n;     // string + bigInt
let l = "50" + true;    // string + boolean
let m = "abc" + 50;     // string (letters) + num
let n = "abc" + 50n;    // string (letters) + bigInt
let o = "abc" + true;   // string (letters) + boolean

console.log(`a: ${a}, type: ${typeof a}`);      // -> 51 [number]
//console.log(`b: ${b}, type: ${typeof b}`);    // ERROR
console.log(`c: ${c}, type: ${typeof c}`);      // -> true50 [string]
console.log(`d: ${d}, type: ${typeof d}`);      // -> 51 [number]
//console.log(`e: ${e}, type: ${typeof e}`);    // ERROR
console.log(`f: ${f}, type: ${typeof f}`);      // -> 5050 [string]
console.log(`g: ${g}, type: ${typeof g}`);      // -> 5050 [string]
//console.log(`h: ${h}, type: ${typeof h}`);    // ERROR
//console.log(`i: ${i}, type: ${typeof i}`);    // ERROR
console.log(`j: ${j}, type: ${typeof j}`);      // -> 5050 [string]
console.log(`k: ${k}, type: ${typeof k}`);      // -> 5050 [string]
console.log(`l: ${l}, type: ${typeof l}`);      // -> 50true [string]
console.log(`m: ${m}, type: ${typeof m}`);      // -> abc50 [string]
console.log(`n: ${n}, type: ${typeof n}`);      // -> abc50 [string]
console.log(`o: ${o}, type: ${typeof o}`);      // -> abctrue [string]

// TASK 6: Try to modify the line const str1 = 42 + "1"; to get the result 43 (without removing the quotes around 1).

const str1 = 42 + + "1"; 
console.log(str1); 