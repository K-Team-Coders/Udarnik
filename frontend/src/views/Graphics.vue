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
        labels: [1, 2, 3, 4, 5],
        datasets: [
          {
            data: [1, 2, 3, 4, 70],
            label: 'Sosanitch',

          },
        ]
      }
    }
  },

  mounted() {
    // Каждую минуту - апдейт!
    setInterval(() => {
      axios.get('http://192.168.0.156/lastGraph/').then(response => { 

      }) }, 1000)
}}
</script>

<style></style>