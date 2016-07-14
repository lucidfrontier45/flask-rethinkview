from flask import Flask
from flask_rethinkview import RethinkDB, RethinkDBView, create_db


class TestView(RethinkDBView):
    _table_name = "users"
    _index_names = ["name"]


class Config(object):
    RETHINKDB_HOST = "127.0.0.1"
    RETHINKDB_PORT = 28015
    RETHINKDB_DB = "test"

app = Flask(__name__)


app.config.from_object(Config)

app.rethinkdb = RethinkDB(app)


TestView.register(app)

if __name__ == "__main__":
    with app.app_context():
        create_db(app)
        TestView.init()
    app.run()
