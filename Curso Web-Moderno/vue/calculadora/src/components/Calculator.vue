<template>
  <div class="calculatorr">
    <Display/>
    <Button/>
  </div>
</template>

<script>
import Display from './Display.vue';
import Button from './Button.vue';

export default {
    name: 'Calculator',
    components:  { Display, Button }
}
</script>

<style>
.calculator {
    height: 320px;
    width: 235px;
    border-radius: 5px;
    overflow: hidden;

    display: grid;
    grid-template-columns: repeat(4, 20%);
    grid-template-rows: 1fr repeat(5, 48px);
}
</style>