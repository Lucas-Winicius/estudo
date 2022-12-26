<template>
    <h2>Esta e a descrição da pessoa: {{ nome }}</h2>
    <Info />
</template>

<script>
import Info from './Info.vue';

export default {
    name: "Pessoa",
    components: { Info },
    data() {
        return {
            nome: "Lucas"
        };
    },
}
</script>