<template>
    <div class="ui view">
        <div @click="$router.go(-1)" class="ui active dimmer"></div>
        <div class="ui register container">
            <form class="ui form" method="post" action="register">
                <div :class="text_class" class="ui text menu">
                    <div class="menu login">
                        注册
                    </div>
                    <div @click="$router.go(-1)" class="ui image close_right">
                        <img src="/static/image/close_icon2.png" alt="" />
                    </div>
                </div>
                <div class="ui view yellow_login"></div>
                <div v-if="errors" class="login-errors">
                    <div v-for="(error, name) in errors">
                        {{name}} : {{error[0]}}
                    </div>
                </div>
                <div class="ui divider"></div>
                <div class="field">
                    <input type="text" v-model='email' name="email" placeholder="邮箱">
                </div>
                <div class="field">
                    <input type="text" v-model='username' name="username" placeholder="用户名">
                </div>
                <div class="field">
                    <input type="password" v-model='password' name="password" placeholder="密码">
                </div>
                <div class="field">
                    <input type="password" v-model='confirmed_password' name="confirmed_password" placeholder="重复密码">
                </div>
                <div class="captcha field">
                    <input type="text" v-model='captcha' class="captcha input" name="captcha">
                    <img :src="captcha_url" @click='flushCaptcha' v-cloak class="captcha image" alt="">
                </div>
            </form>
            <button @click="register" class="ui circular right button" >
                注册
                <i class="chevron inverted right icon"></i>
            </button>
        </div>
    </div>
</template>

<script>
    import Cookies from 'js-cookie';
    import reqwest from 'reqwest';
    export default {
        data () {
            return {
                username: '',
                password: '',
                email: '',
                confirmed_password: '',
                captcha: '',
                captcha_url: '',
                captcha_key: '',
                errors: ''
            };
        },
        methods: {
            flushCaptcha () {
                let self = this;
                reqwest({
                    url: 'http://localhost:8000/api/v1.0/new_captcha',
                    type: 'json',
                    method: 'get',
                    success (resp) {
                        console.log(resp);
                        self.captcha_url = 'http://127.0.0.1:8000' + resp.image;
                        self.captcha_key = resp.key;
                    }
                });
            },
            register () {
                let self = this;
                self.flushCaptcha();
                if (self.password === self.confirmed_password) {
                    reqwest({
                        url: 'http://localhost:8000/api/v1.0/created_user',
                        type: 'json',
                        method: 'post',
                        data: {
                            'username': self.username,
                            'password': self.password,
                            'confirmed_password': self.confirmed_password,
                            'email': self.email,
                            'captcha_0': self.captcha_key,
                            'captcha_1': self.captcha
                        },
                        error (err) {
                            self.errors = JSON.parse(err['response']);
                        },
                        success (resp) {
                            console.log(resp);
                            self.LogIn();
                        }
                    });
                }
            },
            LogIn () {
                let self = this;
                reqwest({
                    url: 'http://localhost:8000/api/v1.0/token-auth',
                    type: 'json',
                    method: 'POST',
                    data: {
                        username: self.username,
                        password: self.password
                    },
                    success (resp) {
                        console.log(resp);
                        console.log(self.username);
                        Cookies.set('token', resp.token);
                        Cookies.set('username', self.username);
                        self.$emit('login-success');
                        self.$router.go(-1);
                    }
                });
            }
        },
        mounted () {
            this.flushCaptcha();
        }
    };
</script>

<style>
    .ui.active.dimmer {
        position: fixed;
    }
    /*中间白色的背景*/
    .ui.view > .ui.register.container {
        width: 484px;
        height: 350px;
        border-radius: 10px;
        background-color: #ffffff;
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%,-50%);
        padding-left: 22px;
        padding-right: 18px;
        padding-top: 12px;
        z-index: 1001;

    }
    .ui.error.text.menu {
        margin-bottom: 10%;
        padding-bottom: 0;
    }
    /*登录*/
    .ui.text.menu > .menu.login {
        font-family: SourceHanSansSC-Normal;
        font-size: 20px;
        text-align: left;
        color: #4a4a4a;
        margin-left: 8px;
    }
    /*叉号按钮*/
    .ui.text.menu .ui.image.close_right {
        margin-left: 380px;
        margin-top: 0px;
    }

    /*黄色横线*/
    .ui.form > .ui.view.yellow_login {
        background-color: #8dc63f;
        width: 100px;
        height: 3px;
        margin-top: -20px;
    }
    /*分割线*/
    .ui.form > .ui.divider {
        width: 440px;
        margin-top: -18px;
    }
    /*错误提示*/
    .ui.form > .login-errors {
        display: block;
        position: absolute;
        top: 7%;
        color: darkred;
    }
    /*输入框*/
    .ui.form > .field {
        width: 440px;
        background-color: #ffffff;
    }
    /*验证码*/
    .ui.form > .captcha.field {
        position: absolute;
        width: 305px;
        background-color: #ffffff;
    }
    .ui.form > .captcha.field > .captcha.input {
        width: 140px;
        /*margin-left: 5px;*/
    }
    .ui.form > .captcha.field > .captcha.image {
        width: 77px;
        height: 33px;
        margin-left: 3px;
    }
    /*黄色的button */
    .ui.register.container > .ui.circular.right.button {
        margin-left: 320px;
        width: 120px;
        height: 40px;
        border-radius: 24px;
        background-image: url('/static/image/button_green.png');
        background-repeat: no-repeat;
        background-size: cover;
        font-size: 16px;
        color: #fff;
        padding-left: 20px;
    }
    /*保存修改*/
    .ui.circular.right.button > .chevron.inverted.right.icon {
        padding-left: 25px;
    }
    /*忘记密码*/
    .inline.field > .ui.button.forget {
        width: 130px;
        background-color: #ffffff;
        position: relative;
        text-align: right;
        left: 250px;
    }
</style>
