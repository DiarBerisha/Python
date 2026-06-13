# {
#     "book1":{ 
#         "title":"Beni Ecen Vetem",
#         "author":"Ismail Kadare",
#         "year":"1920",
#         "genre":"vetmi"

#         },
#     "book2":{ 
#         "title":"80 mijë milje nën det",
#         "author":"Jules Verne",
#         "year":"1920",
#         "genre":"fantazi"

#         },
#     "book3":{ 
#         "title":"Plaku dhe deti",
#         "author":"Ernest Hemingway",
#         "year":"1920",
#         "genre":"fantazi"

#         }
# }
from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def root():
    return{
    "book1":{ 
        "title":"Beni Ecen Vetem",
        "author":"Ismail Kadare",
        "year":"1920",
        "genre":"vetmi"

        },

    "book2":{ 
        "title":"80 mijë milje nën det",
        "author":"Jules Verne",
        "year":"1920",
        "genre":"fantazi"

        },

    "book3":{ 
        "title":"Plaku dhe deti",
        "author":"Ernest Hemingway",
        "year":"1920",
        "genre":"fantazi"

        }}