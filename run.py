from decouple import config

from app import create_app

config_name = config('APPLICATION_SETTINGS', default='')
app = create_app(config_name)


if __name__ == "__main__":
    app.run()
