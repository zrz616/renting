import Vue from 'vue';
// import App from '../App';
import login from '../components/popUpForm/login';
import register from '../components/popUpForm/register';
import Router from 'vue-router';
// import Hello from '@/components/Hello';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/login',
            component: login
        },
        {
            path: '/register',
            name: 'register',
            component: register
        }
    ]
});
