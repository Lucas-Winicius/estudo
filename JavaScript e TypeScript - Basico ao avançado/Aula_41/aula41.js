const max = (x, y) => x > y ? x : y;

console.log(max(10, 5));
console.log(max(10, 15));

const maxOfArray = array => 
    array.reduce((maior, numeroAtual) => numeroAtual > maior ? numeroAtual : maior)

const array = [1000, 3, 10, 150, 30, 5, 7, 8, 22, 20, 200, 199, 11]
console.log(maxOfArray(array))