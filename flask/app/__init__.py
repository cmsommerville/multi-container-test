from flask import Flask
from redis import Redis

redis = Redis(host='redis', port=6379)

def create_app(): 

    app = Flask(__name__)

    @app.route('/')
    def home(): 
        redis.incr('hits')
        v = redis.get('hits').decode('utf-8')
        return f"<h1>Hello world. This page has been viewed {v} times</h1>"

    @app.route('/<string:val>')
    def set_redis(val): 
        redis.set(val, val)
        v = redis.get(val).decode('utf-8')
        return "<h1>" + v + "</h1>"

    return app