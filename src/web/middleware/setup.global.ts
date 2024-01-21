import {useAuthStore} from "~/stores/auth"

export default defineNuxtRouteMiddleware((to, from) => {
	const authStore = useAuthStore();

	const token = useCookie('token').value;
	if (token) {
		authStore.token = token;
		authStore.loginWithToken(token);
	}
})
