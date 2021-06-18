
from datetime import datetime
import flask
import kopDB
import kopError as err

class KopCriminal:
    def __init__(self,app):
        self.app = app
        
        @app.route('/testhtml', methods=['GET'])
        def home():
            dateNow=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return """
            <h1>Distant Reading Archive</h1>
            <p>This site is a prototype API for distant reading of science fiction novels.</p>
            <p>"""+dateNow+"</p>"

        @app.route('/kop/api/v1.0/criminal/<int:id>', methods=['GET'])
            #R = retrieve
        def criminalRbyId(id):
            try: 
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True)
                #non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute("""SELECT `criminal`.`id`,
                `criminal`.`first_name`,
                `criminal`.`middle_name`,
                `criminal`.`last_name`,
                `criminal`.`birth_date`,
                `criminal`.`picture_id` FROM criminal WHERE id = %s""",(id,))
                criminalOne = db.fetchone()
                if criminalOne == None:
                    return err.JsonErrorNotFound("criminal","id",str(id))
                oneCriminal= {
                        "id" : criminalOne["id"],
                        "first_name" : criminalOne["first_name"],
                        "middle_name" : criminalOne["middle_name"],
                        "last_name" : criminalOne["last_name"],
                        "birth_date" : criminalOne["birth_date"],
                        "picture_id" : criminalOne["picture_id"]

                        }
                db.close()
                oneCriminalJSON=flask.jsonify(oneCriminal)
                return oneCriminalJSON   
            except:
                    return err.JsonErrorUnexpected()       

        @app.route('/kop/api/v1.0/criminal/all', methods=['GET'])
        def criminalRAll():
            db_connection = kopDB.getConnection()
            db = db_connection.cursor(dictionary=True)

            db.execute("""SELECT `criminal`.`id`,
            `criminal`.`first_name`,
            `criminal`.`middle_name`,
            `criminal`.`last_name`,
            `criminal`.`birth_date`,
            `criminal`.`picture_id` FROM criminal""")

            allCriminal = db.fetchall()

            criminalList = []

            for criminalOne in allCriminal:
                print(criminalOne["id"])
                # retur "The criminal id = <b>"+riminal_row["id"]+"</b> and its name is ..." 2000
                oneCriminal = {
                    "id": criminalOne["id"],
                    "first_name": criminalOne["first_name"],
                    "middle_name": criminalOne["middle_name"],
                    "last_name": criminalOne["last_name"],
                    "birth_date": criminalOne["birth_date"],
                    "picture_id": criminalOne["picture_id"]
                }

                criminalList.append(oneCriminal)
            db.close()
            # criminalListJSON=json.dumps(criminalList)
            criminalListJSON = flask.jsonify(criminalList)

            return criminalListJSON    