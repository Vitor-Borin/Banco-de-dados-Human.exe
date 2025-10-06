import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import steamLogo from '../assets/steamLogo.png';
import apiService from '../services/api';
import './SignupPage.css';

function SignupPage() {
  const [nomeUsuario, setNomeUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [email, setEmail] = useState('');
  const [apelidoSteam, setApelidoSteam] = useState('');
  const [rememberMe, setRememberMe] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSignUp = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    // Validações básicas
    if (!nomeUsuario.trim()) {
      setError('Nome é obrigatório');
      setLoading(false);
      return;
    }

    if (!email.trim()) {
      setError('Email é obrigatório');
      setLoading(false);
      return;
    }

    if (!apelidoSteam.trim()) {
      setError('Apelido Steam é obrigatório');
      setLoading(false);
      return;
    }

    if (password.length < 6) {
      setError('Senha deve ter pelo menos 6 caracteres');
      setLoading(false);
      return;
    }

    // Limite do bcrypt (72 bytes)
    if (new TextEncoder().encode(password).length > 72) {
      setError('Senha muito longa. Use até 72 caracteres.');
      setLoading(false);
      return;
    }

    if (password !== confirmPassword) {
      setError('As senhas não coincidem');
      setLoading(false);
      return;
    }

    try {
      const userData = {
        nome_usuario: nomeUsuario.trim(),
        email: email.trim(),
        senha_usuario: password,
        apelido_steam: apelidoSteam.trim(),
        id_perfil: 1 // Default profile ID
      };

      console.log('Enviando dados:', userData);
      const response = await apiService.createUser(userData);
      console.log('Resposta da API:', response);
      
      if (response) {
        setError('');
        alert('Conta criada com sucesso! Faça login para continuar.');
        navigate('/');
      }
    } catch (error) {
      console.error('Erro ao criar conta:', error);
      // Repasse mensagens de validação do backend quando houver
      setError(error.message || 'Erro ao criar conta. Tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  const handleSignIn = () => {
    navigate('/');
  };

  return (
    <div className="signup-container">
      <div className="signup-panel">
        <div className="logo-section">
          <img src={steamLogo} alt="Steam Logo" className="steam-logo" />
          <h1 className="steam-title">STEAM</h1>
        </div>
        
        <form className="signup-form" onSubmit={handleSignUp}>
          {error && (
            <div className="error-message" style={{ color: 'red', marginBottom: '10px' }}>
              {error}
            </div>
          )}
          
          <div className="form-group">
            <label className="form-label">FULL NAME</label>
            <input
              type="text"
              className="form-input"
              value={nomeUsuario}
              onChange={(e) => setNomeUsuario(e.target.value)}
              placeholder=""
              required
            />
          </div>
          
          <div className="form-group">
            <label className="form-label">EMAIL ADDRESS</label>
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
            <label className="form-label">STEAM NICKNAME</label>
            <input
              type="text"
              className="form-input"
              value={apelidoSteam}
              onChange={(e) => setApelidoSteam(e.target.value)}
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
              required
            />
          </div>
          
          <div className="form-group">
            <label className="form-label">CONFIRM PASSWORD</label>
            <input
              type="password"
              className="form-input"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder=""
              required
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
          
          <button type="submit" className="signup-button" disabled={loading}>
            {loading ? 'Creating Account...' : 'Create Account'}
          </button>
        </form>
        
        <div className="signup-footer">
          <a href="#" className="help-link">Help, I can't create account</a>
          <div className="signin-account">
            <span className="signin-text">Already have a Steam account? </span>
            <button onClick={handleSignIn} className="signin-link">Sign In</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SignupPage;
