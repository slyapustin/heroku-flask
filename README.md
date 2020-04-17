# Sample Flask application on Heroku

Sample Python Flask TODO application deployed on Heroku

## Used Technology:
 - [Heroku: Cloud Application Platform](https://www.heroku.com/)
 - [Python](https://www.python.org/)
 - [Flask](https://flask.palletsprojects.com/)
 - [PostgreSQL](https://www.postgresql.org/)
 - [Memcached](https://memcached.org/) via [MemCachier](https://elements.heroku.com/addons/memcachier)
 - [Papertrail Log management](https://www.papertrail.com/)

## Deploy to Heroku (For Free)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Run locally
 - Create `.env ` file with your local settings based on the `.env.sample`
 - Install requirements `pip install -r requirements.txt`
 - Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
 - Start Heroku Local server `heroku local -f Procfile.local`
 - Your App are available at: http://127.0.0.1:5000/
 
 
## Related Articles
 - [Scaling a Flask Application with Memcache](https://devcenter.heroku.com/articles/flask-memcache#set-up-memcache)
 - [The Procfile](https://devcenter.heroku.com/articles/procfile)
 - [Quickstart with Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
 
