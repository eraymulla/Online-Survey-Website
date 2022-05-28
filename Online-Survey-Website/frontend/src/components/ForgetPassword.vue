<template>
  <div>
    <div class="container-sm">
      <div class="row">
        <div id="left-side" class="col-sm-6 my-auto">
          <h1>Survey Monkey</h1>
          <p>
            See how experienced developers solve problems in real-time. <br />
            Watching scripted tutorials is great, but understanding how <br />
            developers think is invaluable.
          </p>
        </div>
        <div class="col-sm-6">
          <div
            id="email-form"
            v-if="!isVerifyEmail"
            class="container col-md-11 bg-white mt-5"
          >
            <div class="row col-sm-11 mx-auto">
              <input
                v-model="email"
                id="password"
                class="required"
                placeholder="Email"
                type="email"
                aria-label="email"
              />
            </div>
            <div class="d-grid col-sm-11 mx-auto">
              <button
                @click="postVerifyEmail({ email })"
                id="button-free"
                type="button"
                class="btn mb-1 shadow"
              >
                Verify Email
              </button>
            </div>
          </div>
          <div
            id="password-form"
            v-if="isVerifyEmail"
            class="container col-md-11 bg-white mt-5"
          >
            <div class="row col-sm-11 mx-auto">
              <input
                v-model="newPassword"
                id="password"
                class="required"
                placeholder="New Password"
                type="password"
                aria-label="password"
              />
            </div>
            <div class="row col-sm-11 mx-auto">
              <input
                v-model="newPasswordAgain"
                id="password"
                class="required"
                placeholder="New Password Again"
                type="password"
                aria-label="password"
              />
            </div>
            <router-link :to="routePath">
              <div class="d-grid col-sm-11 mx-auto">
                <button
                  @click="postChangePassword({ newPassword, newPasswordAgain })"

                  id="button-free"
                  type="button"
                  class="btn mb-1 shadow"
                >
                  Change Password
                </button>
              </div>
            </router-link>
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
      newPassword: "",
      newPasswordAgain: "",
      email: "",
      isVerifyEmail: null,
      urlChangePassword: "http://127.0.0.1:5000/changePassword",
      urlVerifyEmail: "http://127.0.0.1:5000/verifyEmail",
      alertMessage: "",
      isMatchedPassword: null,
      routePath: "",
    };
  },

  methods: {
    getAlert: function (event) {
      alert(this.alertMessage);
      if (event) alert(event.target.tagName);
    },
    unmatchedPassword() {
      this.isMatchedPassword = false;
      this.getAlert();
      this.routePath = "/forget-password";
      this.newPassword = "";
      this.newPasswordAgain = "";
    },
    matchedPassword() {
      this.isMatchedPassword = true;
      this.alertMessage = "Şifreniz başarıyla değiştirildi!";
      this.getAlert();
      this.routePath = "/sign-in";
    },
    emptyEmail() {
      this.isVerifyEmail = false;
      this.alertMessage = "Hata! Mail alanı boş geçilemez!";
      this.getAlert();
      this.routePath = "/forget-password";
    },
    postChangePassword(payload) {
      console.log("Change Password Post method worked");
      console.log(
        "payload || newPassword , newPasswordAgain",
        payload.newPassword,
        payload.newPasswordAgain
      );
      const axios = require("axios");
      let data = {
        newPassword: payload.newPassword,
        newPasswordAgain: payload.newPasswordAgain,
        email: this.email
      };
      let url_ = this.urlChangePassword;

      if (payload.newPassword !== payload.newPasswordAgain) {
        this.alertMessage = "Hata! Şifreler eşleşmiyor!";
        this.unmatchedPassword();
      } else if (this.newPassword === "" || this.newPasswordAgain === "") {
        this.alertMessage = "Hata! Şifre alanı boş geçilemez!";
        this.unmatchedPassword();
      } else {
        this.matchedPassword();
      }
      console.log("isMatchedPassword: ", this.isMatchedPassword);
      const config = {
        method: "post",
        url: url_,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
      if (this.isMatchedPassword) {
        console.log("config.data and config.url", config.data, config.url);
        axios(config)
          .then(function (response) {
            console.log(JSON.stringify(response.data));
          })
          .catch(function (error) {
            console.log(error);
          }).finally(() => {
            
          });
      }
    },
    postVerifyEmail(payload) {
      console.log("Verify Email Post method worked");
      console.log("isVerifyEmail: ", this.isVerifyEmail);
      console.log("payload || email", payload.email);
      const axios = require("axios");
      let data = { email: payload.email };
      let _url = this.urlVerifyEmail;
      if (this.email === "") {
        this.emptyEmail();
      }
      const config = {
        method: "post",
        url: _url,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
      let respData;
      console.log("config.data and config.url", config.data, config.url);
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
          console.log("response değeri ", response);
          respData = response.data;
        })
        .catch(function (error) {
          console.log(error);
        }).finally(() => {
          this.isVerifyEmail = respData.isVerifyEmail
          console.log("finally içinde ki this.isVerifyEmail değeri : ",this.isVerifyEmail)
          if(this.isVerifyEmail == true){
            this.alertMessage = "E-mail mevcut, şifrenizi değiştirebilirsiniz."
            this.getAlert()
            this.email = respData.email
          }else{
            this.alertMessage = "E-mail mevcut değil."
            this.getAlert()
          }
        });

      //dönen response : {"isVerifyEmail":1,"email":"admin@gmail","name":"admin","surname":"adminsurname","phone":"1112223344"}

      // async function logYaz() {
      //   await axios(config);
      //   console.log("logYaz daki respData değeri : ", respData);
      //   return respData;
      // }
      // logYaz()
    },
  },
};
</script>

<style>
#left-side {
  font-family: var(--Font);
}

#left-side h1 {
  color: #f6ffff;
  font-weight: 700;
}

#left-side p {
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
#button p {
  text-align: center;
  font-size: 15px;
  padding: 24px 24px 24px 24px;
  display: contents;
}

#password-form {
  padding-top: 35px;
  padding-bottom: 25px;
  border-radius: 8px;
  -webkit-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
}
#email-form {
  padding-top: 35px;
  padding-bottom: 25px;
  border-radius: 8px;
  -webkit-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
}

#password {
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
#email {
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

#button-free {
  background-color: #3acc8b;
  font-family: var(--Font);
  color: #f6ffff;
  font-weight: 600;
  font-size: 0.91em;
  padding: 12px 20px 12px 26px;
}

@media screen and (min-width: 100px) and (max-width: 720px) {
  #left-side {
    display: block;
    text-align: center;
    padding-top: 5rem;
  }
  #button {
    display: grid;
    margin-left: 1rem;
    margin-right: 1rem;
  }
  #password-form {
    display: flexbox;
    padding-top: 25px;
    padding-bottom: 10px;
    height: 436px;
    max-width: 92%;
    margin-bottom: 5rem;
  }
  #email-form {
    display: flexbox;
    padding-top: 25px;
    padding-bottom: 10px;
    height: 436px;
    max-width: 92%;
    margin-bottom: 5rem;
  }
  #button-free {
    display: grid;
    max-width: 100%;
  }
  #password {
    display: grid;
    max-width: 100%;
  }
  #left-side p {
    margin-top: 1.5rem;
    margin-left: 11px;
    margin-right: 11px;
  }
}
</style>
