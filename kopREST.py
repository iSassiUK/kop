from kopM2C import KopM2C
from kopPicture import KopPicture
import flask
from kopCriminal import KopCriminal
from kopMedia import KopMedia
from kopPicture import KopPicture


if __name__ == "__main__":

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    kopCriminal = KopCriminal(app)
    kopMedia = KopMedia(app)
    kopPicture = KopPicture(app)
    kopM2C = KopM2C(app)

    app.run()
