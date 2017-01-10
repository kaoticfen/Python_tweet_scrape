# -*- coding: utf-8 -*-

import pymysql
import requests, base64
import tweepy
from settings import consumer_key, consumer_secret,access_token,access_secret

#This create table is a bit cleaner
def create_table(conn, table_name, sql):

    #Add the table name to the query.
    sql = sql.format(table_name)

    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print("Error creating table: {}".format(str(e)))

#this definition creates the connection to the twitter api
def twitter_connect():
    # Authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return (tweepy.API(auth))


