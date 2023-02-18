import { createStore } from 'vuex'
import axios from 'axios'



export default createStore({
  state: {
   data : [],
   exhauster1_data: [],
   exhauster2_data: [],
   exhauster3_data: [],
   exhauster4_data: [],
   exhauster5_data: [],
   exhauster6_data: []
  },
  getters: {
    allData(state) {
      return state.data
    },
    getExhauster1(state){
      return state.exhauster1_data
    },
    getExhauster2(state){
      return state.exhauster1_data
    },
    getExhauster3(state){
      return state.exhauster1_data
    },
    getExhauster4(state){
      return state.exhauster1_data
    },
    getExhauster5(state){
      return state.exhauster1_data
    },
    getExhauster6(state){
      return state.exhauster1_data
    }
  },
  mutations: {
    SET_ALLDATA: (state, payload) => {
      state.data = payload;
    },
  },
  actions: {
    GET_ALLDATA: async (context, payload) => {
      let {data} = await axios.get('http://192.168.0.156:8079/lastMnemonicEX1/');
      context.commit('SET_ALLDATA', data)
    },
    
  },
  modules: {

  }
})