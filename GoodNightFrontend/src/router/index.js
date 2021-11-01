import { createRouter, createWebHashHistory } from "vue-router";
import { defineAsyncComponent } from "@vue/runtime-core";

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
    { path: '/', component: () => import( /* webpackChunkName: "index" */ '../views/Index.vue'), },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router