from app import mongo
from bson.objectid import ObjectId

# Insert new field into all documents
# mongo.db.books.update_many({},{ '$set': {"review_num": 0}})

#find length of all reviews
agg = mongo.db.books.aggregate([
  {
    "$project": {
      "number_of_reviews": {
        "$size": "$reviews"
      }
    }
  }
])

for each in agg:
    print(each['number_of_reviews'])
    print(each['_id'])
    mongo.db.books.update_one({'_id': ObjectId(each['_id'])},
                               {'$set': {
                                   'review_num': each['number_of_reviews']
                                }} )