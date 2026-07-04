import api from './Api'
export async function submitRegistration(registrationData: any) {
  const { data } = await api.post('/api/participant-registrations/', registrationData)
  return data
}
