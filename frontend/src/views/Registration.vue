<script setup lang="ts">
import Navbar from '@/components/Navbar.vue'
import { ref } from 'vue'
import { submitRegistration } from '@/services/Registration'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

const router = useRouter()

const form = ref({
  first_name: '',
  last_name: '',
  email: '',
  password: '',
  confirm_password: '',
  birthdate: '',
  phone_number: '',
  address: '',
  is_agree_to_terms: false,
})

const errors = ref({
  first_name: '',
  last_name: '',
  email: '',
  password: '',
  confirm_password: '',
  birthdate: '',
  phone_number: '',
  address: '',
  is_agree_to_terms: '',
})

function validateForm() {
  errors.value.first_name = form.value.first_name ? '' : 'First name is required'
  errors.value.last_name = form.value.last_name ? '' : 'Last name is required'
  errors.value.email = form.value.email ? '' : 'Email is required'
  errors.value.password = form.value.password ? '' : 'Password is required'
  errors.value.confirm_password = form.value.confirm_password ? '' : 'Confirm password is required'
  errors.value.birthdate = form.value.birthdate ? '' : 'Birthdate is required'
  errors.value.phone_number = form.value.phone_number ? '' : 'Phone number is required'
  errors.value.address = form.value.address ? '' : 'Address is required'
  errors.value.is_agree_to_terms = form.value.is_agree_to_terms ? '' : 'You must agree to terms'

  // age validation
  if (form.value.birthdate) {
    const today = new Date()
    const birthDate = new Date(form.value.birthdate)

    let age = today.getFullYear() - birthDate.getFullYear()
    const month = today.getMonth() - birthDate.getMonth()

    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
      age--
    }

    if (age < 18) {
      errors.value.birthdate = 'You must be at least 18 years old'
    }
  }

  return Object.values(errors.value).every((e) => e === '')
}

async function submitForm() {
  if (!validateForm()) return

  if (form.value.password !== form.value.confirm_password) {
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: 'Please input the same password!',
    })
    return
  }

  try {
    await submitRegistration(form.value)

    await Swal.fire({
      icon: 'success',
      title: 'Success',
      text: 'Registration successful',
    })

    router.push('/login')

    form.value = {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      confirm_password: '',
      birthdate: '',
      phone_number: '',
      address: '',
      is_agree_to_terms: false,
    }
  } catch (error: any) {
    const data = error?.response?.data

    const message = data
      ? Object.entries(data)
          .map(([k, v]) => `${k}: ${(v as string[]).join(', ')}`)
          .join('\n')
      : 'Something went wrong'

    Swal.fire({
      icon: 'error',
      title: 'Registration Failed',
      text: message,
    })
  }
}
</script>

<template>
  <Navbar />
  <form @submit.prevent="submitForm" class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
    <div class="border-b border-gray-900/10 pb-12 mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <h2 class="text-base/7 font-semibold text-gray-900 mt-10">Participant Registration</h2>
      <p class="mt-1 text-sm/6 text-gray-600">
        Please fill out the following information to participant registration.
      </p>

      <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
        <div class="sm:col-span-3">
          <label for="first_name" class="block text-sm/6 font-medium text-gray-900"
            >First Name</label
          >
          <div class="mt-2">
            <input
              v-model="form.first_name"
              type="text"
              name="first_name"
              id="first_name"
              autocomplete="first-name"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.first_name
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.first_name" class="error-text">{{ errors.first_name }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="last_name" class="block text-sm/6 font-medium text-gray-900">Last Name</label>
          <div class="mt-2">
            <input
              v-model="form.last_name"
              type="text"
              name="last_name"
              id="last_name"
              autocomplete="last-name"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.first_name
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.last_name" class="error-text">{{ errors.last_name }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="birthdate" class="block text-sm/6 font-medium text-gray-900">Birthdate</label>
          <div class="mt-2">
            <input
              v-model="form.birthdate"
              type="date"
              name="birthdate"
              id="birthdate"
              autocomplete="bday"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.birthdate
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.birthdate" class="error-text">{{ errors.birthdate }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="email" class="block text-sm/6 font-medium text-gray-900">Email</label>
          <div class="mt-2">
            <input
              v-model="form.email"
              type="text"
              name="email"
              id="email"
              autocomplete="email"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.first_name
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.email" class="error-text">{{ errors.email }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
          <div class="mt-2">
            <input
              v-model="form.password"
              type="password"
              name="password"
              id="password"
              autocomplete="password"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.password
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.password" class="error-text">{{ errors.password }}</p>
          </div>
        </div>
        <div class="sm:col-span-3">
          <label for="confirm_password" class="block text-sm/6 font-medium text-gray-900"
            >Confirm Password</label
          >
          <div class="mt-2">
            <input
              v-model="form.confirm_password"
              type="password"
              name="confirm_password"
              id="confirm_password"
              autocomplete="confirm_password"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.confirm_password
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.confirm_password" class="error-text">{{ errors.confirm_password }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="phone_number" class="block text-sm/6 font-medium text-gray-900"
            >Phone Number</label
          >
          <div class="mt-2">
            <input
              v-model="form.phone_number"
              type="text"
              name="phone_number"
              id="phone_number"
              autocomplete="tel"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.first_name
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.phone_number" class="error-text">{{ errors.phone_number }}</p>
          </div>
        </div>

        <div class="sm:col-span-3">
          <label for="address" class="block text-sm/6 font-medium text-gray-900">Address</label>
          <div class="mt-2">
            <input
              v-model="form.address"
              type="text"
              name="address"
              id="address"
              autocomplete="street-address"
              :class="[
                'block w-full rounded-md bg-white px-3 py-1.5 text-base placeholder:text-gray-400 sm:text-sm/6',
                errors.first_name
                  ? 'border border-red-500 focus:ring-red-500 focus:border-red-500'
                  : 'border border-gray-300 focus:border-indigo-600',
              ]"
            />
            <p v-if="errors.address" class="error-text">{{ errors.address }}</p>
          </div>
        </div>
        <div class="sm:col-span-6">
          <label for="agree-to-terms" class="flex items-center gap-3 cursor-pointer">
            <input
              id="agree-to-terms"
              v-model="form.is_agree_to_terms"
              type="checkbox"
              name="agree-to-terms"
              :class="[
                'h-4 w-4 rounded focus:ring-2',
                errors.is_agree_to_terms
                  ? 'border-red-500 text-red-600 focus:ring-red-500'
                  : 'border-gray-300 text-indigo-600 focus:ring-indigo-600',
              ]"
            />

            <span class="text-sm font-medium text-gray-900">
              Agree to our Terms and Conditions and Privacy Policy.
            </span>
          </label>

          <p v-if="errors.is_agree_to_terms" class="mt-2 text-sm text-red-600">
            {{ errors.is_agree_to_terms }}
          </p>
        </div>
      </div>
      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button type="button" class="text-sm/6 font-semibold text-gray-900">Cancel</button>
        <button
          type="submit"
          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Register
        </button>
      </div>
    </div>
  </form>
</template>
