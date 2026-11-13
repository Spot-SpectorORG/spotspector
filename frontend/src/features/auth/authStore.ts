import { create } from 'zustand'
import { persist } from 'zustand/middleware'

type AuthState = {
  isAuth: boolean,
  login: (access: string, refresh: string) => void,
  logout: () => void,
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      isAuth: Boolean(localStorage.getItem('access')),
      login: (access, refresh) => {
        localStorage.setItem('access', access);
          localStorage.setItem('refresh', refresh)
        set({isAuth: true})
      },
      logout: () => {
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        set({isAuth: false})
      }
    }),
   {
    name: 'auth-store',
   }
  )
)
