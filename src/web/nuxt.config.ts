// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],
  plugins: ['~/plugins/firebase.client.ts'],
  runtimeConfig: {
	public: {
		googleAuthClientId: process.env.GOOGLE_AUTH_CLIENT_ID,
		googleAuthClientSecret: process.env.GOOGLE_AUTH_CLIENT_SECRET,
		baseUrl: process.env.BASE_URL,
	}
  }
})
