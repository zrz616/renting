<template>
    <div>
        <router-view @login-success="authenticate"></router-view>
        <div class="ui vertical banner segment ">
        <div class="ui menu header">
            <div class="left menu">
                <div class="ui image" style="padding-top:10px;">
                    <img src="/static/image/logo.png" alt="" />
                </div>
                <div class="ui inverted logo" style="margin:24px 0 0 10px;font-style:normal;font-family:Microsoft YaHei;color: white;font-size: 26px;">
                    校园租
                </div>
            </div>
            <div class="rigt menu">
                <div class="ui vertical login" style="margin-top:25px;">
                    <router-link to="/login" style="color:rgb(255, 255, 255);font-size=18px;">登录</router-link>
                </div>
                <button type="button" name="button" class="ui circular yellow button">
                    <router-link to="/register">
                        <div>
                            <img style="height:20px; " src="/static/image/key_icon.png" alt="" />
                            <div class="visible content" style="color: #654303;">注册</div>
                        </div>
                    </router-link>
                </button>

            </div>
        </div>
        <div class="ui header">
            <h2>北京大学搜索结果 - 43个房源</h2>
        </div>
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
            // 通过Cookies判断是否已登录
            authenticate () {
                this.login_user = Cookies.get('username');
                if (Cookies.get('username')) {
                    this.is_login = true;
                };
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

<style scoped>
    .ui.vertical.segment.banner{
        width: 100%;
        height: 228px;
        background-image: url(/static/image/banner_bg.png);
        background-size: cover;
        background-repeat: no-repeat;
        position: absolute;
        left:50%;
        transform: translate(-50%);

    }

    .ui.menu.header{
        position: absolute;
        top:0px;
        margin-top: 0px;
        height: 70px;
        width:100%;
        background:white; background:rgba(0,0,0,0.2) none repeat scroll !important;
        padding-left: 17.5%;
        padding-right: 17.5%;
    }


    .ui.vertical.login{
        font-style:normal;
        font-family:Microsoft YaHei;
        color: white;
        font-size: 16px;
    }


    .ui.circular.yellow.button{
        height:33px;
        width: 100px;
        margin:20px 0 0 10px;
        padding: 4px 0 0 0;
        font-style:normal;
        font-family:Microsoft YaHei;
        font-size: 16px;
        color: rgb(11, 11, 11);
    }

    .ui.header{
        position: absolute;
        top:80px;
        padding-left: 268px;
        font-style:normal;
        font-family:Microsoft YaHei;
        font-size: 5px;
        color: rgb(255, 255, 255);
    }
</style>
