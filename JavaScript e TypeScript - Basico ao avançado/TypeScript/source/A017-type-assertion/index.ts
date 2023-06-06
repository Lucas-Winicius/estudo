// const body = document.querySelector("body");
// body?.style.backgroundColor = "red";

// Non-null assertion (!)
// const body = document.querySelector("body")!;
// body?.style.backgroundColor = "red";

// Type assertion
const body = document.querySelector("body") as HTMLBodyElement;
body.style.backgroundColor = "red";
