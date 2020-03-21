import json

class DBRepository:
    def __init__(self):
        self.filepath = './repository/files/dbs.json'
        with open(self.filepath, 'r') as file:
            self.collection = json.load(file)

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.collection, file)

    def addDB(self, db):
        self.collection.append(db)
        self.save()

    def removeDB(self, db):
        self.collection.remove(db)
        self.save()
