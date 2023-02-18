<template>
<body>
<Header></Header>
<Svoistva></Svoistva>
<MainBody></MainBody>
</body>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import MainBody from '../components/MainBody.vue'
import Svoistva from '../components/Svoistva.vue'
export default {
  components: {Header,Footer,Svoistva,MainBody}
}
</script>

<style>

</style>
