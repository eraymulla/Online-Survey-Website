<template>
  <div>
    <default-layout> </default-layout>
    <!-- Adminin soruları ve cevapları ekleyeceği komponent-->
    <div class="adminSurveyContainer">
      <div class="adminSurveyRow">
        <div
          class=""
          v-for="(email, index) in this.$store.state.mainPage.emailList"
          :key="index"
        >
          <div v-if="isAddParticipant" style="font-size: 45px; color: white" class="email-list">
            <li>{{ email.email }}</li>
          </div>
        </div>

        <div v-if="!isAddParticipant" class="adminSurveyCol">
          <div class="row">
            <div class="col-md-8">
              <div class="input-group">
                <textarea
                  v-if="questionsList.length == 0"
                  class="adminSurveyQuestionText form-control mt-3"
                  placeholder="Anket İsmini Yazınız..."
                  v-model="nameSurvey"
                ></textarea>
              </div>
              <div class="input-group">
                <textarea
                  v-model="descriptionSurvey"
                  v-if="questionsList.length == 0"
                  class="adminSurveyQuestionText form-control mt-3"
                  placeholder="Anket Açıklaması Yazınız..."
                ></textarea>
              </div>
              <div class="input-group">
                <textarea
                  v-model="question"
                  class="adminSurveyQuestionText form-control mt-3"
                  placeholder="Sorunuzu yazınız..."
                ></textarea>
              </div>
            </div>
            <!-- Dropdown / Açık Uçlu / True False / Çoktan Seçmeli -->
            <div class="col-md-4">
              <div class="input-group mb-3 adminSurveyInput">
                <button
                  class="
                    adminSurveyBtn
                    btn btn-outline-secondary
                    dropdown-toggle
                  "
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  {{ answerType }}
                </button>
                <div
                  class="adminSurveyDropDown dropdown-menu dropdown-menu-end"
                >
                  <div @click="closeEnded()">
                    <span class="adminSurveyDropdownItem dropdown-item"
                      >Çoktan Seçmeli</span
                    >
                  </div>
                  <div @click="trueFalse()">
                    <span class="adminSurveyDropdownItem dropdown-item"
                      >Evet-Hayır Sorusu</span
                    >
                  </div>
                  <div>
                    <hr class="dropdown-divider" />
                  </div>
                  <div @click="openEnded()">
                    <span class="adminSurveyDropdownItem dropdown-item"
                      >Açık Uçlu</span
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="form-check adminSurveyForm">
            <div
              class="row mainAnswerColumn"
              v-if="answerTypeId == 1 && willShowAnswers"
            >
              <div class="" v-for="index in numberAnswersArray" :key="index">
                <div class="adminAnswerColumn">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="flexRadioDefault"
                    id="flexRadioDefault1"
                  />
                  <input
                    class="adminAnswerColumn adminAnswerInput"
                    type="text"
                    v-model="answer"
                    id=""
                    placeholder="Soruya ait cevapları giriniz."
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--Adminde ve katılımcıda ortak sonraki soru butonu-->
        <div class="row btnRow">
          <div v-if="!isAddParticipant" class="adminNextQuestionBtn">
            <button
              v-if="answerTypeId == 1"
              class="btnMainPage addAnswerBtn"
              @click="addAnswers()"
            >
              Yeni Şık Ekle
            </button>
            <button
              @click="nextQuestion()"
              type="submit"
              class="btn mb-3 btnMainPage"
            >
              Sonraki Soru
            </button>
            <button
              @click="completeSurvey()"
              type="submit"
              class="btn mb-3 btnMainPage mt-3 mr-3"
            >
              Soru Seçimini Tamamla
            </button>
          </div>
          <div v-if="isAddParticipant" class="anketi-bitir-butonu">
            <button
              @click="completeSurvey()"
              type="submit"
              class="btn mb-3 btnMainPage mt-3 mr-3"
            >
              Anketi Bitir
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import DefaultLayout from "./DefaultLayout.vue";
/* eslint-disable */
export default {
  components: { DefaultLayout },

  data() {
    return {
      alertMessage: "İşleminizde hata oluştu",
      name: null,
      numberAnswers: 0,
      numberAnswersArray: [], //V-FOR'DA DÖNEBİLMEK İÇİN
      defaultChoice: 0,
      willShowAnswers: false,
      answerTypeId: 3,
      answerType: "Cevap Şekli",
      questionsList: [],
      answersList: [],
      emailList: [],
      question: "",
      answer: "",
      categoryId: 1,
      questionId: null,
      nameSurvey: "",
      isAddParticipant: false,
      descriptionSurvey: "",
      urlAddSurveyQuestions: "http://127.0.0.1:5000/addSurveyQuestions", // SORU SEÇİMİ TAMAMLANACAK
      urlAddSurveyParticipants: "http://127.0.0.1:5000/addSurveyParticipants", // SORU SEÇİMİ SONRASI KULLANICI SEÇİMİ TAMAMLANACAK
    };
  },
  methods: {
    getAlert: function (event) {
      alert(this.alertMessage);
      if (event) alert(event.target.tagName);
    },

    addAnswers() {
      this.numberAnswers++;
      this.numberAnswersArray.push(this.numberAnswers);
      this.willShowAnswers = true;
      // console.log(this.numberAnswers, this.numberAnswersArray);
      if (this.answer != "") {
        this.answersList.push({
          answers: this.answer, //ANSWERS => ANSWER OLACAK
          answerType: this.answerTypeId,
          optionId: this.numberAnswers - 1,
          questionId: this.questionId,
        });
      }
      console.log("this.answerList: ", this.answersList);
      this.answer = "";
    },
    closeEnded() {
      this.answerTypeId = 1;
      this.answerType = "Çoktan Seçmeli";
      console.log("answerTypeId: ", this.answerTypeId);
    },
    trueFalse() {
      this.answerTypeId = 2;
      this.answerType = "Evet-Hayır Sorusu";
      console.log("answerTypeId: ", this.answerTypeId);
      this.numberAnswersArray = [];
      this.numberAnswers = 0;
    },
    openEnded() {
      this.answerTypeId = 3;
      this.answerType = "Açık Uçlu";
      console.log("answerTypeId: ", this.answerTypeId);
      this.numberAnswersArray = [];
      this.numberAnswers = 0;
    },
    cannotBeSpace() {
      if (this.answerType == "Cevap Şekli") {
        this.alertMessage = "Cevap Şekli Seçmelisiniz!";
        this.getAlert();
      }
    },
    nextQuestion() {
      this.cannotBeSpace();
      console.log("nameSurvey: ", this.nameSurvey);
      console.log("descriptionSurvey: ", this.descriptionSurvey);
      console.log("question: ", this.question);
      this.willShowAnswers = false;
      this.answerType = "Cevap Şekli";
      this.questionsList.push({
        question: this.question,
        answerType: this.answerTypeId,
        categoryId: this.categoryId,
      });
      this.questionId = this.questionsList.length;
      this.question = "";

      // console.log("this.questionsList: ", this.questionsList)
    },
    completeSurvey() {
      this.nextQuestion();
      console.log("completeSurvey worked");
      const axios = require("axios");
      let data = {
        surveyDescription: this.descriptionSurvey,
        surveyName: this.nameSurvey,
        adminId: 1,
        questions: this.questionsList,
        answers: this.answersList,
      };
      console.log("data: ", data);
      let _url = this.urlAddSurveyQuestions;
      const config = {
        method: "post",
        url: _url,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
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
          if (typeof respData.errorCheck == true) {
            this.getAlert();
            this.isAddParticipant = true;
          }
        });

      this.isAddParticipant = true; //ŞİMDİLİK BURADA DURSUN
    },
  },
};
</script>

<style lang="scss" scoped>
.adminSurveyContainer {
  display: flex;
  justify-content: center;
  resize: both;
  overflow: auto;
}
.mainAnswerColumn {
  max-height: 15rem;
  overflow-y: scroll;
}
.adminSurveyRow {
  padding: 30px;
  margin-top: 100px;
  margin-bottom: 150px;
  min-height: 36rem !important;
  width: 70rem;
  border-radius: 50px;
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;
}

.adminSurveyCol {
  max-height: 20rem !important;
}

.adminSurveyQuestion {
  color: #7cdcffce;
}

.adminSurveyForm {
  color: white;
  margin-top: 50px;
  min-height: 500px;
}

.adminAnswerColumn {
  margin: 10px !important;
}

.adminAnswerInput {
  background-color: #09192c;
  border-radius: 15px;
  border: 1px solid;
  border-color: #7cdcffce;
  color: #ea4aaa;
  min-width: 650px !important;
}

.form-check-input {
  height: 35px;
  width: 35px;
  margin-top: 9px;

  &:checked {
    background-color: #7cdcffce;
    border-color: #09192c;
  }
}

.adminSurveyDropDown {
  background-color: transparent !important;
  border-color: #7cdcffce;
  border-radius: 15px;
  color: #7cdcffce;
}

.adminSurveyInput {
  display: flex;
  justify-content: flex-end;
}

.adminSurveyBtn {
  border-color: #7cdcffce;
  color: #7cdcffce;
  border-radius: 15px;
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;

  &:hover {
    border-color: #09192c;
    color: #09192c;
    background-color: #7cdcffce;
  }

  &:active {
    border-color: #09192c;
    color: #09192c;
    background-color: #7cdcffce;
  }
}

.adminSurveyDropdownItem {
  color: white;

  &:hover {
    color: white;
    background-color: #7cdcffce;
  }
}

.adminSurveyQuestionText {
  background-color: transparent;
  border-color: #7cdcffce;
  color: #ea4aaa;
}

.btnRow {
  display: flex;
  margin-top: 6rem;
}

.adminNextQuestionBtn {
  display: flex;
  justify-content: space-between;
}

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
</style>
