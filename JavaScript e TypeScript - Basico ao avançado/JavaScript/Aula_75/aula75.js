const objA = {
  chaveA: 'A',
};

const objB = {
  chaveB: 'B',
};

const objC = {
  chaveC: 'C',
};

Object.setPrototypeOf(objB, objA);
Object.setPrototypeOf(objC, objB);

console.log(objB.chaveA);
console.log(objC.chaveB);
