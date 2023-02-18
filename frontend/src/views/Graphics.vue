<template>
  
  <Line :chart-data=$data.chartData></Line>
</template>

<script>
import Line from '../components/charts/LineChartApex.vue'
import axios from 'axios'

export default {
  components: { Line },
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