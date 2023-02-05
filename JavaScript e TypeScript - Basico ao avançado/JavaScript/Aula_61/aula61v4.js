function* geradora5() {
    yield function() {
        console.log('Vim do y1')
    }

    // ...

    yield function() {
        console.log('Vim do y2')
    }

}

const g5 = geradora5()
g5.next().value()
g5.next().value()