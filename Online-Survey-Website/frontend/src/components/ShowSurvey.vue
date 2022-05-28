<template>
<!-- Adminin soruları ve cevapları ekleyeceği ve katılımcının soruları cevaplayacağı ortak component-->
  <div class="surveyContainer">
    <div class="surveyRow">
      <div class="surveyCol">
        <div class="row">
          <div class="col-md-8">
            <h3 class="surveyQuestion">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deserunt
              voluptates deleniti est incidunt! Ipsum illo voluptas reiciendis
              autem?
            </h3>

            <div class="input-group">
              <textarea
                class="surveyQuestionText form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
          </div>
          <!--Dropdown sadece adminde gözükecek içerisinde sorunun cevap şekli seçilecek buna göre şıklar değişecek-->
          <div class="col-md-4">
            <div class="input-group mb-3 surveyInput">
              <button
                class="surveyBtn btn btn-outline-secondary dropdown-toggle"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Dropdown
              </button>
              <ul class="surveyDropDown dropdown-menu dropdown-menu-end">
                <li>
                  <a class="surveyDropdownItem dropdown-item" href="#"
                    >Action</a
                  >
                </li>
                <li>
                  <a class="surveyDropdownItem dropdown-item" href="#"
                    >Another action</a
                  >
                </li>
                <li>
                  <a class="surveyDropdownItem dropdown-item" href="#"
                    >Something else here</a
                  >
                </li>
                <li><hr class="dropdown-divider" /></li>
                <li>
                  <a class="surveyDropdownItem dropdown-item" href="#"
                    >Separated link</a
                  >
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="form-check surveyForm">
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
                A şıkkı böyle gözükecek
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
                B şıkkı böyle gözükecek
              </label>
            </div>

            <!--adminin sorulara cevap ekleyeceği input sadece admin soru ve cevap eklerken gözükecek-->
            <div class="answerColumn">
              <input
                class="form-check-input"
                type="radio"
                name="flexRadioDefault"
                id="flexRadioDefault1"
              />
              <input
                class="answerColumn answerInput"
                type="text"
                name=" "
                id=""
              />
            </div>
          </div>
        </div>
        <!--Adminde ve katılımcıda ortak sonraki soru butonu-->
        <div class="row">
          <div class="nextQuestionBtn">
            <button type="submit" class="btn  mb-3 btnMain">
              Sonraki Soru
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      name: null,
    };
  },

  methods: {},
};
</script>

<style>
.surveyContainer {
  display: flex;
  justify-content: center;
  resize: both;
  overflow: auto;
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
  justify-content: end;
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
.nextQuestionBtn{
  display: flex;
  justify-content: end;
}
</style>
