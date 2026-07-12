<script setup lang="ts">
import { ref, onMounted } from 'vue'

import { useRoute, useRouter } from 'vue-router'

import { getDonationSuccess } from '../services/Donation'

const route = useRoute()
const router = useRouter()

const donation = ref({
  first_name: '',

  last_name: '',

  email: '',

  amount: '',

  status: '',

  donated_at: '',
})

async function loadDonation() {
  const sessionId = route.query.session_id as string

  donation.value = await getDonationSuccess(sessionId)
}

function goToProfile() {
  router.push('/participant')
}

onMounted(loadDonation)
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white rounded-lg shadow-lg p-10 w-[600px]">
      <h1 class="text-3xl font-bold text-green-600">Payment Successful</h1>

      <div class="mt-8 space-y-4">
        <div>
          <strong>Name :</strong>
          {{ donation.first_name }}
          {{ donation.last_name }}
        </div>

        <div>
          <strong>Email :</strong>
          {{ donation.email }}
        </div>

        <div>
          <strong>Amount :</strong>
          Rp {{ donation.amount }}
        </div>

        <div>
          <strong>Status :</strong>
          {{ donation.status }}
        </div>

        <div>
          <strong>Donation Date :</strong>
          {{ donation.donated_at }}
        </div>
      </div>

      <!-- Button -->
      <div class="mt-10 flex justify-end">
        <button
          @click="goToProfile"
          class="rounded-md bg-indigo-600 px-6 py-2 text-white font-semibold hover:bg-indigo-500 transition mr-4"
        >
          Go Back to Profile
        </button>

        <button
          @click="router.push('/donation')"
          class="rounded-md border border-gray-300 px-6 py-2 hover:bg-gray-100"
        >
          Donate Again
        </button>
      </div>
    </div>
  </div>
</template>
