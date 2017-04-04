<template>
    <div>
        <v-login :active="login_window_status" @switch-login-active="closeLoginWindow" @login-success="authenticate"></v-login>
        <v-register :active="register_window_status" @switch-register-active="closeRegisterWindow" @register-success="authenticate"></v-register>
        <div class="ui vertical basic segment banner">
            <!-- - - - - - - - - - - - - masterhead - - - - - - - - - - - - -->
            <div class="ui vertical segment masterhead">
                <div class="ui vertical segment masterhead">
                    <div class="ui text menu in-masterhead">
                        <!-- CampusRenting logo-image -->
                        <a class="image-logo in-menu-masterhead" href="#">
                            <img src="/static/image/租房项目切图/1首页/logo.png" alt="" />
                        </a>
                        <!-- CampusRenting logo-text -->
                        <a class="text-logo in-menu-masterhead" href="#">校园租</a>
                        <!-- right menu -->
                        <div v-if='is_login' v-cloak class="ui right text menu in-menu-masterhead">
                            <a class="text-login in-menu-masterhead">
                                {{ login_user }}
                            </a>
                            <div v-on:click='logout' class="ui circular button in-menu-masterhead">
                                <span class="text-register in-menu-masterhead">注销</span>
                            </div>
                        </div>
                        <div v-else v-cloak class="ui right text menu in-menu-masterhead">
                            <!-- login -->
                            <router-link to="/login" @click="popLoginWindow" class="text-login in-menu-masterhead">登录</router-link>
                            <!-- register button -->
                            <router-link to="/register" @click="popRegisterWindow" class="ui circular button in-menu-masterhead">
                                <img class="image-key in-menu-masterhead" src="/static/image/租房项目切图/1首页/key_icon.png" alt="" />
                                <span class="text-register in-menu-masterhead">注册</span>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
            <v-search></v-search> 
        </div>
    </div>
</template>

<script>
    import Cookies from 'js-cookie';
    import login from '../popUpForm/login';
    import register from '../popUpForm/register';
    import search from './search';
    export default {
        data () {
            return {
                login_window_status: false,
                register_window_status: false,
                is_login: false,
                login_user: ''
            };
        },
        methods: {
            authenticate () {
                this.login_user = Cookies.get('username');
                if (Cookies.get('username')) {
                    this.is_login = true;
                };
            },
            popLoginWindow () {
                this.login_window_status = true;
            },
            closeLoginWindow () {
                this.login_window_status = false;
            },
            popRegisterWindow () {
                this.register_window_status = true;
            },
            closeRegisterWindow () {
                this.register_window_status = false;
            },
            logout () {
                Cookies.remove('token');
                Cookies.remove('username');
                this.is_login = false;
            }
        },
        mounted () {
            this.authenticate();
        },
        components: {
            'v-login': login,
            'v-register': register,
            'v-search': search
        }
    };
</script>

<style>
    .ui.vertical.basic.segment.banner {
        height: 689px;
        background-image: url('/static/image/租房项目切图/1首页/cover_beautified.png');
        background-size: cover;
        background-repeat: no-repeat;
        padding: 0;
        margin: 0;
        /*note: search "缩小窗口时CSS背景图出现右侧空白" for more info*/
        /*width:expression(document.body.clientWidth <= 960? "960px": "auto");
        min-width:960px;*/
    }
    /*---------------------------------masterhead---------------------------------*/
    .ui.vertical.segment.masterhead {
        height: 75px;
        background-color: rgba(0, 0, 0, 0.2);
        padding: 0;
        margin: 0;
    }

    .ui.text.menu.in-masterhead {
        height: 75px;
        padding: 0;
        margin: 0;
    }

    .image-logo.in-menu-masterhead {
        margin: 15px 9px 22px 13%;
    }

    .text-logo.in-menu-masterhead {
        min-width: 84px;
        /*font-family: "webfont" !important;*/
        font-size: 28px;
        /*font-style: normal;
        -webkit-font-smoothing: antialiased;
        -webkit-text-stroke-width: 0.2px;
        -moz-osx-font-smoothing: grayscale;*/
        color: #ffffff;
        padding-top: 12px;
        /*note: margin-left of text is better to be auto or 0*/
        margin: 19px auto 15px 0;
    }

    .ui.right.text.menu.in-menu-masterhead {
        height: 33px;
        padding: 0;
        margin: 20px 13% 22px 584px;
    }

    .text-login.in-menu-masterhead {
        min-width: 32px;
        font-size: 16px;
        color: #ffffff;
        padding-top: 6px;
        /*note: margin-left of text is better to be auto or 0*/
        margin: 0 auto 0 0;
    }

    .ui.circular.button.in-menu-masterhead {
        background-color: #fcc416;
        width: 112px;
        height: 33px;
        padding: 0;
        margin: 0 0 0 30px;
    }

    .image-key.in-menu-masterhead {
        /*note: see note for padding-bottom in .text-register.in-menu-masterhead*/
        margin: 6px 13px -4px 0;
    }

    .text-register.in-menu-masterhead {
        min-width: 32px;
        font-size: 16px;
        color: #654303;
        /*note: padding-bottom is not applied because of the image-key.
        Change margin-bottom of image-key and it will be seen.*/
        /*padding-bottom: 12px;*/
        /*note: margin-left of text is better to be auto or 0*/
        margin: 5px auto 5px 0;
        /*note1: margin-top/bottom is not applicable for inline elements like span.
        Make span display: inline-block so that it can be inline as well as block.*/
        /*note2: display is not necessay as the padding-bottom is not applied.
        see above note for padding-bottom.*/
        /*display: inline-block;*/
    }
</style>
