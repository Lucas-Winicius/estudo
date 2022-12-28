<template>
    <p v-if="esta_trabalhando">Estou trabalhando no momento.</p>
    <p v-else>Estou em busca de novas oportunidades</p>
    <div>
        <button @click="show_Email">Mostrar Email</button>
    </div>
    <p v-show="exibir_email">Forma de contato: <a href="mailto:lucaslucas7@gmail.com" target="_blank">Lucasclucas7@gmail.com</a></p>
    <p>Ultilizo as seguintes tecnologias para o backend:</p>
    <ul>
        <li v-for="(technology, index) in backend_technologies" :key="index">{{ technology }}</li>
    </ul>
    <p>Ultilizo as seguintes linguagens no front-end:</p>
    <ul>
        <li v-for="lang in frontend_techonologies" :key="lang.id" v-text="lang.lang"></li>
    </ul>
    <p class="teste">Para acessar meu portifolio <a :href="meu_link">clique aqui</a></p>
</template>

<script>
export default {
    name: 'Info',
    data() {
        return {
            esta_trabalhando: false,
            exibir_email: false,
            meu_link: 'https://www.google.com',
            backend_technologies: [ 'Python', 'JavaScript', 'PHP' ],
            frontend_techonologies: [
                { id: 1, lang: 'HTML' },
                { id: 2, lang: 'CSS' },
                { id: 3, lang: 'VUE' },
            ]
        }
    },
    methods: {
        show_Email(e) {
            this.exibir_email = !this.exibir_email
            e.srcElement.textContent = this.exibir_email ? 'Ocultar Email' : 'Mostrar Email'
        }
    }
}
</script>