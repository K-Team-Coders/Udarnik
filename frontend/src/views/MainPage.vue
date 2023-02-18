<template>
  <body>
    <Header></Header>
    <Svoistva></Svoistva>
    <MainBody></MainBody>
      <div class="flex-row mt-10">
        <div class="flex mt-3">
          <Cards></Cards>
          <Cards></Cards>
          <Cards></Cards>
          <Cards></Cards>
          <Cards></Cards>
          <Cards></Cards>
        </div>
      </div>
  </body>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import MainBody from '../components/MainBody.vue'
import Svoistva from '../components/Svoistva.vue'
import Cards from '../components/Cards.vue'
import EngineSmall from '../components/EngineSmall.vue'
export default {
  components: { Header, Footer, Svoistva, MainBody, Cards,EngineSmall }
}
</script>

<style></style>
