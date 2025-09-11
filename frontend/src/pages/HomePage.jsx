import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import steamLogo from '../assets/steamLogo.png';
import searchSteam from '../assets/searchSteam.png';
import humanbg from '../assets/humanbg.png';
import humancard from '../assets/humancard.png';
import jogo1 from '../assets/jogo1.png';
import jogo2 from '../assets/jogo2.png';
import jogo3 from '../assets/jogo3.png';
import jogo4 from '../assets/jogo4.png';
import Playbutton from '../assets/Playbutton.png';
import apiService from '../services/api';
import './HomePage.css';

function HomePage() {
  const navigate = useNavigate();
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const user = apiService.getCurrentUser();
    if (!user) {
      navigate('/');
    } else {
      setCurrentUser(user);
    }
  }, [navigate]);

  const handleVerDetalhes = () => {
    navigate('/details');
  };

  const handlePlay = () => {
    // Navigate to play page (not created yet)
    console.log('Navigate to play page');
  };

  const handleLogout = () => {
    apiService.logout();
    navigate('/');
  };

  return (
    <div className="home-container">
      {/* Top Navigation */}
      <div className="top-nav">
        <div className="nav-left">
          <img src={steamLogo} alt="Steam Logo" className="nav-logo" />
          <nav className="nav-links">
            <a href="#" className="nav-link active">Your Store</a>
            <a href="#" className="nav-link">New & Noteworthy</a>
            <a href="#" className="nav-link">Categories</a>
            <a href="#" className="nav-link">Points Shop</a>
            <a href="#" className="nav-link">News</a>
            <a href="#" className="nav-link">Labs</a>
          </nav>
        </div>
        <div className="nav-right">
          <div className="search-container">
            <img src={searchSteam} alt="Search" className="search-icon" />
            <input type="text" placeholder="Search..." className="search-input" />
          </div>
          {currentUser && (
            <div className="user-info">
              <span className="user-name">Olá, {currentUser.name}!</span>
              <button onClick={handleLogout} className="logout-button">
                Logout
              </button>
            </div>
          )}
        </div>
      </div>

      <div className="main-content">
        {/* Left Sidebar */}
        <div className="sidebar">
          <div className="sidebar-section">
            <h3 className="sidebar-title">RECOMMENDED</h3>
            <ul className="sidebar-list">
              <li><a href="#" className="sidebar-link">By Friends</a></li>
              <li><a href="#" className="sidebar-link">By Curators</a></li>
              <li><a href="#" className="sidebar-link">Tags</a></li>
            </ul>
          </div>

          <div className="sidebar-section">
            <h3 className="sidebar-title">BROWSE CATEGORIES</h3>
            <ul className="sidebar-list">
              <li><a href="#" className="sidebar-link">Top Sellers</a></li>
              <li><a href="#" className="sidebar-link">New Releases</a></li>
              <li><a href="#" className="sidebar-link">Upcoming</a></li>
              <li><a href="#" className="sidebar-link">Specials</a></li>
              <li><a href="#" className="sidebar-link">VR Titles</a></li>
              <li><a href="#" className="sidebar-link">Controller-Friendly</a></li>
              <li><a href="#" className="sidebar-link">Great on Deck</a></li>
            </ul>
          </div>

          <div className="sidebar-section">
            <h3 className="sidebar-title">BROWSE BY GENRE</h3>
            <ul className="sidebar-list">
              <li><a href="#" className="sidebar-link">Free To Play</a></li>
              <li><a href="#" className="sidebar-link">Early Access</a></li>
              <li><a href="#" className="sidebar-link">Action</a></li>
              <li><a href="#" className="sidebar-link">Adventure</a></li>
              <li><a href="#" className="sidebar-link">Casual</a></li>
              <li><a href="#" className="sidebar-link">Indie</a></li>
              <li><a href="#" className="sidebar-link">Massively Multiplayer</a></li>
              <li><a href="#" className="sidebar-link">Racing</a></li>
              <li><a href="#" className="sidebar-link">RPG</a></li>
              <li><a href="#" className="sidebar-link">Simulation</a></li>
              <li><a href="#" className="sidebar-link">Sports</a></li>
              <li><a href="#" className="sidebar-link">Strategy</a></li>
            </ul>
          </div>
        </div>

        {/* Main Content Area */}
        <div className="content-area">
          {/* Featured & Recommended Section */}
          <div className="featured-section">
            <h2 className="section-title">FEATURED & RECOMMENDED</h2>
            <div className="featured-game">
              <div className="game-banner">
                <img src={humanbg} alt="HUMAN.EXE" className="banner-image" />
                <div className="banner-overlay">
                  <h1 className="game-title">HUMAN.EXE</h1>
                </div>
              </div>
              <div className="game-info">
                <h3 className="game-name">HUMAN.EXE</h3>
                <p className="game-description">
                  A IA dominou o mundo, e agora voce e seus amigos sao os ultimos pingos de esperanca que sobrou na terra. 
                  Seja forte nessa batalha e demote a IA em jogos com uma mistura de cyberpunk e emocao humana.
                </p>
                <div className="game-details">
                  <div className="review-info">
                    <span className="review-label">ANÁLISES RECENTES</span>
                    <span className="review-rating">Extremamente Positivas</span>
                    <span className="review-count">(130.201)</span>
                  </div>
                  <div className="release-info">
                    <span className="release-label">DATA DE LANÇAMENTO:</span>
                    <span className="release-date">10/09/2025</span>
                  </div>
                  <div className="developer-info">
                    <span className="dev-label">DESENVOLVEDOR:</span>
                    <span className="dev-name">ANWPY+V</span>
                  </div>
                  <div className="publisher-info">
                    <span className="pub-label">DISTRIBUIDORA:</span>
                    <span className="pub-name">ANWPY+V</span>
                  </div>
                </div>
                <button onClick={handleVerDetalhes} className="details-button">
                  Ver detalhes
                </button>
              </div>
            </div>
          </div>

          {/* Continue Playing Section */}
          <div className="continue-section">
            <h2 className="section-title">CONTINUE JOGANDO</h2>
            <div className="game-carousel">
              <div className="game-tile robot-tile">
                <img src={humancard} alt="HUMAN.EXE" className="tile-image" />
                <div className="tile-overlay">
                    <div className="time-played">
                  <div className="play-info">
                    <button onClick={handlePlay} className="play-button-overlay">
                      <img src={Playbutton} alt="Play" className="play-icon-overlay" />
                    </button>
                    <div classname="time-row">
                      <div>TIME PLAYED</div>
                      <div>0.5h</div>
                      </div>
                    </div>
                </div>
              </div>
                  </div>
              <div className="game-tile">
                <img src={jogo1} alt="ELLDIVERS" className="tile-image" />
                <div className="tile-overlay">
                </div>
              </div>
              <div className="game-tile">
                <img src={jogo2} alt="MAN'S" className="tile-image" />
                <div className="tile-overlay">
                </div>
              </div>
              <div className="game-tile">
                <img src={jogo3} alt="PUBG" className="tile-image" />
                <div className="tile-overlay">
                </div>
              </div>
              <div className="game-tile">
                <img src={jogo4} alt="Racing" className="tile-image" />
                <div className="tile-overlay">
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}

export default HomePage;
