<template>
    <button @click="primeiro('Primeiro', $event), segundo('Segundo', $event)">Ativar múltiplos eventos</button>
    <p>{{ multiplos_eventos }}</p>
</template>

<script>
export default {
    name: 'MultiplosEventos',
    data() {
        return {
            multiplos_eventos: null
        }
    },
    methods: {
        primeiro(txt, e) {
            this.multiplos_eventos = txt + ' evento'
        },
        segundo(txt, e) {
            setTimeout(() => {this.multiplos_eventos = txt + ' evento'}, 1000)
        }
    }
}
</script>