import flask
import kopDB

class KopM2C:
    def __init__(self,app):
        self.app = app
        
        @app.route('/kop/api/v1.0/m2c/all', methods=['GET'])
        def m2cRAll():
            db_connection = kopDB.getConnection()
            db = db_connection.cursor(dictionary=True)

            db.execute("""SELECT `media2criminal`.`criminal_id`,
    `media2criminal`.`media_id` FROM media2criminal""")

            allM2C = db.fetchall()

            m2cList = []

            for m2cOne in allM2C:
                oneM2C = {
                    "criminal_id": m2cOne["criminal_id"],
                    "media_id": m2cOne["media_id"]
                }

                m2cList.append(m2cOne)
            db.close()
            m2cListJSON = flask.jsonify(m2cList)

            return m2cListJSON    

        @app.route('/kop/api/v1.0/m2c/media/<media_id>', methods=['GET'])
        def m2cRbyMediaId(media_id):
            db_connection = kopDB.getConnection()

            db = db_connection.cursor(dictionary=True)
            #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
            db.execute("""SELECT `media2criminal`.`criminal_id`,
    `media2criminal`.`media_id` FROM media2criminal WHERE media_id = %s""",(media_id,))
            m2cOne = db.fetchone()
            oneM2C= {
                    "criminal_id" : m2cOne["criminal_id"],
                    "media_id" : m2cOne["media_id"],

                    }
            db.close()
            oneM2CJSON=flask.jsonify(oneM2C)
            return oneM2CJSON     

        @app.route('/kop/api/v1.0/m2c/criminal/<criminal_id>', methods=['GET'])
        def m2cRbyCriminalId(criminal_id):
            db_connection = kopDB.getConnection()

            db = db_connection.cursor(dictionary=True)
            #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
            db.execute("""SELECT `media2criminal`.`criminal_id`,
    `media2criminal`.`media_id` FROM media2criminal WHERE criminal_id = %s""",(criminal_id,))
            m2cOne = db.fetchone()
            oneM2C= {
                    "criminal_id" : m2cOne["criminal_id"],
                    "media_id" : m2cOne["media_id"],

                    }
            db.close()
            oneM2CJSON=flask.jsonify(oneM2C)
            return oneM2CJSON          
            