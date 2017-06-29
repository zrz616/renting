import Vue from 'vue';
// import App from '../App';
import index from '../page/index';
import list from '../page/list';
import login from '../components/popUpForm/login';
import register from '../components/popUpForm/register';
import Router from 'vue-router';
// import Hello from '@/components/Hello';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            component: index,
            children: [
                {
                    path: '/login',
                    component: login
                },
                {
                    path: '/register',
                    component: register
                }
            ]
        },
        {
            path: '/list/:school_name',
            // 传递参数必须命名
            name: 'list',
            component: list,
            children: [
                {
                    path: '/login',
                    component: login
                },
                {
                    path: '/register',
                    component: register
                }
            ]
        }
    ]
});
