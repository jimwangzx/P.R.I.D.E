import pymongo

from credentials import connection_url

client=pymongo.MongoClient(connection_url)
Database=client.get_database('yt')
api = Database.api

def insert(date, titles, description, video_id, thumbnails, published_at, url):
    queryObject = {
        'Date': date,
        'Title' : titles,
        'Desc' : description,
        'V_ID' : video_id,
        'Thumb' : thumbnails,
        'Pub' : published_at,
        'URL' : url
    }
    query=api.insert_one(queryObject)
    return 'Query inserted'

def find(argument, value):
    queryObject = {argument: value}
    query=api.find_one(queryObject)
    return query


