let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
}];

let n1 = prompt("Enter Name #1:");
let p1 = prompt("Enter Phone #1:");
let e1 = prompt("Enter Email #1:");

let n2 = prompt("Enter Name #2:");
let p2 = prompt("Enter Phone #2:");
let e2 = prompt("Enter Email #2:");

let obj1 = {
    name: n1,
    phone: p1,
    email: e1
}

let obj2 = {
    name: n2,
    phone: p2,
    email: e2
};

contacts.push(obj1, obj2);

let last = contacts.length - 1;

alert(`${contacts[0].name} ${contacts[0].phone} ${contacts[0].email}`);
alert(`${contacts[last].name} ${contacts[last].phone} ${contacts[last].email}`);

console.log(`${contacts[0].name} ${contacts[0].phone} ${contacts[0].email}`);
console.log(`${contacts[last].name} ${contacts[last].phone} ${contacts[last].email}`);