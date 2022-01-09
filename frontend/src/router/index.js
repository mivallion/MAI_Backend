import { createRouter, createWebHistory } from "vue-router";
import review from './review'

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Index',
            component: () => import('@/pages/Index.vue'),
        },
        {
            path: '/sign-in',
            name: 'SignIn',
            component: () => import('@/pages/SignIn.vue'),
        },
        {
            path: '/sign-up',
            name: 'SignUp',
            component: () => import('@/pages/SignUp.vue'),
        },
        ...review,
        {
            path: '/:pathMatch(.*)*',
            name: '404',
            component: () => import('@/pages/404.vue')
        },
    ]
})
