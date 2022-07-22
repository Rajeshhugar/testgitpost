import pymongo
client = pymongo.MongoClient("mongodb+srv://hugar_rajesh:Rajesh_0808@rajesh.ud2bw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

d= {
    "name":"Rajesh Hugar",
    "email_id":"rajesh_hugar@yahoo.in",
    "surname":"hugar",
    "Job_descrition":"Machine Learning Engineer"

}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
