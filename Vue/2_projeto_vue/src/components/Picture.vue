<template>
    <img :src="link" :alt="descricao" :title="descricao">
</template>

<script>
export default {
    name: 'Picture',
    data() {
        return {
            link: 'https://www.pavilionweb.com/wp-content/uploads/2017/03/man-300x300.png',
            descricao: 'Avatar'
        }
    }
}
</script>