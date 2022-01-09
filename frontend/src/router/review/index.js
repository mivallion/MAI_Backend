export default [
    {
        path: '/cat/:cat_id',
        name: 'Cat',
        component: () => import('@/pages/Cat.vue'),
    },
    {
        path: '/user/:user_id',
        name: 'User',
        component: () => import('@/pages/User.vue'),
    },
    {
        path: '/review/:review_id',
        name: 'Review',
        component: () => import('@/pages/Review.vue')
    }
]
