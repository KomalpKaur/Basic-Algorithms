import mysql.connector
import time

a=time.time()
class DBHelper:
    def fetchAllStudentInDB(self):
        # 1. create SQL statement
        sql = "select * from Student"

        # 2.create connection with database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="DaaLab")

        # 3. Obtain Cursor to execute sql statements
        cursor = con.cursor()
        cursor.execute(sql)

        rows=cursor.fetchall()
        #print(rows)            #print all rows , row is a list of Tuples , 1Tuple represents row, print rows as list of tuples
        list=[]
        for row in rows:
            rm=row[2]         #print all rows in next lines
            list.append(rm)
        print("list of roll numbers are:")
        for i in list:
            print(i)

        roll=int(input("Enter the roll number you want to search"))
        beg=0
        end=len(list)
        while(beg<end):
            mid=int((beg+end)/2)
            if (roll==list[mid]):
                print("Rollnumber",roll," is found at location",mid,"of the list.")
                break
            elif(roll < list[mid]):
                end=mid-1
            elif (roll > list[mid]):
                beg = mid + 1
            else:
                print("wrong input")


# Model

class Student:

    def __init__(self, name, urn, phone):
        self.name = name
        self.urn = urn
        self.phone = phone

    def showStudentDetails(self):
        print(">> Name: {}   urn: {}  Phone: {}".format(self.name, self.urn, self.phone))


db = DBHelper()
db.fetchAllStudentInDB()

b=time.time()
c=b-a
print("time taken=",c)
