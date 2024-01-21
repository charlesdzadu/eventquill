import {defineStore} from "pinia"

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
	token: null as string | null,

  }),
  getters: {
	isAuthenticated: (state) => !!state.token,
  },
  actions: {
	async loginWithToken(token: string) {
		const config = useRuntimeConfig();
		const url = new URL("/api/login", config.public.baseUrl);
		const response = await fetch(url.toString(), {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({token}),
		});
		if(response.ok) {
			this.token = token;
			console.log("Login successful");
			return true;
		}else{
			console.log("Login failed");

			return false;
		}

	},
	async logout() {
	  this.token = null;
	  const config = useRuntimeConfig();

	  const url = new URL("/api/logout", config.public.baseUrl);
	  const response = await fetch(url.toString(), {
		method: "POST",
	  });
	},
  },
})
