import mysql.connector
from datetime import datetime

class BookManager:
    def __init__(self):
        self.connect=mysql.connector.connect(host="localhost",
                                             user="root",
                                             database="library_db",
                                             password="Kashyap@10")

    def get(self):
        try:
            self.cursor=self.connect.cursor()
            query="select * from book"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            print("ALL BOOKS")
            for i in record:
                print(i)
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor=self.connect.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                print("id=",id)
                print(record)
            else:
                print("record not found")
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            query="insert into book(title,author,category,price,published_date) values (%s,%s,%s,%s,%s)"
            self.cursor=self.connect.cursor()
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Added the book")
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                print("Deleting")
                query="delete FROM book WHERE id=%s"
                values=(id,)
                self.cursor.execute(query, values)
                self.connect.commit()
                self.get()
            else:
                print("Book Not Found\n\n")
        except Exception as e:
            print(e)


    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record!=None:
                self.cursor=self.connect.cursor()
                placeholder=""
                for i in kwargs.keys():
                    placeholder+=i+"="+"%s,"
                placeholder=placeholder.rstrip(", ")
                print("Updating Id:", id)
                values=[v for v in kwargs.values()]
                values.append(id)
                query=f"update book set {placeholder} where id=%s"
                self.cursor.execute(query, values)
                self.connect.commit()
            else:
                print("Book Not Found")
        except Exception as e:
            print(e)





b=BookManager()
b.get()
b.retrieve(id=3)
b.delete(id=4)
#b.post(title="book2",author="kaushik",category="action",price=200.90,published_date=datetime.now())
b.put(id=3,title="book_put")
b.get()
