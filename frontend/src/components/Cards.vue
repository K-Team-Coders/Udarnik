<template>
  <div class="flex w-1/6 pr-4">
    <div class="ml-4 rounded-md">
      <p class="flex w-full justify-center bg-gray-100">
        Агломашина 1 (Экран состояния эксгаустера)
      </p>
      <div class="mt-2 rounded-md outline outline-orange-100">
        <div class="flex bg-gray1 p-1 rounded-md">
          <svg width="10" height="11" viewBox="0 0 10 11" v-if="allData.values[120] == 1" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="5" cy="5.5249" r="5" fill="#45f542"/>
</svg>
<svg width="10" height="11" viewBox="0 0 10 11" v-else fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="5" cy="5.5249" r="5" fill="#bf1a0b"/>
</svg>

          <p
            class="flex justify-start items-center ml-2 text-center text-white font-mono text-base"
          >
            Эксгаустер У-171
          </p>
          <button
            onclick="window.location.href = 'http://192.168.0.174:8080/#/mnemonic1'"
            class="flex bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-lg ml-20"
          >
            >
          </button>
        </div>
        <div class="flex-row pt-3 bg-white">
          <div class="outline outline-orange-50 my-6">
            <svg
              id="Слой_1"
              data-name="Слой 1"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 260 138"
            >
              <path
                d="M173.5,18.5h53A3.543,3.543,0,0,1,230,22V65a3.543,3.543,0,0,1-3.5,3.5h-53A3.543,3.543,0,0,1,170,65V22A3.543,3.543,0,0,1,173.5,18.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M167,31.5h3v26l-3-3.8Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M233,57.5h-3v-26l3,3.8Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M83.9,31.5h51.9a4.481,4.481,0,0,1,4.5,4.5V78a4.481,4.481,0,0,1-4.5,4.5H83.9A4.481,4.481,0,0,1,79.4,78V36.1A4.5,4.5,0,0,1,83.9,31.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M82.5,33.5l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V34.3l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M82.5,77.6l.6.4.7.4V80l-.7.4-.6.4-.6-.4-.7-.4V78.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M82.5,55l.6.4.7.4v1.6l-.7.4-.6.2-.6-.4-.7-.4V55.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M136.5,33.5l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V34.3l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M136.5,77.6l.6.4.7.4V80l-.7.4-.6.4-.6-.4-.7-.4V78.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M136.5,55l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V55.8l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M109.8,33.5l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V34.3l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M109.8,77.6l.6.4.7.4V80l-.7.4-.6.4-.6-.4-.7-.4V78.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M12.3,56.5H23.8a2.263,2.263,0,0,1,2.3,2.3V82.3a2.263,2.263,0,0,1-2.3,2.3H12.3A2.263,2.263,0,0,1,10,82.3V58.8A2.263,2.263,0,0,1,12.3,56.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M12.5,57.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V58.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M12.5,80.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V81.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M23.5,57.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V58.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M23.5,80.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V81.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M14,66.5H29v10H14Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M13.8,61.5h8.5a.789.789,0,0,1,.8.8V78.8a.789.789,0,0,1-.8.8H13.8a.789.789,0,0,1-.8-.8V62.3A.789.789,0,0,1,13.8,61.5Z"
                transform="translate(0 -0.5)"
                style="fill: #414f4f;stroke: #8d9595;stroke-width: 2px"
              />
              <path
                d="M57.3,56.5H68.8a2.263,2.263,0,0,1,2.3,2.3V82.3a2.263,2.263,0,0,1-2.3,2.3H57.3A2.263,2.263,0,0,1,55,82.3V58.8A2.263,2.263,0,0,1,57.3,56.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M57.5,57.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V58.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M57.5,80.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V81.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M68.5,57.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V58.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M68.5,80.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.6V81.4l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M53,66.5H79v10H53Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M58.8,61.5h8.5a.789.789,0,0,1,.8.8V78.8a.789.789,0,0,1-.8.8H58.8a.789.789,0,0,1-.8-.8V62.3A.789.789,0,0,1,58.8,61.5Z"
                transform="translate(0 -0.5)"
                style="fill: #414f4f;stroke: #8d9595;stroke-width: 2px"
              />
              <path
                d="M152.3,29.5h11.5a2.263,2.263,0,0,1,2.3,2.3V55.3a2.263,2.263,0,0,1-2.3,2.3H152.3a2.263,2.263,0,0,1-2.3-2.3V31.8A2.263,2.263,0,0,1,152.3,29.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M152.5,30.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V31.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M152.5,53.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V54.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M163.5,30.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V31.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M163.5,53.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V54.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M140,39.5h27v10H140Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M153.8,34.5h8.5a.789.789,0,0,1,.8.8V51.8a.789.789,0,0,1-.8.8h-8.5a.789.789,0,0,1-.8-.8V35.3A.789.789,0,0,1,153.8,34.5Z"
                transform="translate(0 -0.5)"
                style="fill: #414f4f;stroke: #8d9595;stroke-width: 2px"
              />
              <path
                d="M236.3,29.5h11.5a2.263,2.263,0,0,1,2.3,2.3V55.3a2.263,2.263,0,0,1-2.3,2.3H236.3a2.263,2.263,0,0,1-2.3-2.3V31.8A2.263,2.263,0,0,1,236.3,29.5Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M236.5,30.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V31.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M236.5,53.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V54.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M247.5,30.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V31.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M247.5,53.8l.6.4.7.4v1.6l-.7.4-.6.4-.6-.4-.7-.4V54.6l.7-.4Z"
                transform="translate(0 -0.5)"
                style="fill: #8d9595"
              />
              <path
                d="M231,39.5h16v10H231Z"
                transform="translate(0 -0.5)"
                style="fill: #3b4848"
              />
              <path
                d="M237.8,34.5h8.5a.789.789,0,0,1,.8.8V51.8a.789.789,0,0,1-.8.8h-8.5a.789.789,0,0,1-.8-.8V35.3A.789.789,0,0,1,237.8,34.5Z"
                transform="translate(0 -0.5)"
                style="fill: #414f4f;stroke: #8d9595;stroke-width: 2px"
              />
              <rect
                x="29.5"
                y="41.6"
                width="22.9"
                height="54.9"
                style="fill: #8d9595;stroke: #677272;stroke-width: 1.0520999431610107px"
              />
              <rect
                x="29.3"
                y="43.5"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="49.1"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="54.7"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="60.3"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="65.9"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="71.5"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="77.1"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="82.7"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="88.4"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <rect
                x="29.3"
                y="94"
                width="23"
                height="1.4"
                style="fill: #677272"
              />
              <path
                d="M11.9,20.6,29,41.6H53l17.4-21v-10H11.9Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M70,118.7,53,97.5H28.9L12,118.7v9.9H70Z"
                transform="translate(0 -0.5)"
                style="fill: #677272"
              />
              <path
                d="M6,1.5H254a4.951,4.951,0,0,1,5,5v126a4.951,4.951,0,0,1-5,5H6a4.951,4.951,0,0,1-5-5V6.5A5.015,5.015,0,0,1,6,1.5Z"
                transform="translate(0 -0.5)"
                style="fill: none;stroke: #ced7e7;stroke-width: 2px"
              />
              <g id="PS4">
                <path
                  d="M87.8,39.1h19.5a.789.789,0,0,1,.8.8V54.4a.789.789,0,0,1-.8.8H87.8a.789.789,0,0,1-.8-.8V39.8A.713.713,0,0,1,87.8,39.1Z"
                  transform="translate(0 -0.5)"
                  :style="{
                    fill: allData.colors[48],
                    stroke: allData.colors[49]
                  }"
                  stroke-width="2px"
                />
                <rect
                  x="87.8"
                  y="39.6"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(94.263 50.833)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  4
                </text>
              </g>
              <g id="PS3">
                <path
                  d="M111.8,39h19.5a.789.789,0,0,1,.8.8V54.3a.789.789,0,0,1-.8.8H111.8a.789.789,0,0,1-.8-.8V39.8A.789.789,0,0,1,111.8,39Z"
                  transform="translate(0 -0.5)"
                  :style="{
                    fill: allData.colors[46],
                    stroke: allData.colors[47]
                  }"
                  stroke-width="2px"
                />
                <rect
                  x="111.9"
                  y="39.5"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(118.422 50.797)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  3
                </text>
              </g>
              <g id="PS6">
                <path
                  d="M87.8,60.5h19.5a.789.789,0,0,1,.8.8V75.8a.789.789,0,0,1-.8.8H87.8a.789.789,0,0,1-.8-.8V61.3A.789.789,0,0,1,87.8,60.5Z"
                  transform="translate(0 -0.5)"
                  :style="{
                    fill: allData.colors[52],
                    stroke: allData.colors[53]
                  }"
                  stroke-width="2px"
                />
                <rect
                  x="87.9"
                  y="60.7"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(94.422 71.945)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  6
                </text>
              </g>
              <g id="PS5">
                <path
                  d="M111.8,60.8h19.5a.789.789,0,0,1,.8.8V76.1a.789.789,0,0,1-.8.8H111.8a.789.789,0,0,1-.8-.8V61.6A.789.789,0,0,1,111.8,60.8Z"
                  transform="translate(0 -0.5)"
                  :style="{
                    fill: allData.colors[50],
                    stroke: allData.colors[51]
                  }"
                  stroke-width="2px"
                />
                <rect
                  x="111.9"
                  y="61.3"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(118.422 72.583)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  5
                </text>
              </g>
              <g id="PS1">
                <rect
                  x="238"
                  y="35"
                  width="8"
                  height="16"
                  :style="{
                    fill: allData.colors[42],
                    stroke: allData.colors[43]
                  }"
                />
                <rect
                  x="232.4"
                  y="36"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(238.922 47.285)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  1
                </text>
              </g>
              <g id="PS2">
                <rect
                  x="154"
                  y="35"
                  width="8"
                  height="16"
                  :style="{
                    fill: allData.colors[44],
                    stroke: allData.colors[45]
                  }"
                />
                <rect
                  x="148.4"
                  y="36"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(154.922 47.285)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  2
                </text>
              </g>
              <g id="PS7">
                <rect
                  x="59"
                  y="62"
                  width="8"
                  height="16"
                  :style="{
                    fill: allData.colors[54],
                    stroke: allData.colors[55]
                  }"
                />
                <rect
                  x="53.4"
                  y="62.7"
                  width="19.1"
                  height="14"
                  style="fill: none"
                />
                <text
                  transform="translate(59.922 73.926)"
                  style="isolation: isolate;font-size: 12px;font-family: ArialMT, Arial"
                >
                  7
                </text>
              </g>
              <g id="PS8">
                <rect
                  x="14"
                  y="62"
                  width="8"
                  height="8"
                  :style="{
                    fill: allData.colors[56],
                    stroke: allData.colors[57]
                  }"
                />
                <rect x="14" y="62" width="8" height="8.1" style="fill: none" />
                <text
                  transform="translate(16.468 68.187)"
                  style="isolation: isolate;font-size: 6px;font-family: ArialMT, Arial"
                >
                  8
                </text>
              </g>
              <line x1="14" y1="70" x2="22" y2="70" style="fill: none" />
              <line
                x1="21.5"
                y1="90.4"
                x2="21.5"
                y2="90.4"
                style="fill: none"
              />
              <polygon
                points="14 70.5 22 70.5 22 70.5 14 70.5"
                style="fill: none"
              />
              <g id="PS9">
                <rect
                  x="14"
                  y="70"
                  width="8"
                  height="8.2"
                  :style="{
                    fill: allData.colors[58],
                    stroke: allData.colors[59]
                  }"
                />
                <rect
                  x="14"
                  y="70.1"
                  width="8"
                  height="8.1"
                  style="fill: none"
                />
                <text
                  transform="translate(16.461 76.277)"
                  style="isolation: isolate;font-size: 6px;font-family: ArialMT, Arial"
                >
                  9
                </text>
              </g>
              <path
                d="M77.447,106.532h78.407a.357.357,0,0,1,.4.4V128.9a.357.357,0,0,1-.4.4H77.447a.357.357,0,0,1-.4-.4v-21.96A.608.608,0,0,1,77.447,106.532Z"
                transform="translate(0 -0.5)"
                style="fill: #eff2f6"
              />
              <rect
                x="79.063"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="91.458"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="104.256"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="116.65"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="129.045"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="141.574"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <rect
                x="153.968"
                y="108.457"
                width="0.404"
                height="4.85"
                style="fill: #d9dada"
              />
              <path
                d="M77.447,106.532h78.407a.357.357,0,0,1,.4.4V128.9a.357.357,0,0,1-.4.4H77.447a.357.357,0,0,1-.4-.4v-21.96A.608.608,0,0,1,77.447,106.532Z"
                transform="translate(0 -0.5)"
                style="fill: none;stroke: #8d9595;stroke-width: 2px"
              />
              <g id="oil_level">
                <rect
                  id="oil_level_loader"
                  x="79.063"
                  y="114.52"
                  :style="{ width: (allData.values[118] * 75.174) / 100 }"
                  height="12.394"
                  style="fill: #1fb826"
                />
                <text
                  transform="translate(81.258 125.739)"
                  style="isolation: isolate;font-size: 4.794163703918457px;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
                >
                  УРОВЕНЬ МАСЛА, %
                </text>
                <text
                  id="oil_level_value"
                  transform="translate(81.334 120.012)"
                  style="isolation: isolate;font-size: 4.794163703918457px;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
                >
                  {{ allData.values[118] }}
                </text>
              </g>
              <text
                transform="translate(84.218 112.556)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                0
              </text>
              <text
                transform="translate(94.818 112.556)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                20
              </text>
              <text
                transform="translate(107.451 112.556)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                40
              </text>
              <text
                transform="translate(119.786 112.628)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                60
              </text>
              <text
                transform="translate(132.931 112.556)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                80
              </text>
              <text
                transform="translate(143.126 112.637)"
                style="isolation: isolate;font-size: 4.794163703918457px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                100
              </text>
              <path
                d="M163.155,106.223h89.3a.361.361,0,0,1,.409.409v22.359a.361.361,0,0,1-.409.409h-89.3a.361.361,0,0,1-.409-.409V106.632A.435.435,0,0,1,163.155,106.223Z"
                transform="translate(0 -0.5)"
                style="fill: #eff2f6;stroke: #8d9595;stroke-width: 2px"
              />
              <rect
                x="164.791"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="176.925"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="189.604"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="201.738"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="213.871"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="226.142"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="238.275"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="250.545"
                y="108.041"
                width="0.409"
                height="4.772"
                style="fill: #d9dada"
              />
              <rect
                x="164.791"
                y="113.903"
                width="0.818"
                height="12.952"
                style="fill: #eb5835"
              />
              <rect
                x="250.136"
                y="113.903"
                width="0.818"
                height="12.952"
                style="fill: #eb5835"
              />
              <g id="oil_presure">
                <rect
                  id="oil_presure_loader"
                  x="165.609"
                  y="113.903"
                  :style="{ width: (allData.values[119] * 84.527) / 6 }"
                  height="12.952"
                  style="fill: #fdc65f"
                />
                <text
                  transform="translate(167.069 125.6)"
                  style="isolation: isolate;font-size: 4.7207136154174805px;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
                >
                  ДАВЛЕНИЕ МАСЛА, кг/см
                </text>
                <text
                  transform="translate(227.889 124.027)"
                  style="isolation: isolate;font-size: 2.75217604637146px;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
                >
                  2
                </text>
                <text
                  id="oil_presue_val"
                  transform="translate(167.591 119.568)"
                  style="isolation: isolate;font-size: 4.7207136154174805px;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
                >
                  {{ allData.values[119] }}
                </text>
              </g>
              <text
                transform="translate(169.286 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                0
              </text>
              <text
                transform="translate(182.284 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                1
              </text>
              <text
                transform="translate(194.113 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                2
              </text>
              <text
                transform="translate(206.354 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                3
              </text>
              <text
                transform="translate(218.852 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                4
              </text>
              <text
                transform="translate(230.763 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                5
              </text>
              <text
                transform="translate(242.887 112.309)"
                style="isolation: isolate;font-size: 4.7207136154174805px;fill: #595959;font-family: MSReferenceSansSerif, MS Reference Sans Serif"
              >
                6
              </text>
            </svg>
          </div>
          <p class="flex  justify-start pl-5 bg-gray-100 text-2xl font-bold">
            Все подшипники:
          </p>
          <button
            class="bg-gray-300 hover:bg-gray-400 ml-5 mt-2 text-gray-800 font-bold py-2 px-4 rounded-lg flex "
          >
            >
          </button>
          <div id="myDropdown" class="flex-row text-lg my-2 font-mono mt-1">
            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС1
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path :style="{ fill: allData.colors[0], stroke: allData.colors[1] }" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              <svg
                class=""
                version="1.1"
                id="Слой_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] , stroke:allData.colors[5] }"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
                H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
                  c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
                  c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
                  c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
                  c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
                  c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
                  c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VG
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[6], stroke: allData.colors[7] }" 
                  d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.5,8.5
		c-0.5,0.5-0.8,1.3-0.8,2c0,0.7,0.3,1.4,0.8,2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.5,12.5
		c0.5-0.5,0.8-1.3,0.8-2c0-0.7-0.3-1.4-0.8-2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.9,6.9
		c-0.9,1-1.4,2.3-1.4,3.6c0,1.3,0.5,2.6,1.4,3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.1,14.1
		c0.9-1,1.4-2.3,1.4-3.6c0-1.3-0.5-2.6-1.4-3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.9,15.5
		c1.2-1.4,1.9-3.2,1.9-5c0-1.8-0.7-3.6-1.9-5"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.2,5.5
		c-1.2,1.4-1.9,3.2-1.9,5c0,1.8,0.7,3.6,1.9,5"
                  />
                </g>
                <rect
                  x="3"
                  y="8.1"
                  style="fill:none;"
                  width="14.6"
                  height="8.3"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.1"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.4"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VO
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] }" stroke="#FF4B35"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
	H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
		c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
		c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
		c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
		c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
		c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
		c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text transform="matrix(1 0 0 1 3.9275 14.1105)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                  <tspan
                    x="5.74"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                </text>
              </svg>
              
            </a>
                        <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС2
              <svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path :style="{ fill: allData.colors[0], stroke: allData.colors[1] }" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              <svg
                class=""
                version="1.1"
                id="Слой_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[12] , stroke:allData.colors[13] }"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
                H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
                  c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
                  c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
                  c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
                  c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
                  c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
                  c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VG
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[10], stroke: allData.colors[11] }" 
                  d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.5,8.5
		c-0.5,0.5-0.8,1.3-0.8,2c0,0.7,0.3,1.4,0.8,2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.5,12.5
		c0.5-0.5,0.8-1.3,0.8-2c0-0.7-0.3-1.4-0.8-2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.9,6.9
		c-0.9,1-1.4,2.3-1.4,3.6c0,1.3,0.5,2.6,1.4,3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.1,14.1
		c0.9-1,1.4-2.3,1.4-3.6c0-1.3-0.5-2.6-1.4-3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.9,15.5
		c1.2-1.4,1.9-3.2,1.9-5c0-1.8-0.7-3.6-1.9-5"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.2,5.5
		c-1.2,1.4-1.9,3.2-1.9,5c0,1.8,0.7,3.6,1.9,5"
                  />
                </g>
                <rect
                  x="3"
                  y="8.1"
                  style="fill:none;"
                  width="14.6"
                  height="8.3"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.1"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.4"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VO
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] }" stroke="#FF4B35"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
	H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
		c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
		c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
		c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
		c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
		c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
		c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text transform="matrix(1 0 0 1 3.9275 14.1105)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                  <tspan
                    x="5.74"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                </text>
              </svg>
            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС3
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path style="fill:#FCDBCB;stroke:#FF4B35;" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>

            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС4
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path style="fill:#FCDBCB;stroke:#FF4B35;" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              
            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС5
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path style="fill:#FCDBCB;stroke:#FF4B35;" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
             
            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС6
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path style="fill:#FCDBCB;stroke:#FF4B35;" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              

            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС7
              <svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path :style="{ fill: allData.colors[0], stroke: allData.colors[1] }" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              <svg
                class=""
                version="1.1"
                id="Слой_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] , stroke:allData.colors[5] }"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
                H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
                  c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
                  c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
                  c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
                  c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
                  c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
                  c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VG
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[6], stroke: allData.colors[7] }" 
                  d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.5,8.5
		c-0.5,0.5-0.8,1.3-0.8,2c0,0.7,0.3,1.4,0.8,2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.5,12.5
		c0.5-0.5,0.8-1.3,0.8-2c0-0.7-0.3-1.4-0.8-2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.9,6.9
		c-0.9,1-1.4,2.3-1.4,3.6c0,1.3,0.5,2.6,1.4,3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.1,14.1
		c0.9-1,1.4-2.3,1.4-3.6c0-1.3-0.5-2.6-1.4-3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.9,15.5
		c1.2-1.4,1.9-3.2,1.9-5c0-1.8-0.7-3.6-1.9-5"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.2,5.5
		c-1.2,1.4-1.9,3.2-1.9,5c0,1.8,0.7,3.6,1.9,5"
                  />
                </g>
                <rect
                  x="3"
                  y="8.1"
                  style="fill:none;"
                  width="14.6"
                  height="8.3"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.1"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.4"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VO
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] }" stroke="#FF4B35"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
	H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
		c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
		c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
		c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
		c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
		c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
		c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text transform="matrix(1 0 0 1 3.9275 14.1105)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                  <tspan
                    x="5.74"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                </text>
              </svg>
            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС8
	 
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path :style="{ fill: allData.colors[0], stroke: allData.colors[1] }" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
              <svg
                class=""
                version="1.1"
                id="Слой_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] , stroke:allData.colors[5] }"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
                H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
                  c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
                  c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
                  c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
                  c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
                  c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
                  c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VG
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[6], stroke: allData.colors[7] }" 
                  d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.5,8.5
		c-0.5,0.5-0.8,1.3-0.8,2c0,0.7,0.3,1.4,0.8,2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.5,12.5
		c0.5-0.5,0.8-1.3,0.8-2c0-0.7-0.3-1.4-0.8-2"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.9,6.9
		c-0.9,1-1.4,2.3-1.4,3.6c0,1.3,0.5,2.6,1.4,3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.1,14.1
		c0.9-1,1.4-2.3,1.4-3.6c0-1.3-0.5-2.6-1.4-3.6"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.9,15.5
		c1.2-1.4,1.9-3.2,1.9-5c0-1.8-0.7-3.6-1.9-5"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.2,5.5
		c-1.2,1.4-1.9,3.2-1.9,5c0,1.8,0.7,3.6,1.9,5"
                  />
                </g>
                <rect
                  x="3"
                  y="8.1"
                  style="fill:none;"
                  width="14.6"
                  height="8.3"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.1"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.4"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text
                  transform="matrix(1 0 0 1 3.9275 14.1105)"
                  style="font-family:'MyriadPro-Regular'; font-size:10px;"
                >
                  VO
                </text>
              </svg>
              <svg
                version="1.1"
                id="Слой_1"
                xmlns:x="&ns_extend;"
                xmlns:i="&ns_ai;"
                xmlns:graph="&ns_graphs;"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 38 21"
                style="enable-background:new 0 0 38 21;"
                xml:space="preserve"
              >
                <path
                :style="{ fill: allData.colors[4] }" stroke="#FF4B35"
                  d="M2.498,1.024h33.004c0.828,0,1.5,0.672,1.5,1.5v16.004c0,0.828-0.672,1.5-1.5,1.5
	H2.498c-0.828,0-1.5-0.672-1.5-1.5V2.524C0.998,1.695,1.67,1.024,2.498,1.024z"
                />
                <g>
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M23.507,8.532
		c-0.488,0.549-0.757,1.258-0.757,1.993c0,0.735,0.27,1.444,0.757,1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M26.525,12.519
		c0.488-0.549,0.757-1.259,0.757-1.993c0-0.735-0.27-1.444-0.757-1.993"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M21.913,6.939
		c-0.909,0.973-1.415,2.254-1.415,3.586c0,1.331,0.506,2.613,1.415,3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M28.117,14.111
		c0.909-0.973,1.415-2.254,1.415-3.586c0-1.331-0.506-2.613-1.415-3.586"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M29.876,15.525
		c1.228-1.376,1.907-3.156,1.907-5.001c0-1.845-0.679-3.625-1.907-5.001"
                  />
                  <path
                    style="fill:none;stroke:#E32112;stroke-width:1.0019;stroke-linecap:round;stroke-linejoin:round;"
                    d="M20.154,5.523
		c-1.228,1.376-1.907,3.157-1.907,5.001c0,1.845,0.679,3.625,1.907,5.001"
                  />
                </g>
                <rect
                  x="2.979"
                  y="8.106"
                  style="fill:none;"
                  width="14.638"
                  height="8.34"
                />
                <text transform="matrix(1 0 0 1 683 384)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    #1ed9
                  </tspan>
                  <tspan
                    x="31.056"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                  <tspan
                    x="36.359"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:12px;"
                  >
                    c
                  </tspan>
                </text>
                <text transform="matrix(1 0 0 1 3.9275 14.1105)">
                  <tspan
                    x="0"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                  <tspan
                    x="5.74"
                    y="0"
                    style="font-family:'MyriadPro-Regular'; font-size:10px;"
                  >
                    V
                  </tspan>
                </text>
              </svg>
            </a>

            <a href="#" class="flex bg-gray-100 mt-2 ml-8 mr-6 font-medium pl-4 items-center"
              >ПС9
<svg version="1.1" id="Слой_1" xmlns:x="&ns_extend;" xmlns:i="&ns_ai;" xmlns:graph="&ns_graphs;"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 38 21"
	 style="enable-background:new 0 0 38 21;" xml:space="preserve">
<path style="fill:#FCDBCB;stroke:#FF4B35;" d="M2.5,1h33C36.3,1,37,1.7,37,2.5v16c0,0.8-0.7,1.5-1.5,1.5h-33C1.7,20,1,19.4,1,18.5
	v-16C1,1.7,1.7,1,2.5,1z"/>
<rect x="3" y="8.1" style="fill:none;" width="14.6" height="8.3"/>
<text transform="matrix(1 0 0 1 683 384)" style="font-family:'ArialMT'; font-size:12px;">#1ed9</text>
<text transform="matrix(1 0 0 1 714.1 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 719.4 384)" style="font-family:'ArialMT'; font-size:12px;">c</text>
<text transform="matrix(1 0 0 1 7.7645 15.101)" style="font-family:'ArialMT'; font-size:10px;">T</text>
<g>
	<defs>
		<rect id="SVGID_1_" x="17.6" y="3.5" width="14" height="14"/>
	</defs>
	<clipPath id="SVGID_2_">
		<use xlink:href="#SVGID_1_"  style="overflow:visible;"/>
	</clipPath>
	<g style="clip-path:url(#SVGID_2_);">
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M26.014,11.766
			c-0.031-0.02-0.057-0.047-0.075-0.079c-0.018-0.032-0.027-0.069-0.027-0.105V5.689c0-0.348-0.138-0.682-0.384-0.928
			c-0.246-0.246-0.58-0.384-0.928-0.384c-0.348,0-0.682,0.138-0.928,0.384c-0.246,0.246-0.384,0.58-0.384,0.928v5.893
			c0,0.037-0.009,0.073-0.027,0.105c-0.018,0.032-0.043,0.059-0.074,0.079c-0.389,0.253-0.705,0.604-0.917,1.016
			c-0.212,0.413-0.312,0.874-0.292,1.337c0.031,0.685,0.329,1.331,0.83,1.799c0.501,0.468,1.166,0.722,1.851,0.706
			c0.686-0.016,1.338-0.299,1.817-0.789c0.479-0.49,0.748-1.149,0.749-1.834c0-0.444-0.11-0.881-0.322-1.271
			C26.691,12.34,26.386,12.008,26.014,11.766L26.014,11.766z"/>
		<path style="fill:none;stroke:#000000;stroke-width:1.0019;stroke-linecap:round;stroke-miterlimit:10;" d="M24.6,6.564v7.437"/>
		<path d="M24.601,15.315c0.725,0,1.313-0.588,1.313-1.314c0-0.725-0.588-1.313-1.313-1.313s-1.313,0.588-1.313,1.313
			C23.287,14.726,23.875,15.315,24.601,15.315z"/>
	</g>
</g>
</svg>
             

            </a>

            

          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  computed: mapGetters(['allData'])
  // computed: mapGetters(['allData']),
  // methods: mapActions(['GET_ALLDATA']),
  // async created() {
  //   setInterval(() => {
  //     JSON.parse(JSON.stringify(this.GET_ALLDATA()))
  //     console.log(this.allData)
  //   }, 10000)
  // }
}
</script>

<style></style>
