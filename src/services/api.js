const API_BASE_URL = 'http://localhost:8000';

class ApiService {
  constructor() {
    this.baseURL = API_BASE_URL;
    this.currentUser = JSON.parse(localStorage.getItem('currentUser') || 'null');
  }

  setCurrentUser(user) {
    this.currentUser = user;
    localStorage.setItem('currentUser', JSON.stringify(user));
  }

  removeCurrentUser() {
    this.currentUser = null;
    localStorage.removeItem('currentUser');
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // Auth endpoints
  async login(email, password) {
    const response = await this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    
    if (response.success) {
      this.setCurrentUser({
        id: response.user_id,
        name: response.user_name,
        email: email
      });
    }
    
    return response;
  }

  async logout() {
    this.removeCurrentUser();
    return { success: true, message: 'Logout realizado com sucesso' };
  }

  async verifyUser(email, password) {
    return this.request('/auth/verify', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  getCurrentUser() {
    return this.currentUser;
  }

  // User endpoints
  async createUser(userData) {
    return this.request('/usuarios/', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  }

  async getUsers() {
    return this.request('/usuarios/');
  }

  async getUser(userId) {
    return this.request(`/usuarios/${userId}`);
  }

  async updateUser(userId, userData) {
    return this.request(`/usuarios/${userId}`, {
      method: 'PUT',
      body: JSON.stringify(userData),
    });
  }

  async deleteUser(userId) {
    return this.request(`/usuarios/${userId}`, {
      method: 'DELETE',
    });
  }

  // Login audit endpoints
  async getLogins() {
    return this.request('/logins/');
  }

  async getLogin(loginId) {
    return this.request(`/logins/${loginId}`);
  }

  async getUserLogins(userId) {
    return this.request(`/logins/user/${userId}`);
  }

  async getMyLogins() {
    return this.request('/logins/me/logins');
  }
}

export default new ApiService();
