<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

const router = useRouter()

const form = ref({
  email: '',
  password: '',
})

async function login() {
  try {
    const res = await axios.post('http://127.0.0.1:8000/api/token/', {
      username: form.value.email,
      password: form.value.password,
    })

    // simpan token
    localStorage.setItem('access', res.data.access)
    localStorage.setItem('refresh', res.data.refresh)

    Swal.fire({
      icon: 'success',
      title: 'Login Success',
    })

    router.push('/participant')
  } catch (err) {
    console.log(err)
    Swal.fire({
      icon: 'error',
      title: 'Login Failed',
    })
  }
}
</script>
<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        class="mx-auto h-10 w-auto"
        src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600"
        alt="Your Company"
      />
      <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
        Sign in to your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="login">
        <div>
          <label for="email" class="block text-sm/6 font-medium text-gray-900">Email address</label>
          <div class="mt-2">
            <input
              v-model="form.email"
              type="email"
              name="email"
              id="email"
              autocomplete="email"
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"
                >Forgot password?</a
              >
            </div>
          </div>
          <div class="mt-2">
            <input
              v-model="form.password"
              type="password"
              name="password"
              id="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>
          <router-link
            to="/"
            class="mt-2 flex w-full justify-center rounded-md px-3 py-1.5 text-sm/6 font-semibold text-black shadow-xs hover:bg-gray-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Cancel
          </router-link>
        </div>
      </form>

      <p class="mt-10 text-center text-sm/6 text-gray-500">
        Not a member?
        {{ ' ' }}
        <router-link to="/registration" class="font-semibold text-indigo-600 hover:text-indigo-500"
          >Sign up</router-link
        >
      </p>
    </div>
  </div>
</template>
