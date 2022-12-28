<template>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Projetos</a></li>
        <li><a href="#">Contato</a></li>
    </ul>    
</template>

<script>
export default {
    name: 'Header'
}
</script>

<style scoped>
ul {
    list-style: none;
    display: flex;
    flex-direction: row-reverse;
}

li {
    margin-right: 10px;

}

a {
    color: rgb(11, 151, 163);
    text-decoration: none;
    transition: .5s;
}

a:hover {
    color: turquoise;
}

</style>