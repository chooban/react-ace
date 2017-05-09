# Ace My Order

Webapp and related services to make ordering lots of comics from [Ace Comics](https://www.acecomics.co.uk) a little
easier.

## Development Setup

Development is done in a fully containerised, Docker environment and a compose file for deploying a stack to a swarm is
provided.

### Prerequisites

You'll need yarn and npm on your $PATH.

#### Secrets

All of the secrets are defined as external, so will need to be created before the first deployment.

* **auth0_client_id** Client ID from Auth0
* **auth0_client_secret** Client secret from Auth0
* **auth0_domain** Domain from Auth0
* **auth0_management_token** Required by the [profiles service](https://github.com/chooban/ace-profiles-api) to update
  user profiles.

#### Volumes

* **ace_piwikroot** This is the folder which piwik puts its files in. Needs a volume as the config has to be written
  somewhere permanent.
* **ace_mariadb** For the database files.

### Building

`npm run build` will put everything into the `build/` directory and exit. `npm run watch` will watch for changes and
recompile as required.
