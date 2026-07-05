import api from './Api'

export const getDonationProfile = async () => {
  try {
    const { data } = await api.get('/api/donation/me/')
    return data
  } catch (error) {
    console.error('Error fetching donation profile:', error)
    throw error
  }
}

export const createDonation = async (payload: any) => {
  try {
    const { data } = await api.post('/api/donation/create/', payload)
    return data
  } catch (error) {
    console.error('Error creating donation:', error)
    throw error
  }
}
