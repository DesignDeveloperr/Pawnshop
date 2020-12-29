const register = new Vue({
    el: '#register_form',
    delimiters: ['${', '}}'],
    data: {
        name: '',
        surname: '',
        email: '',
        password: '',
        password_reply: '',
        message: ''
    },
    methods: {
        submit: async function() {
            let fd = new FormData()
            fd.append('name', this.name)
            fd.append('surname', this.surname)
            fd.append('email', this.email)
            fd.append('password', this.password)
            fd.append('password_reply', this.password_reply)
            fd.append('csrfmiddlewaretoken', csrf_token)
            let response = await fetch(location.href, {
                method: 'POST',
                body: fd
            })
            if (response.ok) {
                let result = await response.json()
                result.code === 'success' ? location.reload() : this.message = result.msg
            } else if (response.status === 403) {
                this.message = csrf_error
            } else {
                this.message = error_message
            }
        }
    }
})