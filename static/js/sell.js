const sell = new Vue({
    el: '#sell_form',
    delimiters: ['${', '}}'],
    data: {
        name: '',
        description: '',
        price: null,
        message: '',
        error: true
    },
    methods: {
        submit: async function() {
            let fd = new FormData()
            fd.append('name', this.name)
            fd.append('description', this.description)
            fd.append('price', parseInt(this.price))
            fd.append('image', document.getElementById('image').files[0])
            fd.append('csrfmiddlewaretoken', csrf_token)
            let response = await fetch(location.href, {
                method: 'POST',
                body: fd
            })
            if (response.ok) {
                let result = await response.json()
                result.code === 'success' ? this.reset_form(result.msg) : this.error_text(result.msg)
            } else if (response.status === 403) {
                this.error_text(csrf_error)
            } else {
                this.error_text(error_message)
            }
        },
        reset_form: function (message) {
            this.success_text(message)
            this.name = ''
            this.description = ''
            this.price = null
        },
        success_text: function (message) {
            this.message = message
            this.error = false
        },
        error_text: function (message) {
            this.message = message
            this.error = true
        }
    },
    computed: {
        color_message: function () {
            return this.error ? 'text-red-600' : 'text-green-500'
        }
    }
})