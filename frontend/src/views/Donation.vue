<script setup lang="ts">
import Navbar from '../components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { getDonationProfile, createDonation } from '../services/Donation'

const profile = ref({
  first_name: '',
  last_name: '',
  birthdate: '',
  email: '',
  phone_number: '',
  address: '',
})

const donation = ref({
  amount: '',
  agree: false,
})

const loading = ref(false)

async function fetchProfile() {
  try {
    const response = await getDonationProfile()
    profile.value = response
  } catch (error) {
    console.error(error)
  }
}

async function submitDonation() {
  if (!donation.value.amount) {
    alert('Please enter donation amount.')
    return
  }

  if (!donation.value.agree) {
    alert('Please agree to Terms and Conditions.')
    return
  }

  loading.value = true

  try {
    const response = await createDonation({
      amount: donation.value.amount,
    })

    window.location.href = response.checkout_url

    console.log(response)

    // alert('Donation created successfully.')

    // Jika Stripe mengembalikan checkout_url
    // window.location.href = response.checkout_url
  } catch (error) {
    console.error(error)
    alert('Failed to create donation.')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProfile()
})
</script>

<template>
  <Navbar />

  <form @submit.prevent="submitDonation">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <!-- Participant -->
      <div class="border-b border-gray-300 pb-10">
        <h2 class="mt-5 text-xl font-semibold">Participant Information</h2>

        <p class="text-gray-500">Your personal information.</p>

        <div class="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> First Name </label>

            <input
              v-model="profile.first_name"
              readonly
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Last Name </label>

            <input
              v-model="profile.last_name"
              readonly
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Birthdate </label>

            <input
              v-model="profile.birthdate"
              readonly
              type="date"
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Email </label>

            <input
              v-model="profile.email"
              readonly
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Phone Number </label>

            <input
              v-model="profile.phone_number"
              readonly
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Address </label>

            <input
              v-model="profile.address"
              readonly
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>
        </div>
      </div>

      <!-- Donation -->
      <div class="mt-10">
        <h2 class="text-xl font-semibold">Donation Information</h2>

        <p class="text-gray-500">Enter your donation amount.</p>

        <div class="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <label class="block text-sm font-medium"> Donation Amount </label>

            <input
              v-model="donation.amount"
              type="number"
              min="1"
              step="0.01"
              placeholder="100000"
              class="mt-2 block w-full rounded-md border px-3 py-2"
            />
          </div>

          <div class="sm:col-span-6">
            <label class="flex items-center gap-3">
              <input v-model="donation.agree" type="checkbox" />

              <span> I agree to the Terms and Conditions. </span>
            </label>
          </div>
        </div>
      </div>

      <div class="mt-10 flex justify-end gap-4">
        <button type="button" class="rounded-md border px-5 py-2">Cancel</button>

        <button
          type="submit"
          :disabled="loading"
          class="rounded-md bg-indigo-600 px-5 py-2 text-white hover:bg-indigo-500 disabled:bg-gray-400"
        >
          {{ loading ? 'Processing...' : 'Donate' }}
        </button>
      </div>
    </div>
  </form>
</template>
