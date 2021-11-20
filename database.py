import pymongo

if "__main__" == __name__:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['ToDo']
    collection = db['tasks']
    data = {"title":"ToDo","message":"First ToDo","date":"20 nov 2021,8:54PM","complete":True}
    collection.insert_one(data)

    collection = db['user']
    data = {"name":"shivam","email":"shivammandloi1102@gmail.com","password":"shivam101"}
    collection.insert_one(data)

    collection = db['otp']
    data = {"email":"shivammandloi1102@gamil.com","otp":12131,"time":"20 nov 2021,8:54PM"}
    collection.insert_one(data)