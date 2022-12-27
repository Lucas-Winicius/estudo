<template>
    <p>Seja bem-vindo ( a ), {{ nome }}!</p>
    <input type="text" v-model="nomeLocal">
    <Paragrafo v-model:conteudo="nomeLocal" />
</template>

<script>
import Paragrafo from './Paragrafo.vue';

export default {
    name: 'Props',
    components: { Paragrafo },
    props: { nome: String },
    data() { return { nomeLocal: null } }
}
</script>