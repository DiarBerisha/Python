from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello"}
#uvicorn main:app --reload

@app.get("/kurset")
def return_kurset():
    return{"kurset":["Pythin","code1","code2"]}

@app.get("/kurset/{kursi_id}")
def return_kurset(item_id:int):
    return{"kurset":["Pythin","code1","code2"]}


@app.post("/register")
def create_user(name:str , password:str):
    return {"user_id":name,"password":password}


@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return { "message":"item is deleted"}

@app.put("/user/password/{user_id}")
def change_Password(usure_id:int,password:str):
    return { "message":"password is changed"}

