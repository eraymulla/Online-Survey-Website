<template>
  <div>
    <default-layout> </default-layout>
    <div class="userInformationSurveyContainer">
      <div class="userInformationSurveyRow">
        <div class="header">
          <h1>Hesap Bilgileri</h1>
        </div>
        <div class="row">
          <div class="col-md-6 userKolon">
            <!--Kalıcı yazılar-->
            <h4 class="mb-5">Kullanıcı Adı</h4>
            <h4 class="mb-5">Şifre</h4>
            <h4 class="mb-5">E-Mail</h4>
            <h4 class="mb-5">Telefon</h4>
          </div>
          <div
            class="col-md-6 userKolon"
            v-for="(user, index) in this.$store.state.mainPage.signedUser"
            :key="index"
          >
            <!--flasktan gelecek bilgiler-->
            <h4 class="mb-5">{{ user.name }}</h4>
            <h4 class="mb-5">{{ user.surname }}</h4>
            <h4 class="mb-5">{{ user.email }}</h4>
            <h4 class="mb-5">{{ user.phone }}</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import DefaultLayout from "./DefaultLayout.vue";
export default {
  components: { DefaultLayout },
  data() {
    return {
      name: null,
    };
  },

  methods: {},
};
</script>

<style  scoped>
.userInformationSurveyContainer {
  display: flex;
  justify-content: center;
  resize: both;
  overflow: auto;
}

.userInformationSurveyRow {
  padding: 30px;
  margin-top: 100px;
  margin-bottom: 150px;
  min-height: 36rem !important;
  width: 70rem;
  border-radius: 50px;
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;
}

.header {
  display: flex;
  justify-content: center;
  color: deepskyblue;
  margin-bottom: 3rem;
}
.userKolon {
  color: rgb(63, 151, 180);
}
.row {
  width: 90%;
  padding-left: 40px;
}
</style>