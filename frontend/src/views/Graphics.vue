<template>

  <Line :chart-data=$data.chartData ></Line>
</template>

<script>
import Line from '../components/charts/LineChartApex.vue'
import axios from 'axios'
export default {
  components: { Line },
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

  created() {
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