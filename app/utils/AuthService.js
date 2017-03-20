import * as Auth0Lock from 'auth0-lock';

export class AuthService {
  constructor(lock, storage = localStorage) {
    this.lock = lock;
    this.lock.on('authenticated', this.doAuth.bind(this));
    this.login = this.login.bind(this);
    this.getProfile = this.getProfile.bind(this);
    this.storage = storage;
  }

  login() {
    this.lock.show();
  }

  doAuth(authResult) {
    this.setToken(authResult.idToken);
  }

  onAuth(callback) {
    this.lock.on('authenticated', callback.bind(this, this));
  }

  getProfile(done) {
    this.lock.getProfile(this.getToken(), done);
  }

  loggedIn() {
    return !!this.getToken();
  }

  setToken(idToken) {
    this.storage.setItem('id_token', idToken);
  }

  getToken() {
    return this.storage.getItem('id_token');
  }

  logout() {
    this.storage.removeItem('id_token');
  }
}

let instance;

export function AuthServiceFactory() {
  if (!instance) {
    const lock = new Auth0Lock.default(//eslint-disable-line
      localStorage.getItem('auth0_id'),
      localStorage.getItem('auth0_domain'),
      {
        redirectUrl: (global.window) ? global.window.location.href : '',
        responseType: 'token'
      }
    );

    instance = new AuthService(lock);
  }
  return instance;
}
