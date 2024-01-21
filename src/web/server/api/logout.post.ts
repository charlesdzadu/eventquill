export default defineEventHandler(async (event) => {
	try {
	  setCookie(event, 'token', '', {
		maxAge: 0,
		httpOnly: true,
		secure: true,
		sameSite: 'none',
	  } as const);
	  return {
		status: 200,
		body: JSON.stringify({ status: 'success' }),
	  };
	} catch (error) {
	  return {
		status: 401,
		error: 'UNAUTHORIZED',
		message: 'Failed to delete  cookie',
	  };
	}
  });
