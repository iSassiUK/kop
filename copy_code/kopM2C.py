import flask
import kopDB

class KopM2C:
    def __init__(self,app):
        self.app = app
        
        @app.route('/kop/api/v1.0/m2c/all', methods=['GET'])
        def m2cRAll():
            db_connection = kopDB.getConnection()
            db = db_connection.cursor(dictionary=True)

            db.execute("""SELECT m2c.criminal_id as cid, m2c.media_id as mid, c.first_name as 'first Name',last_name,m.title, CONVERT (c_pic.url using UTF8 ) as criminal_pic, CONVERT (m_pic.url using UTF8 ) as media_pic, CONVERT (m.description using UTF8) as media_description
from 	(criminal as c 
		join media2criminal as m2c on c.id = m2c.criminal_id)
        join media as m on m.id = m2c.media_id
		join picture as c_pic on c.picture_id = c_pic.id
		join picture as m_pic on m.picture_id = m_pic.id""")

            allM2C = db.fetchall()

            m2cList = []

            for m2cOne in allM2C:
                oneM2C = {
                    "criminal_id": m2cOne["cid"],
                    "media_id": m2cOne["mid"],
                    "first": m2cOne["first Name"],
                    "last": m2cOne["last_name"],
                    "title": m2cOne["title"],
                    "criminal_pic": m2cOne["criminal_pic"],
                    "media_pic": m2cOne["media_pic"],
                    "media_description": m2cOne["media_description"]

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
            db.execute("""SELECT m2c.criminal_id as cid, m2c.media_id as mid, c.first_name as 'first Name',last_name,m.title, CONVERT (c_pic.url using UTF8 ) as criminal_pic, CONVERT (m_pic.url using UTF8 ) as media_pic, CONVERT (m.description using UTF8) as media_description
from 	(criminal as c 
		join media2criminal as m2c on c.id = m2c.criminal_id)
        join media as m on m.id = m2c.media_id
		join picture as c_pic on c.picture_id = c_pic.id
		join picture as m_pic on m.picture_id = m_pic.id WHERE media_id = %s""",(media_id,))
            m2cOne = db.fetchone()
            oneM2C= {
                    "criminal_id": m2cOne["cid"],
                    "media_id": m2cOne["mid"],
                    "first": m2cOne["first Name"],
                    "last": m2cOne["last_name"],
                    "title": m2cOne["title"],
                    "criminal_pic": m2cOne["criminal_pic"],
                    "media_pic": m2cOne["media_pic"],
                    "media_description": m2cOne["media_description"]

                    }
            db.close()
            oneM2CJSON=flask.jsonify(oneM2C)
            return oneM2CJSON     

        @app.route('/kop/api/v1.0/m2c/criminal/<criminal_id>', methods=['GET'])
        def m2cRbyCriminalId(criminal_id):
            db_connection = kopDB.getConnection()

            db = db_connection.cursor(dictionary=True)
            #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
            db.execute("""SELECT m2c.criminal_id as cid, m2c.media_id as mid, c.first_name as 'first Name',last_name,m.title, CONVERT (c_pic.url using UTF8 ) as criminal_pic, CONVERT (m_pic.url using UTF8 ) as media_pic, CONVERT (m.description using UTF8) as media_description
from 	(criminal as c 
		join media2criminal as m2c on c.id = m2c.criminal_id)
        join media as m on m.id = m2c.media_id
		join picture as c_pic on c.picture_id = c_pic.id
		join picture as m_pic on m.picture_id = m_pic.id WHERE criminal_id = %s""",(criminal_id,))
            m2cOne = db.fetchone()
            oneM2C= {
                   "criminal_id": m2cOne["cid"],
                    "media_id": m2cOne["mid"],
                    "first": m2cOne["first Name"],
                    "last": m2cOne["last_name"],
                    "title": m2cOne["title"],
                    "criminal_pic": m2cOne["criminal_pic"],
                    "media_pic": m2cOne["media_pic"],
                    "media_description": m2cOne["media_description"]
                    }
            db.close()
            oneM2CJSON=flask.jsonify(oneM2C)
            return oneM2CJSON      