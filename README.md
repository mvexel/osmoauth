# OSM OAuth authentication with Flask

This is a minimal application showing how to implement a sign-in flow in a Flask web application using OpenStreetMap OAuth. 

To set it up, create an OAuth application in your OpenStreetMap user settings, at the bottom of the `Settings` > `oauth settings` page.

Note the consumer key and the consumer secret. Set these as environment variables `OSM_CONSUMER_KEY` and `OSM_CONSUMER_SECRET`, respecively.

Then, set up your flask environment. Create a virtual environment and install the dependencies:

```
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

Then, navigate to the application directory and run the app:

```
flask run
```

Then head to `http://localhost:5000` to try it out.