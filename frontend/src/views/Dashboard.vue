<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Dialog, DialogPanel } from '@headlessui/vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import bgImage from '@/assets/images/dashboard.jpg'
import Login from './Login.vue'

const navigation = [
  { name: 'Participants', href: '#' },
  { name: 'Contact Us', href: '#' },
  { name: 'Company', href: '#' },
]
</script>
<template>
  <div
    class="h-full w-full min-h-screen overflow-auto bg-cover bg-center"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <header class="absolute inset-x-0 top-0 z-50">
      <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1"></div>
        <div class="hidden lg:flex lg:gap-x-12">
          <a
            v-for="item in navigation"
            :key="item.name"
            :href="item.href"
            class="text-sm/6 font-bold text-white"
            >{{ item.name }}</a
          >
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end"></div>
      </nav>
    </header>

    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div
        class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%-11rem)] aspect-1155/678 w-144.5 -translate-x-1/2 rotate-30 bg-linear-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-288.75"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        ></div>
      </div>
      <div class="mx-auto max-w-2xl py-24 sm:py-48 lg:py-75">
        <div class="text-center">
          <h1 class="text-3xl font-bold tracking-tight text-balance text-white sm:text-7xl">
            Welcome to Donation Project
          </h1>
          <p class="mt-8 text-lg font-medium text-white text-black-400 sm:text-xl/8">
            Every contribution brings us closer to our goal.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <router-link
              to="/login"
              class="rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
              >Get started</router-link
            >
          </div>
        </div>
      </div>
      <div
        class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%+3rem)] aspect-1155/678 w-144.5 -translate-x-1/2 bg-linear-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-288.75"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        ></div>
      </div>
    </div>
  </div>
</template>
