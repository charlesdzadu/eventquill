<template>
	<div></div>
</template>

<script setup>

import { getAuth, GoogleAuthProvider, signInWithCredential } from 'firebase/auth'
import { useAuthStore } from '~/stores/auth'

const config = useRuntimeConfig();
const authStore = useAuthStore();

useHead({
	script: [
		{
			src: 'https://accounts.google.com/gsi/client',
			async: true,
			defer: true,
		},
	],
});


onMounted(() => {
	if (authStore.isAuthenticated) {
		return;
	}
	const handleCredentialResponse = (response) => {
		if (response.credential) {
			const provider = new GoogleAuthProvider();
			const credential = GoogleAuthProvider.credential(response.credential);
			const auth = getAuth();

			signInWithCredential(auth, credential).then(async (userCredential) => {
				const user = userCredential.user;
				const token = await user.getIdToken();
				authStore.loginWithToken(token);
			})
		}
	};

	const handleOneTapError = (error) => {
		console.log(error);
	};

	google.accounts.id.initialize({
		client_id: config.public.googleAuthClientId,
		cancel_on_tap_outside: false,
		callback: handleCredentialResponse,
		auto_select: true,
		prompt_parent_id: 'google-one-tap',
		prompt_parent_hover: false,
		context: 'signin',
		state_cookie_domain: 'localhost',
		ux_mode: 'redirect',
	});
	google.accounts.id.prompt((_) => {
	}, handleOneTapError);
});


</script>
