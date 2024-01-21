export default defineEventHandler(async (event) => {
	const {token} = await readBody(event);
	const expiresIn = 60 * 60 * 24 * 7; // 7 days

	const options = {
		httpOnly: true,
		secure: true,
		path: "/",
		maxAge: expiresIn,
	}

	try {
		setCookie(event, "token", token, options);
		return new Response(null, {status: 200, statusText: "OK"});
	}catch(e){
		return new Response(null, {status: 500, statusText: "Internal Server Error"});
	}
})
