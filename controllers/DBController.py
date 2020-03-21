import os
import repository.DBRepository as DBRepository

class DBController:
    def __init__(self):
        self.repository = DBRepository.DBRepository()
        self.dbVendors = ["POSTGRESQL"]

    def addDB(self):
        url = raw_input("URL: ")
        port = raw_input("PORT: ")
        dbname = raw_input("DBNAME: ")
        alias = raw_input("ALIAS: ")
        username = raw_input("USERNAME: ")
        password = raw_input("PASSWORD: ")
        dbvendor = raw_input("DBVENDOR: ")

        db = {
            'url': url,
            'port': port,
            'dbname': dbname,
            'alias': alias,
            'username': username,
            'password': password,
            'dbvendor': dbvendor
        }

        self.repository.addDB(db)

    def removeDB(self):
        self.show()
        index = raw_input("Numero do banco de dados: ")
        db = self.repository.collection[int(index) - 1]
        self.repository.removeDB(db)

    def show(self):
        N = len(self.repository.collection)
        for i in range(0,N):
            db = self.repository.collection[i]
            print(str(i + 1) + ": " + db['alias'] + " - " + db['url'] + ":" + db['port'] + "/" + db['dbname'])


    def connectDB(self):
        self.show()
        index = raw_input("Numero do banco de dados: ")
        db = self.repository.collection[int(index) - 1]
        command = "PGPASSWORD=" + db['password'] + " && psql -U " + db['username']
        os.system(command)

    def createDB(self):
        self.show()
        index = raw_input("Numero do banco de dados: ")
        db = self.repository.collection[int(index) - 1]
        command = "PGPASSWORD=" + db['password'] + " && psql -U " + db['username'] + " --command=\"create database " + db['dbname'] + ";\""
        print(command)
        os.system(command)

    def dropDB(self):
        self.show()
        index = raw_input("Numero do banco de dados: ")
        db = self.repository.collection[int(index) - 1]
        command = "PGPASSWORD=" + db['password'] + " && psql -U " + db['username'] + " --command=\"drop database " + db['dbname'] + ";\""
        os.system(command)

    def selectDB(self):
        self.show()
        index = raw_input("Numero do banco de dados: ")
        return self.repository.collection[int(index) - 1]

    def loadDump(self):
        db = self.selectDB()
        dumppath = raw_input("Caminho do dump: ")
        command = "PGPASSWORD=" + db['password'] + " && psql -U " + db['username'] + " -d " + db["dbname"] + " -a -f " + dumppath
        print(command)
        os.system(command)
