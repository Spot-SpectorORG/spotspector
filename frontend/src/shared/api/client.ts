const BASE_URL = '/api/v1';

type LoginInput = {
  username: string;
  password: string;
}

export async function RequestLogin(data: LoginInput) {
  const response = await fetch(`${BASE_URL}/users/login/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  if (!response.ok) {
        throw new Error(`Response Error: ${response.status}`)
  } else {
    return response.json()
     }
}
