import DBRepository

db = {'url': 'alsdkjlaskd', 'username': 'asdasd',
      'password': 'asdasd', 'port': 'askldjhaks', 'dbvendor': 'asdad'}

dbRepository = DBRepository.DBRepository()

print(dbRepository.collection)
dbRepository.addDB(db)
print(dbRepository.collection)