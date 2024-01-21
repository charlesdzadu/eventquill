import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getAnalytics } from 'firebase/analytics';
import firebaseConfig from '~/firebase_config.json';

export default defineNuxtPlugin((nuxtApp) => {
    const firebaseApp = initializeApp(firebaseConfig);
    const auth = getAuth(firebaseApp);
    const analytics = getAnalytics(firebaseApp);

    nuxtApp.vueApp.provide('auth', auth);
    nuxtApp.provide('auth', auth);

    nuxtApp.vueApp.provide('analytics', analytics);
    nuxtApp.provide('analytics', analytics);
});
