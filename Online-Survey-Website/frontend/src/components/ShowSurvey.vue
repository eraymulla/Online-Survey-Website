<template>
  <div>
    <default-layout> </default-layout>
    <div class="surveyContainer">
      <div class="surveyRow">
        <div class="surveyCol">
          <div class="row">
            <div class="col-md">
              <h3 class="surveyQuestion">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Deserunt voluptates deleniti est incidunt! Ipsum illo voluptas
                reiciendis autem?
              </h3>
            </div>
          </div>
          <!-- <div class="form-check surveyForm">
            <div class="row">
              <div class="answerColumn">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                />
                <label
                  class="form-check-label answerLabel"
                  for="flexRadioDefault1"
                >
                  Yes
                </label>
              </div>
              <div class="answerColumn">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                />
                <label
                  class="form-check-label answerLabel"
                  for="flexRadioDefault1"
                >
                  No
                </label>
              </div>
            </div>
          </div> -->
          <div class="row mt-4">
            <div class="input-group">
              <textarea
                class="participantSurveyQuestionText form-control"
                aria-label="With textarea"
                placeholder="Cevabınızı yazınız..."
              ></textarea>
            </div>
          </div>
          <div class="row nextQuestionRow">
            <div class="nextQuestionBtn">
              <button type="submit" class="btn mb-3 btnMain">
                Sonraki Soru
              </button>
            </div>
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

<style scoped>
.surveyContainer {
  display: flex;
  justify-content: center;
  resize: both;
  overflow: auto;
  position: absolute;
  z-index: 1;
}
.surveyRow {
  padding: 30px;
  margin-top: 100px;
  margin-bottom: 150px;
  min-height: 36rem !important;
  width: 70rem;
  display: flex !important;
  border-radius: 50px;
  /* background: linear-gradient(145deg, #112c4d, #13141d); */
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;
}
.surveyCol {
  max-height: 2rem !important;
}
.surveyQuestion {
  color: #7cdcffce;
}
.surveyForm {
  color: white;
  margin-top: 50px;
}
.answerColumn {
  margin: 15px;
}
.form-check-input {
  height: 35px;
  width: 35px;
  margin-top: 9px;
}
.answerLabel {
  margin-top: 4px;
  height: 40px;
  margin-left: 40px;
  display: flex;
  align-items: center;
}
.form-check-input:checked {
  background-color: #7cdcffce;
  border-color: #09192c;
}
.surveyDropDown {
  background-color: transparent !important;
}
.surveyInput {
  display: flex;
  justify-content: flex-end;
}
.surveyBtn {
  border-color: #7cdcffce;
  color: #7cdcffce;
  border-radius: 15px;
  background: transparent;
  box-shadow: 20px 20px 50px #0d1d31, -20px -20px 50px #0c0d13;
}
.surveyBtn:hover {
  border-color: #09192c;
  color: #09192c;
  background-color: #7cdcffce;
}
.surveyBtn:active {
  border-color: #09192c;
  color: #09192c;
  background-color: #7cdcffce;
}
.surveyDropDown {
  border-color: #7cdcffce;
  border-radius: 15px;
  color: #7cdcffce;
}
.surveyDropdownItem:hover {
  color: white;
  background-color: #7cdcffce;
}
.answerInput {
  background-color: #09192c;
  border-radius: 15px;
  border: 1px solid;
  border-color: #7cdcffce;
  color: #ea4aaa;
}
.surveyQuestionText {
  background-color: transparent;
  border-color: #7cdcffce;
  color: #09192c;
}
.nextQuestionBtn {
  display: flex;
  justify-content: flex-end;
}
.participantSurveyQuestionText {
  background-color: transparent;
  border-color: #7cdcffce;
  color: #09192c;
}
</style>
