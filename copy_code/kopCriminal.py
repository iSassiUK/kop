
from datetime import datetime
import flask
import kopDB
import kopError as err


class KopCriminal:
    def __init__(self, app):
        self.app = app

        @app.route('/testhtml', methods=['GET'])
        def home():
            dateNow = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return """
            <h1>Distant Reading Archive</h1>
            <p>This site is a prototype API for distant reading of science fiction novels.</p>
            <p>"""+dateNow+"</p>"

        @app.route('/kop/api/v1.0/criminal/search/middle/<sub_middle>', methods=['GET'])
        #R = retrieve
        def criminalSearchbyMiddleName(sub_middle):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True, buffered=True)
                # non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute("""select first_name, middle_name, last_name, birth_date,
                 c.picture_id as pic_id, alias, c.id as criminal_id, nic.id as nickname_id, 
                 pic.thumb, pic.url, pic.title, pic.description
from criminal as c
join nickname as nic on nic.criminal_id = c.id
join picture as pic on pic.id = c.id WHERE lower(middle_name) like CONCAT('%',%s,'%')""", (sub_middle,))
            
                allCriminal = db.fetchall()
                if allCriminal == None:
                    return err.JsonErrorNotFound("criminal", "middle_name", str(""))
                criminalList = kopDB.dbCriminalList(allCriminal)
                db.close()
                criminalListJSON = flask.jsonify(criminalList)
                return criminalListJSON
            except:
                return err.JsonErrorUnexpected()

        @app.route('/kop/api/v1.0/criminal/search/first/<sub_first>', methods=['GET'])
        #R = retrieve
        def criminalSearchbyFirstName(sub_first):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True, buffered=True)
                # non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute(""" select first_name, middle_name, last_name, birth_date,
                 c.picture_id as pic_id, alias, c.id as criminal_id, nic.id as nickname_id, 
                 pic.thumb, pic.url, pic.title, pic.description
from criminal as c
join nickname as nic on nic.criminal_id = c.id
join picture as pic on pic.id = c.id WHERE lower(first_name) like CONCAT('%',%s,'%')""", (sub_first,))
            
                allCriminal = db.fetchall()
                if allCriminal == None:
                    return err.JsonErrorNotFound("criminal", "first_name", str(""))

                criminalList = kopDB.dbOneCriminal(allCriminal)
                db.close()
                criminalListJSON = flask.jsonify(criminalList)
                return criminalListJSON
            except:
                return err.JsonErrorUnexpected()



        @app.route('/kop/api/v1.0/criminal/search/last/<sub_last>', methods=['GET'])
        #R = retrieve
        def criminalSearchbyLast(sub_last):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True, buffered=True)
                # non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute(""" select first_name, middle_name, last_name, birth_date,
                 c.picture_id as pic_id, alias, c.id as criminal_id, nic.id as nickname_id, 
                 pic.thumb, pic.url, pic.title, pic.description
from criminal as c
join nickname as nic on nic.criminal_id = c.id
join picture as pic on pic.id = c.id  WHERE last_name like CONCAT('%',%s,'%')""", (sub_last,))
            
                allCriminal = db.fetchall()
                if allCriminal == None:
                    return err.JsonErrorNotFound("criminal", "last_name", str(""))
               
                criminalList = kopDB.dbOneCriminal(allCriminal)
                db.close()
                criminalListJSON = flask.jsonify(criminalList)
                return criminalListJSON
            except:
                return err.JsonErrorUnexpected()

        @app.route('/kop/api/v1.0/criminal/<int:id>', methods=['GET'])
        #R = retrieve
        def criminalRbyId(id):
            try:
                db_connection = kopDB.getConnection()

                db = db_connection.cursor(dictionary=True, buffered=True)
                # non puoi considerare dopo = una stringa per sicurezza (problema sql injection)
                db.execute("""select first_name, middle_name, last_name, birth_date,
                 c.picture_id as pic_id, alias, c.id as criminal_id, nic.id as nickname_id, 
                 pic.thumb, pic.url, pic.title, pic.description
from criminal as c
join nickname as nic on nic.criminal_id = c.id
join picture as pic on pic.id = c.id WHERE criminal_id = %s""", (id,))
                criminalOne = db.fetchall()
                if criminalOne == None:
                    return err.JsonErrorNotFound("criminal", "id", str(id))
                oneCriminal = kopDB.dbOneCriminal(criminalOne)
                db.close()
                oneCriminalJSON = flask.jsonify(oneCriminal)
                return oneCriminalJSON
            except:
                return err.JsonErrorUnexpected()

        @app.route('/kop/api/v1.0/criminal/all', methods=['GET'])
        def criminalRAll():
            db_connection = kopDB.getConnection()
            db = db_connection.cursor(dictionary=True, buffered=True)

            db.execute("""select first_name, middle_name, last_name, birth_date, c.picture_id as pic_id, alias, c.id as criminal_id, nic.id as nickname_id, pic.thumb, pic.url, pic.title, pic.description
from criminal as c
join nickname as nic on nic.criminal_id = c.id
join picture as pic on pic.id = c.id""")

            allCriminal = db.fetchall()

            criminalList = kopDB.dbCriminalList(allCriminal)
            db.close()
            # criminalListJSON=json.dumps(criminalList)
            criminalListJSON = flask.jsonify(criminalList)

            return criminalListJSON
