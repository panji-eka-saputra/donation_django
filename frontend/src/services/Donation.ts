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
