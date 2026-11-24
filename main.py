from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def header():
    return {
        "message": "My first API with FastAPI"
    }

@app.get("/about")
def home():
    return{
        "about":"this api in work with modern technologies and frameworks like fastapi, python",
        "technologies":"fastapi web framework,python",
        "course":"this api is part of a course on fastapi and python"
    }
@app.get("/contact")
def info():
    return[{
        "phone number":"123-456-7890",
        "email": "abc@gmail.com"
    }]

@app.get("/student")
def course_name(stud_name:str,rollno:int):
    return{
        "Student Name":stud_name,
        "Roll No":rollno
    }

@app.get("/student/{c_id}")
def learn(c_id:int):
    return {
        "course_id":c_id,
        "topic":"python basic , data visualization , streamlit(ui design)"
    }



