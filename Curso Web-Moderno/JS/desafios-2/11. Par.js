const receberSomenteOsParesDeIndicesPares = lista => console.log( lista.filter((n, i, a) => Number(n) % 2 == 0 && i % 2 == 0))

receberSomenteOsParesDeIndicesPares([1, 2, 3, 4]) // retornarĂ¡ []
receberSomenteOsParesDeIndicesPares([10, 70, 22, 43]) // retornarĂ¡ [10, 22]
