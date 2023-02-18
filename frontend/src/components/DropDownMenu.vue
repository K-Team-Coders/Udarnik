<template>
  <body>
    <div class="flex-row ml-3 mt-2">
      <div class="flex-row mt-3">
        <button
          id="dropdownSearchButton"
          data-dropdown-toggle="dropdownSearch"
          class="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-black bg-gray-50 outline outline-1 outline-orange-500  hover:bg-orange-500 hover:text-white"
          type="button"
        >
          Dropdown search
          <svg
            class="w-4 h-4 ml-2"
            aria-hidden="true"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 9l-7 7-7-7"
            ></path>
          </svg>
        </button>
        <!-- Dropdown menu -->
        <div
          id="dropdownSearch"
          class="z-10 bg-gray-50 rounded-lg shadow w-60 "
        >
          <div class="p-3">
            <label for="input-group-search" class="sr-only">Search</label>
          </div>
          <ul
            class="px-3 pb-3 overflow-y-auto text-sm text-gray-700"
            aria-labelledby="dropdownSearchButton"
          >
            <li>
              <div class="flex items-center p-2 rounded hover:bg-gray-100 ">
                <input
                  id="checkbox-item-11"
                  type="checkbox"
                  value=""
                  class="w-4 h-4 text-orange-600 bg-gray-100 border-gray-300 rounded"
                />
                <label
                  for="checkbox-item-11"
                  class="w-full ml-2 text-sm font-medium text-gray-900 rounded"
                  >Bonnie Green</label
                >
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="flex-row mt-3">
        <button
          id="dropdownSearchButton"
          data-dropdown-toggle="dropdownSearch"
          class="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-black bg-gray-50 outline outline-1 outline-orange-500  hover:bg-orange-500 hover:text-white"
          type="button"
        >
          Dropdown search
          <svg
            class="w-4 h-4 ml-2"
            aria-hidden="true"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 9l-7 7-7-7"
            ></path>
          </svg>
        </button>
        <!-- Dropdown menu -->
        <div
          id="dropdownSearch"
          class="z-10 bg-gray-50 rounded-lg shadow w-60 "
        >
          <div class="p-3">
            <label for="input-group-search" class="sr-only">Search</label>
          </div>
          <ul
            class="px-3 pb-3 overflow-y-auto text-sm text-gray-700"
            aria-labelledby="dropdownSearchButton"
          >
            <li>
              <div class="flex items-center p-2 rounded hover:bg-gray-100 ">
                <input
                  id="checkbox-item-11"
                  type="checkbox"
                  value=""
                  class="w-4 h-4 text-orange-600 bg-gray-100 border-gray-300 rounded"
                />
                <label
                  for="checkbox-item-11"
                  class="w-full ml-2 text-sm font-medium text-gray-900 rounded"
                  >Bonnie Green</label
                >
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </body>
</template>
