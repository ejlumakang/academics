// Create a Java script program that let the user enter for a number, then the user will input integers based on the inputted number. The program will count the number of even, odd and zero numbers from the user's input. (use Loops).

let num = prompt("Enter a number:");
let oddCount = 0;
let evenCount = 0;
let zeroCount = 0;

for (let i = 1; i <= num; i++) {
    let userInput = Number(prompt("Input number " + i + ":"));
    if (userInput === 0) {
        zeroCount++;
    } else if (userInput % 2 === 0) {
        evenCount++;
    } else {
        oddCount++;
    }
}

let display = "\n" + "EVEN Count: " + evenCount + "\n" + "ODD Count: " + oddCount + "\n" + "ZERO Count: " + zeroCount;
console.log(display);