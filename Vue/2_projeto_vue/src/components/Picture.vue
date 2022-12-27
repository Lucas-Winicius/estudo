<template>
    <img :src="link" :alt="descricao" :title="descricao" >
    <MudarImagem @mudar-imagem="trocarImagem" />
</template>

<script>
import MudarImagem from './MudarImagem.vue';

export default {
    name: 'Picture',
    components: { MudarImagem },
    data() {
        return {
            link: 'https://www.pavilionweb.com/wp-content/uploads/2017/03/man-300x300.png',
            descricao: 'Avatar'
        }
    },
    methods: {
        trocarImagem() {
            this.link = 'https://cdn.iconscout.com/icon/free/png-256/avatar-370-456322.png'
        }
    }
}
</script>

<style>
img {
    height: 300px;
}
</style>