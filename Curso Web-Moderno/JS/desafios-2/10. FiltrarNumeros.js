const filtrarNumeros = array => console.log(array.filter(a => a * 0 == 0 ))

filtrarNumeros(["Javascript", 1, "3", "Web", 20]) // retornarĂ¡ [1, 20]
filtrarNumeros(["a", "c"]) // retornarĂ¡ []