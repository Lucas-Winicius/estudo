const { html } = require("./base");

const regExp = /<.+>.+<\/.+>/g // greedy
const regExp2 = /<.+?>.+?<\/.+?>/g // non-greedy
console.log(html.match(regExp2))