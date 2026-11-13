//MAIN LANDING PAGE//
import logoIcon from '../../images/spotspector-icon.svg'
import authorLogo from '../../images/author-logo.png'
import authorLogo2 from '../../images/author-logo2.png'
import LoginForm from '../features/auth/LoginUser'
import { useAuthStore } from '../features/auth/authStore'
import {useState} from 'react'

function Navbar({onOpenLogin}: {onOpenLogin: () => void}) {
  const { isAuth, logout } = useAuthStore()

  return (
    <div className="navbar">
      <div className="nav">
        <div className="nav-logo">
          <img  className="logo" src={logoIcon} alt="Logo" />
          <p>SpotSpector</p>
        </div>
        <div className="nav-links">
          <a href="">Home</a>
          <a href="">About</a>
          <a href="">Contact</a>
        </div>

        {isAuth ? <button className="login-btn" onClick={logout}>Log out</button> : <button className="login-btn" onClick={onOpenLogin}>Log in</button> }
       </div>
     </div>
   )
}

function Hero() {
  const handleScroll = () => {
    document.getElementById('albums')?.scrollIntoView({behavior: 'smooth'})
  }

  return (
    <section className="hero">
      <div className="hero-parent">
        <div className="about">
          <h1>SpotSpector</h1>
          <ul>
            <li>Join bllalalalalalaallalalalalalalalalalalalallalla</li>
            <li>Findlalalalalalalalalalalala</li>
            <li>Listenlalalalalalalalalalaallaallalaal</li>
            <li>Enjoylalalalallalalalalalallalalalalalala</li>
          </ul>
        </div>
        <div className="contibutors">
          <div className="avatars">
            <a href="https://github.com/Roman-Belyi">
              <img src={authorLogo} alt="Kopliton1" />
            </a>
            <a href="https://github.com/kapusta123b">
              <img src={authorLogo2} alt="kapusta123" />
            </a>
          </div>
          <h2>Contributors</h2>
        </div>
      </div>

      <button className="enjoy" onClick={handleScroll}>Join & Enjoy</button>
    </section>
  )
}

function Artists() {
  return (
    <section className="artists">
      <h2>Popular Artists</h2>

      <div className="artist-container">
        <a href="">
          <img src={undefined} alt="" />
          <p>1</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>2</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>3</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>4</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>5</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>6</p>
        </a>
      </div>
    </section>
  )
}

function Albums() {
  return (
    <section className="albums" id="albums">
      <h2>Albums</h2>

      <div className="album-container">
        <a href="">
          <img src={undefined} alt="" />
          <p>album1</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>album2</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>album3</p>
        </a>
        <a href="">
          <img src={undefined} alt="" />
          <p>album4</p>
        </a>
      </div>
     </section>
   )
}


export default function RenderLandingPage() {
  const [isOpen, setIsOpen] = useState(false);
  const isAuth = useAuthStore((state) => state.isAuth)

  return (
    <div className="children">
      <Navbar onOpenLogin={() => setIsOpen(true)}/>
    <Hero/>
    <Artists />
      <Albums />
      {isOpen && !isAuth && <LoginForm onClose={() => setIsOpen(false)} />}

    </div>
  )
}
