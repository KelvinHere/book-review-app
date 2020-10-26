genres = ['Absurdist/surreal/whimsical',
'Action',
'Aventure',
'Comedy',
'Crime',
'Drama',
'Fantasy',
'Historical',
'Historical fiction',
'Horror',
'Magical realism',
'Mystery',
'Paranoid fiction',
'Philosophical',
'Political',
'Romance',
'Saga',
'Satire',
'Science fiction',
'Social',
'Speculative',
'Thriller',
'Urban',
'Western']

def insert_genres():
    for genre in genres:
        mongo.db.genres.insert_one( { "genre_name" : genre } )
    