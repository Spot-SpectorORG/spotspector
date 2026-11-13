import * as z from 'zod'
import { useState } from 'react'
import {RequestLogin} from '../../shared/api/client'
import {useAuthStore} from '../../features/auth/authStore'

const LOGIN_SCHEMA = z.object({
  username: z.string().min(1, 'Required!'),
  password: z.string().min(1, 'Required!'),
})


type LoginInput = z.infer<typeof LOGIN_SCHEMA>
type ErrorInput = Partial<Record<string, string>>

export default function LoginForm({onClose}: {onClose: () => void}) {
  const [input, setInput] = useState<LoginInput>({username: '', password: ''})
  const [error, setError] = useState<ErrorInput>({})
  const login = useAuthStore((state) => state.login)

 async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const result = LOGIN_SCHEMA.safeParse(input);

    if (!result.success) {
      const fieldErrors = result.error.flatten().fieldErrors;
      setError({
            username: fieldErrors.username?.[0],
            password: fieldErrors.password?.[0],
          });
    } else {
      setError({});
      try {
        const data = await RequestLogin(result.data)
        console.log('Data:', data)
        login(data.access, data.refresh)
       }
      catch(err) {
           setError({final: 'Wrong password or username' })
         }
     }
  }


  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="login-modal" onClick={(e) => e.stopPropagation()}>
        <button type="button" className="close-btn" onClick={onClose}>×</button>

        <h2>Log in to SpotSpector rigth now!</h2>

        <form onSubmit={handleSubmit} className="login-form">
          <div className="login-inputs">

            <div className="input-group">
              <label htmlFor="username">Username</label>
              <input type="text" name="username" placeholder="Enter your name..." value={input.username} onChange={(e) => setInput({ ...input, username: e.target.value })} />
              {error.username && <span className="error-text">{error.username}</span>}
            </div>

            <div className="input-group">
              <label htmlFor="password">Password</label>
              <input type='password' placeholder="Enter your password..." name="password" value={input.password} onChange={(e) => setInput({ ...input, password: e.target.value })} />
              {error.password && <span className="error-text">{error.password}</span>}
            </div>
          </div>

          <button className="submit-btn" type="submit">Submit</button>
          {error.final && <p className="error-final">{error.final}</p>}
        </form>
      </div>
    </div>
  )
}
