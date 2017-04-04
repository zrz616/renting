<template>
    <div v-show=copyActive class="ui view">
        <div @click="switchWindow" class="ui active dimmer"></div>
        <div class="ui login container">
            <form class="ui form">
                <div class="ui text menu">
                    <div class="menu login">
                        登录
                    </div>
                    <div @click="switchWindow" class="ui image close_right">
                        <img src="/static/image/close_icon2.png" alt="" />
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
        props: ['active'],
        data () {
            return {
                copyActive: this.active,
                username: '',
                password: ''
            };
        },
        methods: {
            switchWindow () {
                this.copyActive = !this.copyActive;
                this.$emit('switch-active');
            },
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
                    success (resp) {
                        console.log(resp);
                        console.log(self.username);
                        Cookies.set('token', resp.token);
                        Cookies.set('username', self.username);
                        self.$emit('login-success');
                        self.copyActive = false;
                    }
                });
            }
        },
        watch: {
            active (val) {
                if (this.active === true) {
                    this.copyActive = val;
                }
            },
            copyActive (val) {
                if (this.copyActive === false) {
                    this.$emit('switch-login-active');
                }
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
        left: 250px;
        text-decoration: underline;
    }
</style>
