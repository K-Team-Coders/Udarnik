<template>
  <div class="flex w-1/6 pr-4">
    <div class="ml-4 rounded-md">
      <p class="flex w-full justify-center bg-gray-100">Агломашина 1</p>
      <div class="mt-2 rounded-md outline outline-orange-100">
        <div class="flex bg-gray1 p-1 rounded-md">
          <img class="flex ml-4" src="../assets/Ellipse.svg" alt="" />
          <p
            class="flex justify-start ml-2 text-center text-white font-mono text-base"
          >
            Эксгаустер У-171
          </p>
          <a href="#mnemonic1"><img class="flex ml-16" src="../assets/button.svg" alt=""/></a>
        </div>
        <div class="flex-row pt-3 bg-white">
          <div class="flex text-base h-10 mx-1">
            <p class="flex w-1/2 font-mono ml-2 text-base text-justify font-bold">
              Ротор №22
            </p>
            <p
              class="flex text-base font-mono ml-8 px-2 h-6 bg-gray-200 rounded-md "
            >
              12.02.2020
            </p>
            <a class="flex font-mono text-base ml-2 mr-2" href="">Изменить</a>
          </div>
          <div class="flex font-mono font-bold text-xl ml-2 mt-3">
            <p>Последняя замена ротора</p>
          </div>
          <div class="bg-gray-100 flex mx-2 rounded-md my-1">
            <p
              class="font-bold text-lg font-mono text-center justify-center w-1/3 rounded-md bg-slate-200"
            >
              6 сут
            </p>
            <p class="w-2/3 font-mono ml-3 text-start justify-center text-lg">
              Прогноз: 12 сут
            </p>
          </div>
          <div class="flex justify-center outline outline-orange-50 my-6">
            <EngineSmall></EngineSmall>
          </div>
          <div class="flex-row ml-3">
            <div class="flex">
              <img class="" src="../assets/Btn2.svg" alt="" width="30px" />
              <p class="ml-2 mt-0.5 text-xl font-mono">Предупреждение</p>
            </div>
            <div class="flex bg-gray-200 justify-start mt-3 mr-8 ml-2">
              <p class="font-mono text-xl ml-2 ">№7 п-к</p>
              <img
                class="flex ml-14"
                src="../assets/Frametempa.svg"
                alt=""
                width="50px"
              />
              <img
                class="flex"
                src="../assets/Framevolna.svg"
                alt=""
                width="50px"
              />
            </div>
            <div class="flex bg-gray-200 justify-start mt-2 mr-8 ml-2">
              <p class="flex font-mono text-xl ml-2">№8 п-к</p>
              <img
                class="flex ml-14"
                src="../assets/Frametempa.svg"
                alt=""
                width="50px"
              />
              <img
                class="flex"
                src="../assets/Framevolna.svg"
                alt=""
                width="50px"
              />
            </div>
          </div>
          <div class="flex ml-2 mt-4 pb-10">
            <img
              class="flex"
              src="../assets/Btnright.svg"
              alt=""
              width="30px"
            />
            <p class="flex font-mono text-xl mt-0.5 ml-2">Все подшипники</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import EngineSmall from '../components/EngineSmall.vue'
export default {
  components: { EngineSmall }
}
</script>

<style></style>

