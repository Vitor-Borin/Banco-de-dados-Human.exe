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
              <h3 className="subtitle">Ficção científica interativa sobre a resistência humana</h3>
              <p className="game-description">
                HUMAN.EXE é uma experiência narrativa que mistura minigames, animações e
                escolhas do jogador em um mundo cyberpunk onde a Inteligência Artificial
                tomou o controle. Você acompanha cinco especialistas tentando reconquistar
                a humanidade, enquanto progride por fases com trilha sonora imersiva e
                momentos cinematográficos.
              </p>
            </div>

            <div className="features-section">
              <h2 className="section-title">Características do Jogo</h2>
              <ul className="features-list">
                <li>Animações cinematográficas com GSAP e transições fluídas.</li>
                <li>Trilha sonora e efeitos sonoros imersivos para cada fase.</li>
                <li>Múltiplos minigames, um para cada especialista do time.</li>
                <li>Sistema de chat entre personagens com interações dinâmicas.</li>
                <li>Visual cyberpunk com identidade própria e interface responsiva.</li>
                <li>Progressão por fases com desbloqueios e registro local de avanço.</li>
                <li>Decisões críticas que impactam o desfecho da história.</li>
                <li>Otimização para desktop e mobile, com suporte a toque.</li>
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
                    <span className="reviewer">@ana.dev</span>
                    <span className="review-time">2h</span>
                  </div>
                  <p className="review-text">As animações com GSAP deixaram tudo muito cinematográfico. Curti demais!</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@nicolas</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">A trilha sonora e o visual cyberpunk criam uma imersão absurda.</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@vborin</span>
                    <span className="review-time">1h</span>
                  </div>
                  <p className="review-text">Gostei dos minigames de cada personagem e do sistema de chat.</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@winny</span>
                    <span className="review-time">45m</span>
                  </div>
                  <p className="review-text">Funciona bem no celular e as escolhas realmente mudam o final.</p>
                </div>
                <div className="review-item">
                  <div className="review-header">
                    <img src={likeSteam} alt="Like" className="review-thumbs" />
                    <span className="reviewer">@yas</span>
                    <span className="review-time">30m</span>
                  </div>
                  <p className="review-text">Projeto redondinho. Recomendo para quem curte narrativa interativa.</p>
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
