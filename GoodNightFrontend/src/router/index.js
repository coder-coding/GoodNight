import { createRouter, createWebHashHistory } from "vue-router";


const routes = [
    {
        path: '/index',
        component: () => import( /* webpackChunkName: "index" */ '../views/Index.vue'),
        children: [
            {
                name: 'Main',
                path: ':project',
                component: () => import( /* webpackChunkName: "main" */ '../views/Main.vue'),
                meta: {
                    title: 'Main',
                    keepAlive: true
                },
            },
        ],
    },
    // { path: '/about', component: About },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router