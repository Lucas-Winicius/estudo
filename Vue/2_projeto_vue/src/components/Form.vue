<template>
  <form action="">
    <InputText />
    <InputText />
    <input type="submit" value="Enviar">
  </form>
</template>

<script>
import InputText from './InputText.vue';

export default {
  name: "Form",
  components: { InputText }
};
</script>