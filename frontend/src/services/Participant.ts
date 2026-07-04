import api from './Api'

export const getParticipantsProfile = async () => {
  try {
    const { data } = await api.get('/api/participant/me/')
    return data
  } catch (error) {
    console.error('Error fetching participants:', error)
    throw error
  }
}

export const updateParticipantsProfile = async (profileData: any) => {
  try {
    const { data } = await api.put('/api/participant/me/', profileData)
    return data
  } catch (error) {
    console.error('Error updating participants profile:', error)
    throw error
  }
}
