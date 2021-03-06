import os
from flask import Flask, url_for, render_template, redirect, session
from authlib.integrations.flask_client import OAuth
from osm import User
import json

class Cache:
    """A super simple Cache class needed to store the intermediate Oauth 1.0 token"""
    kv = {}
    def get(self, key):
        """get a key from the store"""
        return self.kv.get(key)
    def set(self, key, value, timeout=None):
        """set a key / value"""
        self.kv[key] = value
    def delete(self, key):
        """delete a key / value"""
        del self.kv[key]


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    cache = Cache()
    app.config.from_mapping(
        SECRET_KEY="dev",
        OSM_CONSUMER_KEY=os.environ.get("OSM_CONSUMER_KEY"),
        OSM_CONSUMER_SECRET=os.environ.get("OSM_CONSUMER_SECRET")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    oauth = OAuth(app, cache=cache)

    oauth.register(
        name="osm",
        client_id=app.config.get("OSM_CONSUMER_KEY"),
        client_secret=app.config.get("OSM_CONSUMER_SECRET"),
        request_token_url="https://www.openstreetmap.org/oauth/request_token",
        request_token_params=None,
        access_token_url="https://www.openstreetmap.org/oauth/access_token",
        access_token_params=None,
        authorize_url="https://www.openstreetmap.org/oauth/authorize",
        api_base_url="https://www.openstreetmap.org/api/0.6/",
        client_kwargs=None,
    )

    @app.route("/login")
    def login():
        """user log in entrypoint"""
        redirect_uri = url_for("authorize", _external=True)
        return oauth.osm.authorize_redirect(redirect_uri)

    @app.route("/authorize")
    def authorize():
        """process the user once authorized on OSM"""
        token = oauth.osm.authorize_access_token()
        resp = oauth.osm.get("user/details")
        user = User.from_xml(resp.text)
        session["osm_id"] = user.osm_id
        session["display_name"] = user.display_name
        session["access_token"] = token
        return redirect("/")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/")

    @app.route("/")
    def home():
        """home page"""
        return render_template("home.html")
    
    return app
