String.prototype.reverse = function() {
    return this.split('').reverse().join('')
}

console.log('arobobA'.reverse())

Array.prototype.first = function() {
    return this[0]
}

console.log(['A', 'b', 'o', 'b', 'o', 'r', 'a'].first())