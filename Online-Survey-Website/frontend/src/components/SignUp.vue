<template>
  <div>
    <div class="container-sm">
      <div class="row">
        <div id="text-area" class="col-sm-6 my-auto">
          <h1>Survey Monkey</h1>
          <p>
            See how experienced developers solve problems in real-time. <br />
            Watching scripted tutorials is great, but understanding how <br />
            developers think is invaluable.
          </p>
        </div>
        <!-- name=data['name'],surname=data['surname'],email=data['email'],phone=data['phone'],password=data['password'],permissionId=2,studentOrEmployee=data['studentOrEmployee']) -->
        <div class="col-sm-6">
          <div id="main-input-area" class="container col-md-11 bg-white mt-5">
            <!-- first area  -->
            <div class="first-input-area" v-show="!isNextArea">
              <!-- name  -->
              <div class="row col-sm-11 mx-auto">
                <input
                  v-model="name"
                  id="input-area"
                  class="required"
                  placeholder="First Name"
                  type="text"
                  aria-label="name"
                />
              </div>
              <!-- surname -->
              <div class="row col-sm-11 mx-auto">
                <input
                  v-model="surname"
                  id="input-area"
                  class="required"
                  placeholder="Last Name"
                  type="text"
                  aria-label="last-name"
                />
              </div>
              <!-- email -->
              <div class="row col-sm-11 mx-auto">
                <input
                  v-model="email"
                  id="input-area"
                  class="required"
                  placeholder="Email Address"
                  type="text"
                  aria-label="mail"
                />
              </div>
              <!-- phone  -->
              <div class="row col-sm-11 mx-auto">
                <input
                  v-model="phoneNumber"
                  id="input-area"
                  class="required"
                  placeholder="Phone Number"
                  type="text"
                  aria-label="phone"
                />
              </div>
              <!-- password  -->
              <div class="row col-sm-11 mx-auto">
                <input
                  v-model="password"
                  id="input-area"
                  class="required"
                  placeholder="Password"
                  type="password"
                  aria-label="password"
                />
              </div>
              <!-- permission Id  Admin için 2 değeri User için 1 değeri -->
              <div class="row col-sm-11 mx-auto">
                <div id="input-area">
                  Choose an one: <br />
                  <input
                    type="radio"
                    value="1"
                    v-model="permissionId"
                    @click="setPermissionId1()"
                  />
                  <label for="one">Katılımcı</label>

                  <input
                    type="radio"
                    value="2"
                    v-model="permissionId"
                    @click="setPermissionId2()"
                  />
                  <label for="two">Admin</label>
                </div>
              </div>
              <!-- student or employee  -->
              <div class="row col-sm-11 mx-auto">
                <div @click="deneme()" id="input-area">
                  Choose an one: <br />
                  <input
                    type="radio"
                    value="1"
                    v-model="jobId"
                    @click="setJobId1()"
                  />
                  <label for="one">Student</label>

                  <input
                    type="radio"
                    value="2"
                    v-model="jobId"
                    @click="setJobId2()"
                  />
                  <label for="two">Employee</label>
                </div>
              </div>
            </div>

            <!-- second input area for student -->
            <!-- studentInfo = StudentUserInfoModel(userId=data['userId'],permissionId=data['permissionId'],age=data['age'],
            educationStatus=data['educationStatus'],department=data['department'],year=data['year']) -->
            <div class="second-input-area" v-show="isNextArea">
              <div class="for-student" v-if="jobId == '1'">
                <!-- age  -->
                <div class="row col-sm-11 mx-auto">
                  <input
                    v-model="age"
                    id="input-area"
                    class="required"
                    placeholder="What's your age ?"
                    type="number"
                  />
                </div>
                <!-- education status  -->
                <div class="row col-sm-11 mx-auto">
                  <div id="input-area">
                    Choose your education status
                    <select v-model="educationStatus">
                      <option
                        v-for="(option, index) in options"
                        :key="index"
                        :value="option.value"
                      >
                        {{ option.text }}
                      </option>
                    </select>
                  </div>
                </div>
                <!-- department  -->
                <div class="row col-sm-11 mx-auto">
                  <input
                    v-model="department"
                    id="input-area"
                    class="required"
                    placeholder="What's your department ?"
                    type="text"
                  />
                </div>
                <!-- grade  -->
                <div
                  class="row col-sm-11 mx-auto"
                  v-if="educationStatus == 3"
                >
                  <input
                    v-model="grade"
                    id="input-area"
                    class="required"
                    placeholder="What grade are u in ?"
                    type="number"
                  />
                </div>
              </div>

              <!-- employeeInfo = EmployeeUserInfoModel(userId=data['userId'],permissionId=data['permissionId'],age=data['age'],
               salary=data['salary'],experience=data['experience']) -->
              <!-- second input area for employee -->
              <div class="for-employee" v-if="jobId == '2'">
                <!-- salary  -->
                <div class="row col-sm-11 mx-auto">
                  <input
                    v-model="salary"
                    id="input-area"
                    class="required"
                    placeholder="What's your salary ?"
                    type="number"
                  />
                </div>
                <!-- experience -->
                <div class="row col-sm-11 mx-auto">
                  <input
                    v-model="experience"
                    id="input-area"
                    class="required"
                    placeholder="Experience ?"
                    type="number"
                  />
                </div>
                <!-- age -->
                <div class="row col-sm-11 mx-auto">
                  <input
                    v-model="age"
                    id="input-area"
                    class="required"
                    placeholder="What's your age ?"
                    type="number"
                  />
                </div>
              </div>
            </div>
            <!-- sign up button  -->
            <div class="d-grid col-sm-11 mx-auto">
              <button
                v-show="isNextArea"
                @click="
                  signUpPost({
                    name,
                    surname,
                    email,
                    age,
                    password,
                    phoneNumber,
                    jobId,
                    isAdmin,
                    department,
                    permissionId,
                    grade,
                    experience,
                    salary,
                    educationStatus,
                  })
                "
                id="signup-button"
                type="button"
                class="btn mb-1 shadow"
              >
                <router-link to="/sign-in"> SIGN UP</router-link>
              </button>
            </div>

            <div class="d-grid col-sm-11 mx-auto">
              <button
                v-if="!isNextArea"
                @click="
                  nextAreaPost({
                    name,
                    surname,
                    email,
                    password,
                    phoneNumber,
                    jobId,
                    isAdmin,
                    permissionId,
                  }),
                    deneme()
                "
                id="signup-button"
                type="button"
                class="btn mb-1 shadow justify-content-center"
              >
                Next
              </button>
              <a
                v-if="isNextArea"
                id="lastOne"
                @click="this.isNextArea = false"
              >
                Prev
              </a>
            </div>
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
      email: "",
      password: "",
      name: "",
      surname: "",
      age: "",
      phoneNumber: "",
      studentOrEmployee : null,
      jobId: null,
      isAdmin: "",
      department: "",
      permissionId: null,
      grade: null,
      experience: null,
      salary: null,
      urlSignUp: "http://127.0.0.1:5000/Signup",
      urlAddInfo: "http://127.0.0.1:5000/addInfo",
      isNextArea: null,
      isAdminorUser: false,
      educationStatus: null,
      userId: null,
      options: [
        { text: "Secondary School", value: 1 },
        { text: "High School", value: 2 },
        { text: "University", value: 3 },
        { text: "Postgraduate", value: 4 },
      ],
    };
  },

  methods: {
    deneme() {
      console.log(this.permissionId, this.jobId);
    },

    setJobId1() {
      this.jobId = 1;
      console.log("setJobId çalıştı jobId değeri : ", this.jobId);
    },
    setJobId2() {
      this.jobId = 2;
      console.log("setJobId çalıştı jobId değeri : ", this.jobId);
    },
    setPermissionId1() {
      this.permissionId = 1;
      console.log(
        "setPermissionId1 çalıştı permissionId değeri : ",
        this.permissionId
      );
    },
    setPermissionId2() {
      this.permissionId = 2;
      console.log(
        "setPermissionId2 çalıştı permissionId değeri : ",
        this.permissionId
      );
    },
    nextAreaPost(payload) {
      console.log("nextArea function worked");
      const axios = require("axios");

      let data = {
        name: payload.name,
        surname: payload.surname,
        email: payload.email,
        password: payload.password,
        phone: payload.phoneNumber,
        studentOrEmployee: this.jobId,
        //isAdmin: payload.isAdmin,
        permissionId: this.permissionId,
        //permissionId: payload.permissionId,
      };

      let url_ = this.urlSignUp;

      const config = {
        method: "post",
        url: url_,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
      console.log(
        "config.data |||| \n name: ",
        config.data.name,
        "\n surname: ",
        config.data.surname,
        "\n email: ",
        config.data.email,
        "\n password: ",
        config.data.password,
        "\n phoneNumber: ",
        config.data.phoneNumber,
        "\n jobId: ",
        config.data.jobId,
        "\n permissionId: ",
        config.data.permissionId,
        "\n grade: ",
        config.data.grade,
        "\n experience: ",
        config.data.experience,
        "\n salary: ",
        config.data.salary,
        "\n educationStatus: ",
        config.data.educationStatus,
        "\n age: ",
        config.data.age
      );
      let respData;
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
          respData = response.data;
        })
        .catch(function (error) {
          console.log(error);
        })
        .finally(() => {
          console.log("finally çalıştı");
          if (respData.check == true) {
            this.isNextArea = true;
            this.userId = respData.userId;
          }
        });
    },

    isAdminOrUser() {
      this.isAdminorUser = !this.isAdminorUser;
      console.log("isAdminOrUser function worked");
    },

    signUpPost(payload) {
      console.log("Sign Up Post method worked");
      console.log(
        "data() return {} |||| \n name: ",
        this.name,
        "\n surname: ",
        this.surname,
        "\n email: ",
        this.email,
        "\n password: ",
        this.password,
        "\n phoneNumber: ",
        this.phoneNumber,
        "\n jobId: ",
        this.jobId,
        "\n permissionId: ",
        this.permissionId,
        "\n grade: ",
        this.grade,
        "\n experience: ",
        this.experience,
        "\n salary: ",
        this.salary,
        "\n educationStatus: ",
        this.educationStatus,
        "\n age: ",
        this.age,
      );
      console.log(
        "payload |||| \n name: ",
        payload.name,
        "\n surname: ",
        payload.surname,
        "\n email: ",
        payload.email,
        "\n password: ",
        payload.password,
        "\n phoneNumber: ",
        payload.phoneNumber,
        "\n jobId: ",
        payload.jobId,
        "\n permissionId: ",
        payload.permissionId,
        "\n grade: ",
        payload.grade,
        "\n experience: ",
        payload.experience,
        "\n salary: ",
        payload.salary,
        "\n educationStatus: ",
        payload.educationStatus,
        "\n age: ",
        payload.age,
      );
      let data;
      const axios = require("axios");
      if (this.jobId == 1) {
        console.log("this.jobId = 1")
        data = {
          studentOrEmployee: parseInt(this.jobId),
          permissionId: this.permissionId,
          age: payload.age,
          department: payload.department,
          grade: payload.grade,
          educationStatus: payload.educationStatus,
          userId: this.userId,
        };
        console.log(
          "öğrenci gönderilen bilgiler : ",
          payload.jobId,
          this.permissionId,
          payload.age,
          payload.department,
          payload.grade,
          payload.educationStatus,
          this.userId
        );
      } else if (this.jobId == 2) {
        console.log("this.jobId = 2")
        data = {
          studentOrEmployee: parseInt(this.jobId),
          permissionId: this.permissionId,
          age: payload.age,
          experience: payload.experience,
          salary: payload.salary,
          userId: this.userId,
        };
      }

      let _url = this.urlAddInfo;

      const config = {
        method: "post",
        url: _url,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
      console.log(
        "config.data |||| \n name: ",
        config.data.name,
        "\n surname: ",
        config.data.surname,
        "\n email: ",
        config.data.email,
        "\n password: ",
        config.data.password,
        "\n phoneNumber: ",
        config.data.phoneNumber,
        "\n studentOrEmployee: ",
        config.data.studentOrEmployee,
        "\n permissionId: ",
        config.data.permissionId,
        "\n grade: ",
        config.data.grade,
        "\n experience: ",
        config.data.experience,
        "\n salary: ",
        config.data.salary,
        "\n department: ",
        config.data.department,
        "\n educationStatus: ",
        config.data.educationStatus,
        "\n userId: ",
        config.data.userId,
        "\n age: ",
        config.data.age
      );
      console.log(config)
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
          console.log(error);
        })
        .finally(() => {
          console.log();
        });
    },
  },
};
</script>

<style>
:root {
  --Red: hsl(0, 100%, 74%);
  --Green: hsl(154, 59%, 51%);
  --Blue: hsl(248, 32%, 49%);
  --Dark-Blue: hsl(249, 11%, 26%);
  --Grayish-Blue: hsl(246, 25%, 77%);
  --Font: "Poppins", "sans-serif";
}

#text-area {
  font-family: var(--Font);
}

#text-area h1 {
  color: #f6ffff;
  font-weight: 700;
}

#text-area p {
  color: #f7c5c5;
  font-weight: 650;
}

#button {
  background-color: #6054a6;
  border-radius: 8px;
  margin-top: 3rem;
  -webkit-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  padding: 12px 20px 12px 26px;
}

#buttonForm {
  font-family: var(--Font);
}

.span {
  text-align: end;
  font-family: var(--Font);
  font-size: 13px;
  color: red;
  margin: -10px 10px 10px 0px !important;
  font-weight: 600;
}
#button p {
  text-align: center;
  font-size: 15px;
  padding: 24px 24px 24px 24px;
  display: contents;
}

#main-input-area {
  padding-top: 35px;
  padding-bottom: 25px;
  border-radius: 8px;
  -webkit-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
}

#input-area {
  font-family: var(--Font);
  padding: 12px 20px 12px 26px;
  border: solid 1px gainsboro;
  margin-bottom: 1.8rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.91em;
  outline-color: #9997a5;
  color: #555353;
}

#signup-button {
  background-color: #3acc8b;
  font-family: var(--Font);
  color: #f6ffff;
  font-weight: 600;
  font-size: 0.91em;
  padding: 12px 20px 12px 26px;
}

.termsText {
  transition: 2s ease 0.5s;
  margin-top: 4px;
  text-align: center;
  color: var(--Grayish-Blue);
  font-weight: 10px;
  font-size: 10px;
}

#lastOne {
  color: var(--Red);
}

@media screen and (min-width: 100px) and (max-width: 720px) {
  #text-area {
    display: block;
    text-align: center;
    padding-top: 5rem;
  }
  #text-area p {
    margin-top: 1.5rem;
    margin-left: 11px;
    margin-right: 11px;
  }
  #button {
    display: grid;
    margin-left: 1rem;
    margin-right: 1rem;
  }
  #main-input-area {
    display: flexbox;
    padding-top: 25px;
    padding-bottom: 10px;
    height: 436px;
    max-width: 92%;
    margin-bottom: 5rem;
  }
  #lastOne {
    display: grid;
    align-items: center;
    justify-content: center;
  }
  #signup-button {
    display: grid;
    max-width: 100%;
  }
}
</style>
