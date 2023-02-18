import axios from "axios";
export default {
  state: {
    data1: [],
  },
  getters: {
    allData1(state) {
      return state.data1;
    },
  },
  mutations: {
    SET_ALLDATA1: (state, payload) => {
      state.data1 = payload;
    },
  },
  actions: {
    GET_ALLDATA1: async (context, payload) => {
      let { data1 } = await axios.get(
        "http://192.168.0.156:8079/lastMnemonicEX1/"
      );
      context.commit("SET_ALLDATA1", data1);
      console.log(data1);
    },
  },
};
