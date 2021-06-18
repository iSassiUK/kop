import mysql.connector
from dns.rdatatype import NULL
db_connection=NULL

def getConnection():
    global db_connection
    if db_connection==NULL:
            db_connection = mysql.connector.connect(
            host="192.168.56.5",
            user="kop",
            passwd="killeroverpython.33",
            database="kop")
    return db_connection

def createTestDB():
    db_connection = mysql.connector.connect(
    host="192.168.56.5",
    user="kop",
    passwd="killeroverpython.33",
    database="kop")

    db = db_connection.cursor()

    sqlMedia = """INSERT INTO `kop`.`media`
        (`title`,
        `description`,
        `date_release`,
        `instalment`,
        `genre`,
        `running`,
        `published`,
        `picture_id`)
        VALUES
        ('%s',
        '%s',
        '1980-12-12',
        %d,
        '%s',
        1,
        1,
        null);"""

    sqlMedia1 = (sqlMedia % ('Confession','Story of ciccio',2,'Doc'))
    sqlMedia2 = (sqlMedia % ('Inside the Criminal Mind','Explore immoral behavior',10,'Doc'))
    sqlMedia3 = (sqlMedia % ('Texas Chainsaw Massacre','1st American slasher',1,'Movie'))

    sqlCriminal = """INSERT INTO `kop`.`criminal`
    (`first_name`,
    `middle_name`,
    `last_name`,
    `birth_date`,
    `picture_id`)
    VALUES
    (%s,
    %s,
    %s,
    %s,
    null);"""

    sqlMedia2Criminal="""
    INSERT INTO `kop`.`media2criminal`
(`criminal_id`,
`media_id`)
VALUES
(%s,
%s);
"""

    sqlNickname="""
    INSERT INTO `kop`.`nickname`
(`alias`,
`criminal_id`)
VALUES
(%s,
%s);
"""

    sqlPicture="""
    INSERT INTO `kop`.`picture`
(`thumb`,
`url`,
`title`,
`description`)
VALUES
(%s,
%s,
%s,
%s);
"""
    picEG="https://www.americas-most-haunted.com/wp-content/uploads/2016/10/ed-gein-680x1024-680x675.jpg"
    picJWG="https://attitude.co.uk/media/images/2018/09/John-Wayne-Gacy_grande.png"
    picTB="https://i.pinimg.com/736x/d5/2d/25/d52d2552b2e5d5264207412abc2e86b9.jpg"
    picCM="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Manson1968.jpg/220px-Manson1968.jpg"


    sqlUpdateCriminalwithPicture="""UPDATE `kop`.`criminal`
SET
`picture_id` = %s
WHERE `last_name` = %s;
"""

    confPic="https://images-na.ssl-images-amazon.com/images/I/51Bg4wdqQtL._SX323_BO1,204,203,200_.jpg"
    insidePic="https://www.onnetflix.co.uk/media/11/inside-the-criminal-mind_80185065.jpg"
    texasPic="https://baylorlariat.com/wp-content/uploads/2018/10/chainsaw.jpg"

    sqlUpdateMediawithPicture="""UPDATE `kop`.`media`
SET
`picture_id` = %s
WHERE `title` = %s;
"""
    #db.execute(sqlPicture,(confPic,confPic,'Confession',''))
    #db.execute(sqlPicture,(insidePic,insidePic,'Inside the Criminal Mind',''))
    #db.execute(sqlPicture,(texasPic,texasPic,'Texas Chainsaw Massacre',''))
    

    #db.execute(sqlUpdateMediawithPicture,(5,'Confession'))
    #db.execute(sqlUpdateMediawithPicture,(7,'Texas Chainsaw Massacre'))
    #db.execute(sqlUpdateMediawithPicture,(6,'Inside the Criminal Mind'))

    
    #db.execute(sqlPicture,(picEG,picEG,'Ed Gein',''))
    #db.execute(sqlPicture,(picJWG,picJWG,'John Wayne Gacy',''))
    #db.execute(sqlPicture,(picTB,picTB,'Theodore Robert Bundy',''))
    #db.execute(sqlPicture,(picCM,picCM,'Charles Milles Manson',''))

    #db.execute(sqlUpdateCriminalwithPicture,(1,'Gein'))
    #db.execute(sqlUpdateCriminalwithPicture,(2,'Gacy'))
    #db.execute(sqlUpdateCriminalwithPicture,(3,'Bundy'))
    #db.execute(sqlUpdateCriminalwithPicture,(4,'Manson'))

    #db.execute(sqlNickname,('Grandfather of Gore',1))
    #db.execute(sqlNickname,('The Plainfield Butcher',1))
    #db.execute(sqlNickname,('The Plainfield Ghoul',1))
    #db.execute(sqlNickname,('Pogo the Clown',2))
    #db.execute(sqlNickname,('The Killer Clown',2))
    #db.execute(sqlNickname,('Lady Killer',3))
    #db.execute(sqlNickname,('The Campus Killer',3))


    #db.execute(sqlMedia2Criminal,(1,3))
    #db.execute(sqlMedia2Criminal,(2,2))
    #db.execute(sqlMedia2Criminal,(3,1))
    #db.execute(sqlMedia2Criminal,(3,2))
    #db.execute(sqlMedia2Criminal,(4,2))  

    #db.execute(sqlCriminal,('Ed','Theodore','Gein','1906-08-27'))
    #db.execute(sqlCriminal,('John','Wayne','Gacy','1942-03-17'))
    #db.execute(sqlCriminal,('Theodore','Robert','Bundy','1946-11-24'))
    #db.execute(sqlCriminal,('Charles','Milles','Manson','1934-11-12'))


    #db.execute(sqlMedia1)
    #db.execute(sqlMedia2)
    #db.execute(sqlMedia3)

    db_connection.commit()

    print(db.rowcount,"record inserted")

if __name__ == "__main__":
    createTestDB()    
    





