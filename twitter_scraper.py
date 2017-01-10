# -*- coding: utf-8 -*-
import tweepy
import pymysql
import common

def create_connection(server, db, port=3306):
    # type: (object, object, object) -> object
    #user = input("Username: ")
    #u_pw = getpass.getpass()
    user = "twitterdata"
    u_pw = "Grooten04!"
    connection = pymysql.connect(
        user=user,
        password=u_pw,
        host=server,
        database=db,
        port=port)
    return connection

def url_extractor(tweet):
    url = tweet._json["entities"]["urls"][0]["expanded_url"]
    if not is_shortened(url):
        url = resolve(url)
    return(url)

def pull_tweets(query):

    #this encapsulates the twitter key(s)
    api = common.twitter_connect()

    # Pull in the tweets
    results = []

    results = api.search(q=query, count=200)

    return (results)



def write_tweets_to_table(tablename):
    try:
        connection = create_connection('rambalf.cas.msu.edu', 'fennell_production_copy')
        print(connection.server_status)

        # Create the table you want to parse
        sql = """ """

        # Excute the table command
        common.create_table(connection, 'url_info_normalized', sql)

        with connection.cursor() as cursor:
            # Get everything from url_info
            sql = """SELECT * FROM url_info"""
            cursor.execute(sql, )
            result = cursor.fetchall()

            for row in result:
                # normalize the domains
                cursor.execute(sql_to_table)

            print(result)
    finally:
        connection.close()
        # server.stop()


if __name__ == '__main__':
    #create database connection
    conn = create_connection("localhost", "twitter_data")

    #sql used to create the table that we want to store
    sql = ("""CREATE TABLE IF NOT EXISTS tweets_table
                    (p_id INT(11) AUTO_INCREMENT PRIMARY KEY,
                     twitter_id VARCHAR(255),
                     created_at VARCHAR(255),
                     texts VARCHAR(255),
                     url VARCHAR(255))
                     ENGINE=MyISAM CHARACTER SET utf8 COLLATE utf8_general_ci;""")

    #Build the table to store the tweets
    common.create_table(conn, "tweets_table", sql)

    #search terms
    searchquery = ["clown", "clownsightings"]

    #pull tweets for that we are looking for
    all_tweets = pull_tweets(searchquery)

    #
