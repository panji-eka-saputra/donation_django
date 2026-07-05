<script setup lang="ts">
import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid'
import { ChevronDownIcon } from '@heroicons/vue/16/solid'
import Navbar from '../components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { getParticipantsProfile, updateParticipantsProfile } from '../services/Participant.ts'
import swal from 'sweetalert2'

const profile = ref({
  first_name: '',
  last_name: '',
  birthdate: '',
  email: '',
  phone_number: '',
  address: '',
  total_donation: '',
  total_transactions: '',
})

async function fetchProfile() {
  try {
    const response = await getParticipantsProfile()
    profile.value = response
  } catch (error) {
    console.error('Error fetching profile:', error)
  }
}

async function updateProfile() {
  try {
    await updateParticipantsProfile(profile.value)
    swal.fire({
      icon: 'success',
      title: 'Profile Updated',
    })
  } catch (error) {
    console.error('Error updating profile:', error)
    swal.fire({
      icon: 'error',
      title: 'Profile Update Failed',
    })
  }
}

onMounted(() => {
  fetchProfile()
})
</script>
<template>
  <Navbar />
  <form @submit.prevent="updateProfile">
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
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
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="total_donation" class="block text-sm/6 font-medium text-gray-900"
              >Total Donation</label
            >
            <div class="mt-2">
              <input
                v-model="profile.total_donation"
                type="text"
                name="total_donation"
                id="total_donation"
                autocomplete="total_donation"
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                readonly
              />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="total_transaction" class="block text-sm/6 font-medium text-gray-900"
              >Total Transaction</label
            >
            <div class="mt-2">
              <input
                v-model="profile.total_transactions"
                type="text"
                name="total_transaction"
                id="total_transaction"
                autocomplete="total_transaction"
                class="mt-2 block w-full rounded-md border border-black-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                readonly
              />
            </div>
          </div>
        </div>
      </div>
      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button type="button" class="text-sm/6 font-semibold text-gray-900">Cancel</button>
        <button
          type="submit"
          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Update
        </button>
      </div>
    </div>
  </form>
</template>
