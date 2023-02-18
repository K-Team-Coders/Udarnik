<template>
    <Line :options="$options" />
  </template>

  <script>
  import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  } from 'chart.js'
  import { Line } from 'vue-chartjs'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  )
  
  export default {
    components: {
      Line
    },
    data() {
    return {
        labels: [],
        datasets: [
                {
                label: 'Data One',
                backgroundColor: '#f87979',
                data: []
                }
            ]
        }
    }
}

export const options = {
  responsive: false,
  maintainAspectRatio: false
}

  </script>
  