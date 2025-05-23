let rosePrice = 8;
let lilyPrice = 10;
let tulipPrice = 2;
let sampaguitaPrice = 5;
let gerberaPrice = 25;

let numberOfRoses = 70;
let numberOfLilies = 50;
let numberOfTulips = 120;
let numberofSampaguitas = 20;
let numberofGerberas = 24;

let rosesValue = rosePrice * numberOfRoses;
let liliesValue = lilyPrice * numberOfLilies;
let tulipsValue = tulipPrice * numberOfTulips;
let sampaguitasValue = sampaguitaPrice * numberofSampaguitas;
let gerberasValue = gerberaPrice * numberofGerberas;

let total = rosesValue + liliesValue + tulipsValue + sampaguitasValue + gerberasValue;

console.log("Rose - unit price:", rosePrice, "quantity:", numberOfRoses,  "value:", rosesValue);
console.log("Lily - unit price:", lilyPrice, "quantity:", numberOfLilies,  "value:", liliesValue);
console.log("Tulip - unit price:", tulipPrice, "quantity:", numberOfTulips,  "value:", tulipsValue);
console.log("Sampaguita - unit price:", sampaguitaPrice, "quantity:", numberofSampaguitas,  "value:", sampaguitasValue);
console.log("Gerbera - unit price:", gerberaPrice, "quantity:", numberofGerberas,  "value:", gerberasValue);
console.log("Total: ", total);