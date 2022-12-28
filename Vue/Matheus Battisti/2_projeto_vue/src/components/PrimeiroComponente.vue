<template>
  <h1>Olá Vue</h1>
  <p>Meu nome é: {{ nome }}, Trabalho como: {{ profissao }}</p>
</template>

<script>
export default {
  name: "PrimeiroComponente",
  data() {
    return { 
        nome: 'Lucas',
        profissao: 'Programador ( Estudante )'
     };
  },
};
</script>