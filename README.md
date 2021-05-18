# OSM OAuth authentication with Flask

This is a minimal application showing how to implement a sign-in flow in a Flask web application using OpenStreetMap OAuth. 

To set it up:

1. Set up your Flask environment.

```
pipenv install
pipenv shell
```

2. Create an OAuth application in your OpenStreetMap user settings, at the bottom of the `Settings` > `oauth settings` page. Note the consumer key and the consumer secret. Set these as environment variables `OSM_CONSUMER_KEY` and `OSM_CONSUMER_SECRET`, respecively.

```
export OSM_CONSUMER_KEY="the_consumer_key_from_osmorg"
export OSM_CONSUMER_SECRET="the_consumer_secret_from_osmorg"
```

3. Navigate to the application directory and run the app:

```
cd osmoauth
flask run
```

4. Head to `http://localhost:5000` to try it out.