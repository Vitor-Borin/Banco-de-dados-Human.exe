import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import steamLogo from '../assets/steamLogo.png';
import searchSteam from '../assets/searchSteam.png';
import humanbg from '../assets/humanbg.png';
import likeSteam from '../assets/LikeSteam.png';
import apiService from '../services/api';
import './DetailsPage.css';

function DetailsPage() {
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

  const handleBackToHome = () => {
    navigate('/home');
  };

  const handleLogout = () => {
    apiService.logout();
    navigate('/');
  };

  return (
    <div className="details-container">
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

      <div className="details-content">
        <div className="details-main">
          {/* Game Title */}
          <div className="game-header">
            <button onClick={handleBackToHome} className="voltar-link">← Voltar</button>
            <h1 className="game-title">HUMAN.EXE</h1>
          </div>

          {/* Main Game Image */}
          <div className="game-image-section">
            <img src={humanbg} alt="HUMAN.EXE" className="main-game-image" />
          </div>

          {/* Left Column - Game Info */}
          <div className="game-info-column">
            <div className="about-section">
              <h2 className="section-title">Sobre este jogo</h2>
              <h3 className="subtitle">Salve o mundo de um destino caótico</h3>
              <p className="game-description">
                A IA dominou o mundo, e agora voce e seus amigos sao os ultimos pingos de esperanca que sobrou na terra. 
                Seja forte nessa batalha e demote a IA em jogos com uma mistura de cyberpunk e emocao humana.
              </p>
            </div>

            <div className="features-section">
              <h2 className="section-title">Características do Jogo</h2>
              <ul className="features-list">
                <li>Descubra um reino de insetos caídos, explorando cavernas musgosas, cidades douradas e pântanos.</li>
                <li>Envolva-se em combate acrobático e letal com uma variedade de movimentos mortais.</li>
                <li>Crie ferramentas poderosas e domine um arsenal de armas e armadilhas.</li>
                <li>Resolva missões surpreendentes, cace bestas raras e desvende mistérios antigos.</li>
                <li>Enfrente mais de 200 inimigos ferozes, incluindo bestas, caçadores, monstros e cavaleiros.</li>
                <li>Elimine mais de 40 chefes lendários e lute contra reis caídos.</li>
                <li>Desafie o modo "Steel Soul" após conquistar o reino.</li>
                <li>Desfrute de uma trilha sonora instrumental de Christopher Larkin, com melodias melancólicas, cordas sinfônicas e percussão.</li>
              </ul>
            </div>
          </div>

          {/* Right Column - Game Details */}
          <div className="game-details-column">
            <h1 className="game-title-right">HUMAN.EXE</h1>
            <p className="game-description-right">
            A IA dominou o mundo, e agora voce e seus amigos sao os ultimos pingos de esperanca que sobrou na terra. 
            Seja forte nessa batalha e demote a IA em jogos com uma mistura de cyberpunk e emocao humana.
            </p>
            
            <div className="game-stats">
              <div className="stat-item">
                <span className="stat-label">ANÁLISES RECENTES</span>
                <span className="stat-value">Extremamente Positivas (130.201)</span>
              </div>
              <div className="stat-item">
                <span className="stat-label">DATA DE LANÇAMENTO:</span>
                <span className="stat-value">10/09/2025</span>
              </div>
              <div className="stat-item">
                <span className="stat-label">DESENVOLVEDOR:</span>
                <span className="stat-value">ANWPY+V</span>
              </div>
              <div className="stat-item">
                <span className="stat-label">DISTRIBUIDORA:</span>
                <span className="stat-value">ANWPY+V</span>
              </div>
            </div>

            <div className="game-tags">
              <span className="tag">Indie</span>
              <span className="tag">Retro</span>
              <span className="tag">Pixel games</span>
              <span className="tag">Novidade</span>
              <span className="tag">Radiacinio</span>
            </div>

            <div className="reviews-section">
              <h3 className="reviews-title">ÚLTIMAS ANÁLISES</h3>
              <div className="reviews-list">
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@dianacitra</span>
                    <span className="review-time">2.5h</span>
                  </div>
                  <p className="review-text">I loved it, incredibly!</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@deliger</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">The game is perfect...</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />s
                    <span className="reviewer">@doscazr</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">One of the best experiences...</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@qwrtyui</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">I liked it, I would just play</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@enviaso</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">The game was very well made, recommended!</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}

export default DetailsPage;
