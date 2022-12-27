<template>
  <Header />
  <PrimeiroComponente />
  <LifeCycle />
  <Pessoa />
  <Form />
  <Picture />
  <MultiplosEventos />
  <Props nome="Lucas Winicius" />
</template>

<script>
import PrimeiroComponente from "./components/PrimeiroComponente.vue";
import MultiplosEventos from "./components/MultiplosEventos.vue";
import LifeCycle from "./components/LifeCycle.vue";
import Picture from "./components/Picture.vue";
import Header from "./components/Header.vue";
import Pessoa from "./components/Pessoa.vue";
import Props from "./components/Props.vue";
import Form from "./components/Form.vue";

export default {
  components: {
    PrimeiroComponente,
    MultiplosEventos,
    LifeCycle,
    Picture,
    Pessoa,
    Header,
    Props,
    Form,
  },
  name: "App",
};
</script>

<style>

  body {
    background-color: whitesmoke;
    color: #333;
  }

  a {
    color: red;
  }

  .teste {
    background-color: rgb(129, 129, 129);
  }

</style>