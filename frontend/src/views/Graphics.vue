<template>
  <body>
    <Headernd></Headernd>
    <div class="flex justify-start mt-6 mx-2">
      <Links></Links>
    </div>
    <div>
      <div class="flex mt-4">
        <div class="ml-80">
          <Line
            :width="1500"
            :height="800"
            :chart-data="$data.chartData"
          ></Line>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Line from '../components/charts/LineChartApex.vue'
import axios from 'axios'
import Headernd from '../components/Headernd.vue'
import Links from '../components/Links.vue'
import DropDownMenu from '../components/DropDownMenu.vue'
export default {
  components: { Line, Headernd, Links, DropDownMenu },
  data () {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            label: '',
            backgroundColor: ''

          },
        ]
      }
  }},

   async created() {
    // Каждую минуту - апдейт!
   setInterval(() => {
      axios.get('http://192.168.0.156:8079/lastGraphEX1/').then(response => { 
        console.log(response.data)
        this.$data.chartData.labels = response.data.times
        this.$data.chartData.datasets = response.data.datasets
      }) }, 10000)
}}
</script>

<style></style>
