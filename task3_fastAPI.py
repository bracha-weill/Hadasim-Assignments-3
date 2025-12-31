from fastapi import FastAPI
from typing import Dict, Any
import json,os

app = FastAPI()

# קובץ לשמירת האובייקטים
DATA_FILE = "data.json"

#1. כתיבת נתונים
@app.post("/append")
#פונקציה שמקבלת את האובייקט החופשי
def append_payload(payload:Dict[str,Any]):
    #אם הקובץ עוד לא קיים - תיצור רשימה ריקה שאליה נכניס את הקלט מהלקוח
    if not os.path.exists(DATA_FILE):
        data = []
    else:
        #אם הקובץ קיים תכניס לרשימה את כל האובייקטים הקיימים
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    #נדחוף לרשימה את הקלט מהלקוח
    data.append(payload)
    #נפתח את הקובץ לכתיבה ונרשום את הרשימה המעודכנת בצורה קריאה
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    #החזרת תגובה ללקוח
    return {"status": "payload saved"}

#2. קבלת 10 אובייקטים אחרונים
@app.get("/10last")
def get_10last_payload():
    #אם הקובץ לא קיים החזרת רשימה ריקה
    if not os.path.exists(DATA_FILE):
        return []
    
    #פתיחת הקובץ לקריאה והעברת האובייקטים לרשימה
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    #החזרת 10 אובייקטים אחרונים
    return data[-10:]