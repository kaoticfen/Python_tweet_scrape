# encoding: utf-8

import tweepy
import pymysql

def create_connection(server, db, port=3306):
    # type: (object, object, object) -> object
    #user = input("Username: ")
    #u_pw = getpass.getpass()
    user = "cfennell"
    u_pw = "Grooten04!"
    connection = pymysql.connect(
        user=user,
        password=u_pw,
        host=server,
        database=db,
        port=port)
    return connection