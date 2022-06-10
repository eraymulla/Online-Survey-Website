import { createStore } from "vuex";
import createPersistedState from 'vuex-persistedstate'
// import {Vuex} from 'Vue'
// import Vue from 'vue'
// Create a new store instance or import from module.

const mainPageModule = {
  namespaced: true,
  state: {
    signedUser: [],
    surveyInfo: [],
    emailList: [],
    deneme: 0,
  },
  mutations: {
    INCREASE_COUNT_MUT(state, payload) {
      console.log("mainPageModule increaseCountMutations worked")
      state.deneme++
      console.log("state.deneme :", state.deneme)
      console.log("payload :", payload)
    },
    SET_LOAD_DATA(state, payload) {
      console.log("mainPageModule setLoadData mutations worked, payload: ", payload)
      state.signedUser.push(payload)
      // dispatch('answerSurvey/loadData', state.signedUser[0].email)
      state.surveyInfo = payload.surveyData.map(e => { return e })
      console.log("state.surveyInfo: ", state.surveyInfo)
      console.log("state.signedUser: ", state.signedUser)
    },
    RESET(state) {
      console.log("mainPage reset mutations worked")
      state.signedUser = []
      console.log("mainPage Reset mutations state.signedUser: ", state.signedUser)
    },
    GET_EMAIL_LIST(state, payload) {
      console.log("payload: ", payload)
      state.emailList = payload.data.map(e => { return e })
      console.log("getEmailList mutations worked. state.emailList: ", state.emailList)
    }
  },
  actions: {
    increaseCount({ commit }, payload) {
      console.log("mainPageModule increaseCount actions worked")
      commit("INCREASE_COUNT_MUT", payload)
    },
    loadData({ commit }, payload) {
      console.log("mainPageModule loadData actions worked")
      commit('SET_LOAD_DATA', payload)
    },
    resetState({ commit }) {
      commit('RESET')
    },
    getEmailList({ commit }, payload) {
      console.log("getEmailList actions worked")
      const axios = require("axios");
      let _url = payload;
      const config = {
        method: "get",
        url: _url,
        headers: {
          "Content-Type": "application/json",
        },
      };
      let respData;
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
          respData = response.data;
          console.log(".then respData : ", respData);
        })
        .catch(function (error) {
          console.log(error);
        })
        .finally(() => {
          commit('GET_EMAIL_LIST', respData)
        });

    }
  }
}

const createSurveyModule = {
  namespaced: true,
  state: {
    survey: [],
    deneme: 0,
  },
  mutations: {
    INCREASE_COUNT_MUT(state, payload) {
      console.log("createSurveyModule increaseCountMutations worked")
      state.deneme++
      console.log("state.deneme :", state.deneme)
      console.log("payload :", payload)
    }
  },
  actions: {
    increaseCount({ commit }, payload) {
      console.log("createSurveyModule increaseCount actions worked")
      commit("INCREASE_COUNT_MUT", payload)
    }
  }
}

//HAZIR OLAN ANKETLERİN GÖZÜKECEĞİ MODÜL
const answerSurveyModule = {

  namespaced: true,
  state: {

  },
  mutations: {
    LOAD_DATA() {
      console.log("LOAD_dATA WORKED")
    }
  },
  actions: {
    loadData({ commit }, payload) {
      console.log("answerSurvey loadData actions worked", payload)

      console.log("getEmailList actions worked")
      const axios = require("axios");
      let _url = payload.url;
      let data = {
        surveyId: payload.index,
        email: payload.email
      }
      const config = {
        method: "post",
        url: _url,
        data: data,
        headers: {
          "Content-Type": "application/json",
        },
      };
      let respData;
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
          respData = response.data;
          console.log(".then respData : ", respData);
        })
        .catch(function (error) {
          console.log(error);
        })
        .finally(() => {

          commit("LOAD_DATA", payload.index)
        });


    }
  }
}

const store = createStore({
  modules: {
    mainPage: mainPageModule,
    createSurvey: createSurveyModule,
    answerSurvey: answerSurveyModule
  },
  plugins: [createPersistedState()]
});

// new Vue({
//   store,
//   computed: {
//     ...Vuex.mapState({
//       mainPage: state => state.mainPage,
//       createSurvey: state => state.createSurvey
//     })
//   },
//   methods: {
//     increaseCount(payload) {
//       this.$store.dispatch("mainPage/increaseCount", payload);
//     },
//     increaseCount(payload) {
//       this.$store.dispatch("createSurvey/increaseCount", payload);
//     }
//   }
// });

export default store;