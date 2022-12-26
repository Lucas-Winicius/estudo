<template>
    <p v-if="esta_trabalhando">Estou trabalhando no momento.</p>
    <p v-else>Estou em busca de novas oportunidades</p>
    <div>
        <button @click="show_Email">Mostrar Email</button>
    </div>
    <p v-show="exibir_email">Forma de contato: <a href="mailto:lucaslucas7@gmail.com" target="_blank">Lucasclucas7@gmail.com</a></p>
    <p>Ultilizo as seguintes tecnologias:</p>
    <ul>
        <li>Python</li>
        <li>JavaScript</li>
        <li>PHP</li>
    </ul>
    <p>Para acessar meu portifolio <a :href="meu_link">clique aqui</a></p>
</template>

<script>
export default {
    name: 'Info',
    data() {
        return {
            esta_trabalhando: false,
            exibir_email: false,
            meu_link: 'https://www.google.com'
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