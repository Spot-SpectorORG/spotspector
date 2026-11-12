import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import RenderLandingPage from '../pages/LandingIntro'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    <RenderLandingPage/>
  </StrictMode>,
)
