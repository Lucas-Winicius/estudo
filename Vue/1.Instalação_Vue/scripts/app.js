const myNameApp = {
    data() {
        return {
            inputName: '',
            name: 'Lucas',
            age: 15
        }
    },
    methods: {
        submitForm(e) { e.preventDefault() }
    }
}

Vue.createApp(myNameApp).mount('#app')