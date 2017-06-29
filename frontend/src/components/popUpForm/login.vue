<template>
    <div class="ui view">
        <div @click="$router.go(-1)" class="ui active dimmer"></div>
        <div class="ui login container">
            <form class="ui form">
                <div :class="text_class" class="ui text menu">
                    <div class="menu login">
                        登录
                    </div>
                        <div @click="$router.go(-1)" class="ui image close_right">
                            <img src="/static/image/close_icon2.png" alt="" />
                        </div>
                </div>
                <div v-if="errors" class="login-errors">
                    <div v-for="(error, name) in errors">
                        {{name}} : {{error[0]}}
                    </div>
                </div>
                <div class="ui divider"></div>
                <div class="ui view yellow_login"></div>

                <div class="field">
                    <input v-model='username' type="text"  placeholder="Username">
                </div>
                <div class="field">
                    <input v-model='password' type="password"  placeholder="Password">
                </div>
                <div class="inline field">
                    <div class="ui checkbox checked">
                        <input type="checkbox" tabindex="0">
                        <label>记住我</label>
                    </div>
                    <button class="ui button forget" type="submit">
                        忘记密码？
                    </button>
                </div>
            </form>
            <button v-on:click="LogIn" type="submit" class="ui circular right button" >
                登录
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
                text_class: '',
                username: '',
                password: '',
                errors: ''
            };
        },
        methods: {
            LogIn () {
                let self = this;
                reqwest({
                    url: 'http://localhost:8000/api/token-auth',
                    type: 'json',
                    method: 'POST',
                    data: {
                        username: self.username,
                        password: self.password
                    },
                    error (err) {
                        self.text_class = 'error';
                        self.errors = JSON.parse(err['response']);
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
        }
    };

</script>

<style>
    .ui.active.dimmer {
        position: fixed;
    }
    /*中间白色的背景*/
    .ui.login.container {
        width: 484px;
        height: 300px;
        border-radius: 10px;
        background-color: #ffffff;
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%,-50%);
        padding-left: 22px;
    /*    padding-right: 22px;*/
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
    .ui.text.menu > .ui.image.close_right {
        margin-left: 380px;
        margin-top: 0px;
    }

    /*黄色横线*/
    .ui.form > .ui.view.yellow_login {
        background-color: #fcc416;
        width: 100px;
        height: 5px;
        margin-top: -12px;
        margin-bottom: 18px;
    }
    /*分割线*/
    .ui.form > .ui.divider {
        width: 440px;
        margin-top: -18px;
        margin-bottom: 7px;
    }
    /*输入框*/
    .ui.form > .field {
        width: 440px;
        background-color: #ffffff;
    }

    .ui.form > .login-errors {
        display: block;
        position: absolute;
        top: 7%;
        color: darkred;
    }
    /*黄色的button */
    .ui.login.container > .ui.circular.right.button {
        margin-left: 320px;
        width: 120px;
        height: 40px;
        border-radius: 24px;
        background-image: url('/static/image/button.png');
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
        width: 120px;
        background-color: #ffffff;
        position: relative;
        text-align: center;;
        left: 40%;
        text-decoration: underline;
    }
</style>
