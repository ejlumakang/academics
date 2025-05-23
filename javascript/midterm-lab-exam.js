let items = [
    {
        product: "Nutella",
        quantity: 3,
        price: 500
    },
    {
        product: "Gummy Bears",
        quantity: 4,
        price: 100
    }
];

let p1 = prompt("Enter PRODUCT name:", "Pringles"),
    q1 = parseInt(prompt("Enter QUANTITY of product:", 3)),
    pr = parseInt(prompt("Enter PRICE of product:", 150));
    
let p2 = prompt("Enter PRODUCT name:", "Cupcake"),
    q2 = parseInt(prompt("Enter QUANTITY of product:", 4)),
    pr2 = parseInt(prompt("Enter PRICE of product:", 75));

let obj1 = {
    product: p1,
    quantity: q1,
    price: pr
};
let obj2 = {
    product: p2,
    quantity: q2,
    price: pr2
};

items.push(obj1, obj2);

let totalAmountDue = 0;
let output = "";

output += "Product / Quantity / Price / Total";

output += `\n${items[0].product}  Ð  ${items[0].quantity}  Ð  ${items[0].price}  Ð  ${items[0].quantity * items[0].price}\n`
output += `${items[1].product}  Ð  ${items[1].quantity}  Ð  ${items[1].price}  Ð  ${items[1].quantity * items[1].price}\n`
output += `${items[2].product}  Ð  ${items[2].quantity}  Ð  ${items[2].price}  Ð  ${items[2].quantity * items[2].price}\n`
output += `${items[3].product}  Ð  ${items[3].quantity}  Ð  ${items[3].price}  Ð  ${items[3].quantity * items[3].price}\n`

totalAmountDue += items[0].quantity * items[0].price;
totalAmountDue += items[1].quantity * items[1].price;
totalAmountDue += items[2].quantity * items[2].price;
totalAmountDue += items[3].quantity * items[3].price;

output += "Total Amount Due: " + totalAmountDue;

alert(output);