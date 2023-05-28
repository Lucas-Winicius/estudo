let x: unknown;
const y = 800;
x = 100;
x = "100";
x = 100;

if (typeof x === "number") console.log(x + y);
