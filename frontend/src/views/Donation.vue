<script setup lang="ts">
import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid'
import { ChevronDownIcon } from '@heroicons/vue/16/solid'
import Navbar from '../components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { getDonationProfile } from '../services/Donation.ts'

const profile = ref({
  first_name: '',
  last_name: '',
  birthdate: '',
  email: '',
  phone_number: '',
  address: '',
})

async function fetchProfile() {
  try {
    const response = await getDonationProfile()
    profile.value = response
  } catch (error) {
    console.error('Error fetching profile:', error)
  }
}

onMounted(() => {
  fetchProfile()
})
</script>
<template>
  <Navbar />
  <form @abort="">
    <div class="border-gray-900/10 pb-12 mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="border-b border-gray-900/10 pb-12">
        <h2 class="text-base/7 font-semibold text-gray-900 mt-4">Personal Information</h2>
        <p class="mt-1 text-sm/6 text-gray-600">Participant Donation Information</p>

        <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <label for="first-name" class="block text-sm/6 font-medium text-gray-900"
              >First name</label
            >
            <div class="mt-2">
              <input
                v-model="profile.first_name"
                type="text"
                name="first-name"
                id="first-name"
                autocomplete="given-name"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="last-name" class="block text-sm/6 font-medium text-gray-900"
              >Last name</label
            >
            <div class="mt-2">
              <input
                v-model="profile.last_name"
                type="text"
                name="last-name"
                id="last-name"
                autocomplete="family-name"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="birthdate" class="block text-sm/6 font-medium text-gray-900"
              >Birthdate</label
            >
            <div class="mt-2">
              <input
                v-model="profile.birthdate"
                type="date"
                name="birthdate"
                id="birthdate"
                autocomplete="birthdate"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="email" class="block text-sm/6 font-medium text-gray-900">Email</label>
            <div class="mt-2">
              <input
                v-model="profile.email"
                type="text"
                name="email"
                id="email"
                autocomplete="email"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="phone_number" class="block text-sm/6 font-medium text-gray-900"
              >Phone Number</label
            >
            <div class="mt-2">
              <input
                v-model="profile.phone_number"
                type="text"
                name="phone_number"
                id="phone_number"
                autocomplete="phone_number"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="address" class="block text-sm/6 font-medium text-gray-900">Address</label>
            <div class="mt-2">
              <input
                v-model="profile.address"
                type="text"
                name="address"
                id="address"
                autocomplete="address"
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-6">
            <label for="agree-to-terms" class="flex items-center gap-3 cursor-pointer">
              <input
                id="agree-to-terms"
                type="checkbox"
                name="agree-to-terms"
                class="h-4 w-4 rounded focus:ring-2 border-gray-300 text-indigo-600 focus:ring-indigo-600"
              />

              <span class="text-sm font-medium text-gray-900">
                Agree to our Terms and Conditions and Privacy Policy.
              </span>
            </label>
          </div>
        </div>
      </div>
      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button type="button" class="text-sm/6 font-semibold text-gray-900">Cancel</button>
        <button
          type="submit"
          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Donate
        </button>
      </div>
    </div>
  </form>
</template>
