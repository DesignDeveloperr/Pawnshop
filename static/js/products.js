Vue.component('product', {
    props: ['name', 'description', 'price', 'image', 'user', 'id', 'added'],
    data: function () {
        return {
            text: 'Добавить в корзину'
        }
    },
    template: `<div class="mt-4 bg-blue-100 p-2 rounded shadow">
                    <div class="flex">
                    <img class="shadow object-fill h-32 rounded" v-bind:src="image" alt="">
                        <div class="block my-auto ml-8">
                            <p class="text-gray-600 font-medium">{{ name }}</p>
                            <p class="text-gray-600">{{ description }}</p>
                            <p class="text-gray-600">Цена: {{ price }} рублей</p>
                            <p class="text-gray-600">Добавил: {{ user }}</p>
                        </div>
                    </div>
                    <button v-bind:class="buttonColor" v-on:click="add_to_cart" class="mt-2 focus:outline-none py-2 w-full rounded text-white">{{ text }}</button>
               </div>`,
    methods: {
        add_to_cart: async function() {
            if (!this.added) {
                let response = await fetch(`/cart/add/${this.id}/`)
                if (response.ok) {
                    let result = await response.json()
                    result.code === 'success' ? this.added = true : alert(result.msg)
                    await catalog.getCart()
                } else {
                    alert(error_message)
                }
                await catalog.getProducts()
            } else {
                alert('Товар уже добавлен в корзину')
            }
        }
    },
    computed: {
        buttonColor: function () {
            return this.added ? 'bg-green-500' : 'bg-blue-400 hover:bg-blue-500'
        }
    },
    mounted: function () {
        this.added ? this.text = 'Товар добавлен в корзину' : this.text = 'Добавить в корзину'
    },
    updated: function () {
        this.added ? this.text = 'Товар добавлен в корзину' : this.text = 'Добавить в корзину'
    }
})

Vue.component('cart', {
    props: ['name', 'price', 'id'],
    template: `<div class="p-2 bg-blue-100 rounded shadow mt-4 flex">
                    <p class="text-gray-800 my-auto">{{ name }}. {{ price }} рублей</p>
                    <button v-on:click="remove_from_cart" class="px-2 bg-red-500 rounded-full text-white shadow ml-auto focus:outline-none">X</button>
               </div>`,
    methods: {
        remove_from_cart: async function() {
            let response = await fetch(`/cart/remove/${this.id}/`)
            if (response.ok) {
                let result = await response.json()
                result.code === 'success' ? await catalog.getProducts() : alert(result.msg)
            } else {
                alert('Ошибка')
            }
        }
    }
})

const catalog = new Vue({
    el: '#products',
    delimiters: ['${', '}}'],
    data: {
        search: '',
        sorted: '',
        products: [],
        cart: []
    },
    mounted: async function() {
        this.products = await (await fetch(`/products/${this.getSearch()}/${this.getSort()}/`)).json()
        this.cart = await (await fetch('/cart/')).json()
    },
    methods: {
        getSearch: function () {
            return this.search === '' ? 'all' : this.search
        },
        getSort: function () {
            return this.sorted === '' ? 'all' : this.sorted
        },
        getProducts: async function () {
            this.products = await (await fetch(`/products/${this.getSearch()}/${this.getSort()}/`)).json()
            await this.getCart()
        },
        getCart: async function() {
            this.cart = await (await fetch('/cart/')).json()
        }
    }
})