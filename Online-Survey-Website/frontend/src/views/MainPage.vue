<template>
  <div>
    <default-layout></default-layout>
    <!--Anketlerin küçük şekilde görüneceği component-->
    <div style="font-size: 30px; margin-left: 4rem; color: white">
      Sayın {{ this.$store.state.mainPage.signedUser[0].name }}
      {{ this.$store.state.mainPage.signedUser[0].surname }} Hoşgeldiniz
    </div>
    <div class="row surveyCompRow">
      <div
        class="surveyComponentRow"
        v-for="(survey, index) in this.$store.state.mainPage.surveyInfo"
        :key="index"
      >
        <router-link to="/main-page">
          <div  @click="findIndex(index+1)" class="oneComponent">
            <h3 class="surveyName">{{ survey.surveyName }}</h3>
            <p class="surveyDescription">{{ survey.surveyDescription }}</p>
          </div>
        </router-link>
      </div>
    </div>
    <shooting-star> </shooting-star>
  </div>
</template>

<script>
/* eslint-disable */
import DefaultLayout from "../components/DefaultLayout.vue";
import ShootingStar from "../components/ShootingStar.vue";

export default {
  data() {
    return {
      urlGetEmailList: "http://127.0.0.1:5000/getParticipants",
      urlGetSurveyParticipants: "http://127.0.0.1:5000/getSurveyParticipants"
    };
  },
  created() {
    console.log("created worked");
    this.$store.dispatch('mainPage/getEmailList', this.urlGetEmailList)
  },
  methods: {
    findIndex(payload) {
      console.log("index: ",payload)
      this.$store.dispatch("answerSurvey/loadData",{index:payload, url:this.urlGetSurveyParticipants})
    },
  },
  components: { DefaultLayout, ShootingStar },
};
</script>

<style lang="scss" scoped>
.surveyComponentContainer {
  display: flex;
  justify-content: center;
  resize: both;
  overflow: auto;
}
.surveyName {
  white-space: pre-line;
}
.surveyComponentRow {
  margin: 100px !important;
  padding: 30px;
  margin-top: 100px;
  margin-bottom: 150px;
  min-height: 10rem !important;
  width: 15rem;
  display: flex !important;
  border-radius: 50px;
  /* background: linear-gradient(145deg, #112c4d, #13141d); */
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;
}
.oneComponent {
  color: deepskyblue;
}
/*NAVBAR STYLE*/
.btnMainPage {
  height: 3rem;
  border: 1px solid deepskyblue;
  background: transparent;
  color: rgb(123, 217, 249);
  font-weight: bold;
  position: relative;
  cursor: pointer;
  margin-right: 55px;
  &::before {
    content: "";
    width: 40px;
    height: 40px;
    position: absolute;
    border: inherit;
    transition: 0.5s ease;
    left: -15px;
    top: -15px;
    border-width: 1px 0 0 1px;
  }
  &::after {
    content: "";
    width: 40px;
    height: 40px;
    position: absolute;
    border: inherit;
    transition: 0.5s ease;
    right: -15px;
    bottom: -15px;
    border-width: 0 1px 1px 0;
  }
  &:hover {
    &::after {
      width: calc(100% + 27px);
      height: calc(100% + 27px);
    }
    &::before {
      width: calc(100% + 27px);
      height: calc(100% + 27px);
    }
  }
}
.nav {
  display: flex;
  justify-content: center;
  align-items: center !important;
  background: radial-gradient(ellipse at bottom, #0d1d31 30%, #0c0d13 100%);
  box-shadow: 0 0 3px rgb(0, 191, 255), 0 0 15px rgb(0, 110, 147);
  min-height: 100px;
}
.navHeader {
  font-size: xx-large !important;
  padding-left: 4rem;
}
.navItems {
  padding-right: 4rem;
  font-size: medium !important;
  justify-content: end !important;
}
.navItem {
  margin-right: 40px !important;
}
a {
  margin-right: 45px !important;
  color: #7cdcffce;
  text-decoration: none;
}
img {
  &:hover {
    text-shadow: 0 0 20px rgb(193, 224, 235), 0 0 20px rgb(0, 110, 147);
  }
}
.mainDropDown {
  border-color: #7cdcffce;
  border-radius: 15px;
  color: #7cdcffce;
  background-color: transparent !important;
  margin: 25px 0px 0px 150px !important;
}
.mainDropdownItem {
  color: white;
  &:hover {
    color: white;
    background-color: #7cdcffce;
  }
}
.input-group {
  width: 20%;
}
.surveyComp {
  margin-left: 50px !important;
}
</style>