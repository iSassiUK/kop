from dns.rdatatype import NULL
import flask
from mysql.connector.utils import NUMERIC_TYPES
import kopDB
import kopError as err

class KopMedia:
    def __init__(self,app):
        self.app = app
             
             
        @app.route('/kop/api/v1.0/media/<int:id>', methods=['GET'])
            #R = retrieve
        def mediaRbyId(id):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True)
                #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute("""SELECT `media`.`id`,
        `media`.`title`,
        `media`.`description`,
        `media`.`date_release`,
        `media`.`instalment`,
        `media`.`genre`,
        `media`.`running`,
        `media`.`published`,
        `media`.`picture_id` FROM media WHERE id = %s""",(id,))
                mediaOne = db.fetchone()
                if mediaOne == None:
                    return err.JsonErrorNotFound("media","id",str(id))

                oneMedia= {
                    "id": mediaOne["id"],
                        "title": mediaOne["title"],
                        "description": mediaOne["description"],
                        "date_release": mediaOne["date_release"],
                        "instalment": mediaOne["instalment"],
                        "genre": mediaOne["genre"],
                        "running": mediaOne["running"],
                        "published": mediaOne["published"],
                        "picture_id": mediaOne["picture_id"]

                        }
                db.close()
                oneMediaJSON=flask.jsonify(oneMedia)
                return oneMediaJSON   
            except:
                return err.JsonErrorUnexpected()


        @app.route('/kop/api/v1.0/media/all', methods=['GET'])
        def mediaRAll():
            db_connection = kopDB.getConnection()
            db = db_connection.cursor(dictionary=True)

            db.execute("""SELECT `media`.`id`,
    `media`.`title`,
    `media`.`date_release`,
    `media`.`instalment`,
    `media`.`genre`,
    `media`.`running`,
    `media`.`published`,
    `media`.`picture_id`,
    pic.title as pic_title,
    
  
    CONVERT (pic.thumb using UTF8) as pic_thumb,
    CONVERT (pic.url using UTF8) as pic_url,
    CONVERT (media.description using UTF8) as media_desc,
    CONVERT (pic.description using UTF8) as pic_desc
FROM `kop`.`media` 
join kop.picture as pic on pic.id = media.picture_id""")

            allMedia = db.fetchall()

            mediaList = []

            for mediaOne in allMedia:
                oneMedia = {
                    "id": mediaOne["id"],
                    "title": mediaOne["title"],
                    "description": mediaOne["media_desc"],
                    "date_release": mediaOne["date_release"],
                    "instalment": mediaOne["instalment"],
                    "genre": mediaOne["genre"],
                    "running": mediaOne["running"],
                    "published": mediaOne["published"],
                    "picture":    {
                    "picture_id": mediaOne["picture_id"],
                    "picture_url": mediaOne["pic_url"],
                    "picture_thumb": mediaOne["pic_thumb"],
                    "picture_title": mediaOne["pic_title"],
                    "picture_description": mediaOne["pic_desc"]

                    }
                 
                }

                mediaList.append(oneMedia)
            db.close()
            httpResponse = flask.jsonify(mediaList)
            httpResponse.headers.add('Access-Control-Allow-Origin', '*')	
            return httpResponse    
