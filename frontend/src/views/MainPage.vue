<template>
  <body>
    <Header></Header>
    <Svoistva></Svoistva>
    <MainBody></MainBody>
      <div class="flex-row mt-10">
        <div class="flex mt-3">
          <Cards></Cards>
          <Cards></Cards>
          {{ allData.values[0] }}
        </div>
      </div>
  </body>
</template>

<script>
import Header from '../components/Header.vue'
import Svoistva from '../components/Svoistva.vue'
import Cards from '../components/Cards.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  components: { Header, Svoistva, Cards },
  computed: mapGetters(['allData']),
  methods: mapActions(['GET_ALLDATA']),
  async created() {
    setInterval(() => {
      JSON.parse(JSON.stringify(this.GET_ALLDATA()))
      console.log(this.allData)
    }, 10000)
  }
}
</script>

<style></style>
