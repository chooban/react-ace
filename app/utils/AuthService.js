import Auth0Lock from 'auth0-lock';

class AuthService {
  constructor(clientId, domain) {
    this.lock = new Auth0Lock(
        clientId,
        domain,
      {
        redirectUrl: window.location.href,
        responseType: 'token'
      });

    this.lock.on('authenticated', this.doAuth.bind(this));
    this.login = this.login.bind(this);
    this.getProfile = this.getProfile.bind(this);
  }

  login() {
    this.lock.show();
  }

  doAuth(authResult) {
    this.setToken(authResult.idToken);
  }

  getProfile(done) {
    this.lock.getProfile(this.getToken(), done);
  }

  loggedIn() {
    return !!this.getToken();
  }

  setToken(idToken) {
    localStorage.setItem('id_token', idToken);
  }

  getToken() {
    return localStorage.getItem('id_token');
  }

  logout() {
    localStorage.removeItem('id_token');
  }
}

export function AuthServiceFactory() {
  return new AuthService(
    '3ZRxcpSCqh6CnKU1zFZuWbKY0uIrfK7D',
    'acemyorder.eu.auth0.com'
    );
}
