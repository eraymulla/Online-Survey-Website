import { createRouter, createWebHashHistory } from "vue-router";

const routes =
    [
        {
            path: '/',
            component: () => import('@/views/HomePage')
        },
        {
            path: '/main-page',
            component: () => import("@/views/MainPage")
        },
        {
            path: '/forget-password',
            component: () => import("@/components/ForgetPassword")
        },
        {
            path: '/sign-in',
            component: () => import("@/components/SignIn")
        },
        {
            path: '/sign-up',
            component: () => import("@/components/SignUp")
        },{
            path: '/show-survey',
            component: () => import("@/components/ShowSurvey")
        }
        // {
        //     path: "*",
        //     redirect: "/404"
        // },
    ]

const router = createRouter({
    routes,
    history: createWebHashHistory()
})

export default router;