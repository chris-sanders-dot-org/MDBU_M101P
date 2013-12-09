import pymongo
import sys
import exceptions

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
grades=db.grades

def sanity(x):
    sanity = 0
    for doc in x:
        print doc
        sanity += 1
        if (sanity > 10):
            break

def del_hwk():

    recs = []

    query = {'type':'homework'}
    #selector = {'_id':0, 'student_id':1, 'score':1}

    try:
        iter = grades.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    #sanity(iter)

    y = -1
    for doc in iter:
        sid = doc["student_id"]
        did = doc["_id"]
        if sid > y:
            db.grades.remove(did)

        y = sid

del_hwk()
