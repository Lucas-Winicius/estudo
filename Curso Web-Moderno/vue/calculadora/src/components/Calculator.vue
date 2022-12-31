<template>
  <div class="calculator">
    <display-vue value="1100"/>
    <button-vue label="AC" triple/>
    <button-vue label="/" operation/>
    <button-vue label="7"/>
    <button-vue label="8"/>
    <button-vue label="9"/>
    <button-vue label="*" operation/>
    <button-vue label="4"/>
    <button-vue label="5"/>
    <button-vue label="6"/>
    <button-vue label="-" operation/>
    <button-vue label="1"/>
    <button-vue label="2"/>
    <button-vue label="3"/>
    <button-vue label="+" operation/>
    <button-vue label="0" double/>
    <button-vue label="."/>
    <button-vue label="=" operation/>
  </div>
</template>

<script>
import DisplayVue from './Display.vue';
import ButtonVue from './Button.vue';

export default {
    name: 'CalculatorContainer',
    components:  { DisplayVue, ButtonVue }
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