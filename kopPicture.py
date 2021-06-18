import flask
import kopDB
import kopError as err

class KopPicture:
    def __init__(self,app):
        self.app = app
        
        @app.route('/kop/api/v1.0/picture/<int:id>', methods=['GET'])
            #R = retrieve
        def pictureRbyId(id):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True)
                #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute("""SELECT `picture`.`id`,
                `picture`.`thumb`,
                `picture`.`url`,
                `picture`.`title`,
                `picture`.`description` FROM picture WHERE id = %s""",(id,))
                pictureOne = db.fetchone()
                if pictureOne == None:
                    return err.JsonErrorNotFound("picture","id",str(id))
                onePicture= {
                    "id": pictureOne["id"],
                        "thumb": pictureOne["thumb"],
                        "url": pictureOne["url"],
                        "title": pictureOne["title"],
                        "description": pictureOne["description"]
                        }
                db.close()
                pictureOneJSON=flask.jsonify(onePicture)
                return pictureOneJSON  
            except:
                    return err.JsonErrorUnexpected() 