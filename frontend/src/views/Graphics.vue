<template>
  <body>
      <Headernd></Headernd>
      <div class="flex justify-start mt-6 mx-2">
        <Links></Links>
      </div>
      <div class="flex ml-96 mt-4">
         <Line :width="1500" :height="800" :chart-data=$data.chartData></Line>
      </div>
  </body>
</template>

<script>
import Line from '../components/charts/LineChartApex.vue'
import axios from 'axios'
import Headernd from '../components/Headernd.vue'
import Links from '../components/Links.vue'
export default {
  components: { Line,Headernd,Links },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            label: 'Sosanitch',

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
        this.$data.chartData.datasets[0].data = response.data.values
        this.$data.chartData.datasets[0].label = response.data.name

      }) }, 60000)
}}
</script>

<style></style>