//MAIN LANDING PAGE//
import logoIcon from '../../images/spotspector-icon.svg'
import authorLogo from '../../images/author-logo.png'
import authorLogo2 from '../../images/author-logo2.png'

function Navbar() {
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

        <button className="login-btn">Log in</button>
       </div>
     </div>
   )
}

function Hero() {
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

      <button className="enjoy">Join & Enjoy</button>
    </section>
  )
}

function Artists() {
  return (
    <section className="artists">
      <h2>Popular Artists</h2>

      <div className="artist-container">
        <a href="">
          <img src="" alt="" />
          <p>1</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>2</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>3</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>4</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>5</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>6</p>
        </a>
      </div>
    </section>
  )
}

function Albums() {
  return (
    <section className="albums">
      <h2>Albums</h2>

      <div className="album-container">
        <a href="">
          <img src="" alt="" />
          <p>album1</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>album2</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>album3</p>
        </a>
        <a href="">
          <img src="" alt="" />
          <p>album4</p>
        </a>
      </div>
     </section>
   )
}


export default function RenderLandingPage() {
  return (
    <div className="children">
    <Navbar />
    <Hero/>
    <Artists />
    <Albums/>
    </div>
  )
}
