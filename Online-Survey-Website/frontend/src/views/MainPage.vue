<template>
  <div>
    <div class="navbar-container">
      <div class="nav row">
        <div class="col-md-4 navHeader d-flex justify-content-start">
          <a href="#/main-page" class="mx-3"
            ><img src="../../public/icons/main-logo.png"
          /></a>
        </div>
        <div class="col-md-8 navItems d-flex justify-content-end">
          <button class="navItem mx-4 btnMain">Anket Oluştur</button>
          <button class="navItem mx-4 btnMain">Hesabım</button>
        </div>
      </div>
      <show-survey></show-survey>
    </div>

    <shooting-star></shooting-star>
  </div>
</template>

<script>
/* eslint-disable */
import ShootingStar from "../components/ShootingStar.vue";
import ShowSurvey from "@/components/ShowSurvey.vue";

export default {
  components: { ShootingStar, ShowSurvey },
  methods: {
    logyaz(){
      console.log("deneme deneme 1 2 1 12")
    }
  }
};
</script>

<style>
.btnMain{
  height: 3rem;
  border: 1px solid deepskyblue;
  background: transparent;
  color: rgb(123, 217, 249);
  font-weight: bold;
  position: relative;
  cursor: pointer;
  margin-right:55px;
}
.btnMain::before,
.btnMain::after{
content:'';
width: 40px;
height: 40px;
position: absolute;
border:inherit;
transition:0.5s ease;
}
.btnMain::before{
left:-15px;
top:-15px;
border-width: 1px 0 0 1px;
}

.btnMain::after{
  right:-15px;
  bottom:-15px;
  border-width: 0 1px 1px 0;
}
.btnMain:hover::after,
.btnMain:hover::before{
  width:calc(100% + 27px);
  height:calc(100% + 27px);
}

/*NAVBAR STYLE*/
.nav{
    /*background:radial-gradient(ellipse at bottom, #0d1d31 20%, #0c0d13 70%);*/
    display: flex;
    justify-content: center;
    align-items: center!important;
    background: radial-gradient(ellipse at bottom, #0d1d31 30%, #0c0d13 100%);
    box-shadow: 0 0 3px rgb(0, 191, 255), 0 0 15px rgb(0, 110, 147);
    min-height: 100px;
}
.navHeader{
    font-size: xx-large!important;
    padding-left: 4rem;
}
.navItems{
    padding-right: 4rem;
    font-size: medium!important;
}
.navItem{
  margin-right: 40px!important;
}
a{
    margin-right: 45px!important;
    color:#7cdcffce;
    text-decoration: none;
}
img:hover{
/* box-shadow: 0 0 20px rgb(193, 224, 235), 0 0 20px rgb(0, 110, 147); */
text-shadow: 0 0 20px rgb(193, 224, 235), 0 0 20px rgb(0, 110, 147);
}

</style>