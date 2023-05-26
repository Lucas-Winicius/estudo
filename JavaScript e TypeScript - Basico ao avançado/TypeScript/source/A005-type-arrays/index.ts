// Array<T> - T[]
function sumArgs(...args: number[]) {
  return args.reduce((a, b) => a + b);
}

function concatString(...args: string[]) {
  return args.join(" ");
}

console.log(sumArgs(1, 2, 3, 4));
console.log(concatString("Hello,", "TypeScript!"));
