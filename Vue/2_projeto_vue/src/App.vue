<template>
  <PrimeiroComponente />
  <LifeCycle />
  <Pessoa />
  <Form />
  <Picture />
</template>

<script>
import PrimeiroComponente from "./components/PrimeiroComponente.vue";
import LifeCycle from "./components/LifeCycle.vue";
import Pessoa from "./components/Pessoa.vue";
import Form from "./components/Form.vue";
import Picture from "./components/Picture.vue";

export default {
  components: {
    PrimeiroComponente,
    LifeCycle,
    Picture,
    Pessoa,
    Form,
  },
  name: "App",
};
</script>