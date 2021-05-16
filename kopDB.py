import mysql.connector


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

    db.execute(sqlCriminal,('Ed','Theodore','Gein','1906-08-27'))
    db.execute(sqlCriminal,('John','Wayne','Gacy','1942-03-17'))
    db.execute(sqlCriminal,('Theodore','Robert','Bundy','1946-11-24'))
    db.execute(sqlCriminal,('Charles','Milles','Manson','1934-11-12'))


    #db.execute(sqlMedia1)
    #db.execute(sqlMedia2)
    #db.execute(sqlMedia3)

    db_connection.commit()

    print(db.rowcount,"record inserted")

if __name__ == "__main__":
    createTestDB()    
    





