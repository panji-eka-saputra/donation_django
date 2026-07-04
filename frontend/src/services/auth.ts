import api from './Api'
import axios from 'axios'

export async function refreshToken() {
  const refresh = localStorage.getItem('refresh')

  const res = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {
    refresh,
  })

  localStorage.setItem('access', res.data.access)

  return res.data.access
}
