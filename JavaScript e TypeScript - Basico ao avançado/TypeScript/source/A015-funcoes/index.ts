type MapFunction = (item: string) => string;

function mapString(array: string[], cb: MapFunction): string[] {
  const newArray: string[] = [];

  for (let i = 0; i < array.length; i++) {
    newArray.push(cb(array[i]));
  }

  return newArray;
}

const stringsArray = [
  "lucas",
  "WInicius",
  "Leonardo",
  "Maria",
  "Pedro",
  "Brenda",
];

console.log(mapString(stringsArray, (item) => item.toUpperCase()));

export default 1;
