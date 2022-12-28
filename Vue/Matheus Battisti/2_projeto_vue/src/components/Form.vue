<template>
  <form action="">
    <input type="text" v-model="nome"> <br>
    <input type="text" v-model="email">
    <input type="submit" value="Enviar" @click="enviarFormulario">
  </form>
  <p>{{ nome }} | {{ email }}</p>
</template>

<script>
import InputText from './InputText.vue';

export default {
  name: "Form",
  components: { InputText },
  data() {
    return {
      nome: null,
      email: null
    }
  },
  methods: {
    enviarFormulario(e) {
      e.preventDefault()

      const nome = this.nome
      const email = this.email

      console.log('Formulario Enviado')
      console.log('Nome: ' + nome)
      console.log('Email: ' + email)
    }
  }
};
</script>