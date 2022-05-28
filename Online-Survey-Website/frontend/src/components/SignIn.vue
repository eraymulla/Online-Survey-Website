<template>
  <div>
    <div class="container-sm">
      <div class="row">
        <div id="left-side" class="col-sm-6 my-auto">
          <h1>StarPool </h1>
          <p>
            See how experienced developers solve problems in real-time. <br />
            Watching scripted tutorials is great, but understanding how <br />
            developers think is invaluable.
          </p>
        </div>
        <div class="col-sm-6">
          <div id="input-form" class="container col-md-11 bg-white mt-5">
            <div class="row col-sm-11 mx-auto">
              <input
                v-model="email"
                id="email"
                class="required"
                placeholder="Email Address"
                type="text"
                aria-label="mail"
              />
            </div>
            <div class="row col-sm-11 mx-auto">
              <input
                v-model="password"
                id="password"
                class="required"
                placeholder="Password"
                type="password"
                aria-label="password"
              />
            </div>
            <router-link to="/forget-password">
              <div @click="changePassword()" class="span">
                Forgot your password ?
              </div></router-link
            >

            <div class="d-grid col-sm-11 mx-auto my-3">
              <button
                @click="post({ email, password })"
                id="button-free"
                type="button"
                class="btn mb-1 shadow"
              >
                SIGN IN
              </button>
            </div>
            <div class="col-sm-9 mx-auto">
              <p @click="createAccount()" class="terms-text">
                <b>
                  New to Survey ?
                  <router-link to="/sign-up">
                    <a href="#" id="last-one"> Create an account.</a>
                  </router-link>
                </b>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import ForgetPassword from "./ForgetPassword.vue";

export default {
  data() {
    return {
      email: "",
      password: "",
      urlSignIn: "http://127.0.0.1:5000/Login",
      isChangePassword: false,
    };
  },
  components: { ForgetPassword },
  methods: {
    changePassword() {
      console.log("changePassword function worked");
      this.isChangePassword = true;
      console.log("");
    },
    createAccount() {
      console.log("createAccount function worked");
    },
    post(payload) {
      console.log("Sign In Page Post method worked");
      console.log(
        "payload || email , password",
        payload.email,
        payload.password
      );
      const axios = require("axios");
      let data = {
        email: payload.email,
        password: payload.password,
      };
      let _url = this.urlSignIn;
      const config = {
        method: "post",
        url: _url,
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
      console.log(
        "config.data || email, password, url",
        config.data.email,
        config.data.password,
        config.url
      );
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
          if (typeof respData.email != "undefined") {
            this.$router.push("/main-page");
          } else {
            this.$router.push("/");
          }
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

#input-form {
  padding-top: 35px;
  padding-bottom: 25px;
  border-radius: 8px;
  -webkit-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 6px 0px 0px rgba(0, 0, 0, 0.24);
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

#button-free {
  background-color: #3acc8b;
  font-family: var(--Font);
  color: #f6ffff;
  font-weight: 600;
  font-size: 0.91em;
  padding: 12px 20px 12px 26px;
}

.terms-text {
  transition: 2s ease 0.5s;
  margin-top: 4px;
  text-align: center;
  color: var(--Grayish-Blue);
  font-weight: 10px;
  font-size: 10px;
}

#last-one {
  color: var(--Red);
}

/*Button Efekti*/

.btn {
  height: 3rem;
  border: 5px solid var(--Green) !important;
  font-weight: bold;
  position: relative;
  cursor: pointer;
  margin-right: 55px;
}
.btn::before,
.btn::after {
  content: "";
  width: 40px;
  height: 40px;
  position: absolute;
  border: inherit;
  transition: 0.5s ease;
}
.btn::before {
  left: -15px;
  top: -15px;
  border-width: 3px 0 0 3px !important;
  border-radius: 5px 0px;
}

.btn::after {
  right: -15px;
  bottom: -15px;
  border-width: 0 3px 3px 0 !important;
  border-radius: 5px 0px;
}
.btn:hover::after,
.btn:hover::before {
  width: calc(100% + 20px) !important;
  height: calc(100% + 20px) !important;
}

/*----------------------------- */

@media screen and (min-width: 100px) and (max-width: 720px) {
  #left-side {
    display: block;
    text-align: center;
    padding-top: 5rem;
  }
  #input-form {
    margin-bottom: 5rem;
  }
  #button {
    display: grid;
    margin-left: 1rem;
    margin-right: 1rem;
  }
  #input-form {
    display: flexbox;
    padding-top: 25px;
    padding-bottom: 10px;
    height: 436px;
    max-width: 92%;
  }
  #last-one {
    display: grid;
    align-items: center;
    justify-content: center;
  }
  #button-free {
    display: grid;
    max-width: 100%;
  }
  #email {
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
