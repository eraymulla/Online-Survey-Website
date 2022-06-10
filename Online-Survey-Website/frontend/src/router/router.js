import { createRouter, createWebHashHistory } from "vue-router";

const routes =
    [
        {
            path: '/',
            component: () => import('@/views/HomePage')
        },
        {
            path: '/main-page',
            name:"main",
            component: () => import("@/views/MainPage")
        },
        {
            path: '/forget-password',
            name:"forget-password",
            component: () => import("@/components/ForgetPassword")
        },
        {
            path: '/sign-in',
            name:"sign-in",
            component: () => import("@/components/SignIn")
        },
        {
            path: '/sign-up',
            name:"sign-up",
            component: () => import("@/components/SignUp")
        },
        {
            path: '/show-survey',
            name:"show-survey",
            component: () => import("@/components/ShowSurvey")
        },
        {
            path: '/create-survey',
            name:"create-survey",
            component: () => import("@/components/ShowAdminSurvey")
        },
        {
            path: '/user-informations',
            name:"user-informations",
            component: () => import("@/components/UserInformations")
        },
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