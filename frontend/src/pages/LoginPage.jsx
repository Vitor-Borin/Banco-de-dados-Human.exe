import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import steamLogo from '../assets/steamLogo.png';
import apiService from '../services/api';
import './LoginPage.css';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSignIn = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      // SIMULAÇÃO: Não chama a API, só simula login bem-sucedido
      console.log('Simulando login:', { email, password });
      
      // Simula delay da API
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // Simula usuário logado
      apiService.setCurrentUser({
        id: 1,
        name: email.split('@')[0],
        email: email
      });
      
      navigate('/home');
    } catch (error) {
      setError(error.message || 'Erro ao fazer login');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateAccount = () => {
    navigate('/signup');
  };

  return (
    <div className="login-container">
      <div className="login-panel">
        <div className="logo-section">
          <img src={steamLogo} alt="Steam Logo" className="steam-logo" />
          <h1 className="steam-title">STEAM</h1>
        </div>
        
        <form className="login-form" onSubmit={handleSignIn}>
          {error && (
            <div className="error-message" style={{ color: 'red', marginBottom: '10px' }}>
              {error}
            </div>
          )}
          
          <div className="form-group">
            <label className="form-label">SIGN IN WITH EMAIL</label>
            <input
              type="email"
              className="form-input"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder=""
              required
            />
          </div>
          
          <div className="form-group">
            <label className="form-label">PASSWORD</label>
            <input
              type="password"
              className="form-input"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder=""
            />
          </div>
          
          <div className="checkbox-group">
            <input
              type="checkbox"
              id="remember"
              checked={rememberMe}
              onChange={(e) => setRememberMe(e.target.checked)}
              className="checkbox"
            />
            <label htmlFor="remember" className="checkbox-label">Remember me</label>
          </div>
          
          <button type="submit" className="signin-button" disabled={loading}>
            {loading ? 'Signing In...' : 'Sign In'}
          </button>
        </form>
        
        <div className="login-footer">
          <a href="#" className="help-link">Help, I can't sign in</a>
          <div className="create-account">
            <span className="create-text">Don't have a Steam account? </span>
            <button onClick={handleCreateAccount} className="create-link">Create a Free Account</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
