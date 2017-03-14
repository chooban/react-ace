import * as Auth0Lock from 'auth0-lock';

import config from './config';

export class AuthService {
  constructor(lock) {
    this.lock = lock;
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
    localStorage.setItem('id_token', idToken);
  }

  getToken() {
    return localStorage.getItem('id_token');
  }

  logout() {
    localStorage.removeItem('id_token');
  }
}

let instance;

export function AuthServiceFactory() {
  if (!instance) {
    const lock = new Auth0Lock.default(//eslint-disable-line
      config.auth0Id,
      config.auth0Domain,
      {
        redirectUrl: (global.window) ? global.window.location.href : '',
        responseType: 'token'
      }
    );

    instance = new AuthService(lock);
  }
  return instance;
}
