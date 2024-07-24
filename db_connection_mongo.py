#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
from pymongo import MongoClient

def connectDataBase():

    # Create a database connection object using pymongo
    DB_NAME = "CPP"
    DB_HOST = "localhost"
    DB_PORT = 27017

    try:
        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]

        return db

    except:
        print("Error, database not connected")

def createDocument(col, docId, docText, docTitle, docDate, docCat):

   # create a dictionary to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    docTerms = doc_text.lower().split(" ")
    count_terms = {}

    for i in docTerms:
        if i in count_terms:
            count_terms[i] += 1
        else:
            count_terms[i] = 1

    # create a list of dictionaries to include term objects. [{"term", count, num_char}]
    term_obj = [{"term": i, "count": j} for i, j in count_terms.items()]

    #Producing a final document as a dictionary including all the required document fields
    doc = {
        "_id": doc_id,
        "text": doc_text,
        "title": doc_title,
        "date":doc_date,
        "category": doc_cat,
        "terms": term_obj
    }

    # Insert the document
    col.insert_one(doc)

def deleteDocument(col, docId):

    # Delete the document from the database
    col.delete_one(col, docId)

def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    deleteDocument(col, docId)

    # Create the document with the same id
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3'}
    # ...
    index = {}
    docs = col.find()

    for doc in docs:
        for term_obj in doc["terms"]:
            term = term_obj["terms"]
            count = term_obj["count"]
            if term in index:
                index[term].append(f"{doc['title']}:{count}")
                
    return index
