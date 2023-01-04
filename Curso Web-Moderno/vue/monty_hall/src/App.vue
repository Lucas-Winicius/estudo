<template>
  <div id="app">
    <h1>Problema de Monty Hall</h1>
    <door-component-vue number="1" has-gift="false" />
  </div>
</template>

<script>
import DoorComponentVue from './components/DoorComponent.vue';

export default {
  name: 'App',
  components: { DoorComponentVue }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Montserrat', sans-serif;
}

body {
  color: white;
  background-image: linear-gradient(100deg, rgb(21, 153, 87), rgb(21, 87, 153));
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
}

#app h1 {
  border: 1px solid #000;
  background-color: #0004;
  padding: 20px;
  margin-bottom: 60px;
}
</style>