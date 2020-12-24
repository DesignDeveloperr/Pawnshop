const login = new Vue({
    el: '#login_form',
    delimiters: ['${', '}}'],
    data: {
        email: '',
        password: '',
        message: ''
    },
    methods: {
        submit: async function() {
            let fd = new FormData()
            fd.append('email', this.email)
            fd.append('password', this.password)
            fd.append('csrfmiddlewaretoken', csrf_token)
            let response = await fetch(location.href, {
                method: 'POST',
                body: fd
            })
            if (response.ok) {
                let result = await response.json()
                return result.code === 'success' ? location.reload() : this.message = result.msg
            }
            else if (response.status === 403) {
                this.message = 'Ошибка проверки CSRF токена'
            } else {
                this.message = 'Ошибка'
            }
        }
    }
})