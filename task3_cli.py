import typer,json,os

app = typer.Typer()

#קובץ לשמירת האובייקטים
DATA_FILE = "data.json"

#יצירת פקודה חדשה
#הפקודה קולטת מהמשתמש סטרינג
@app.command()
def append_payload(payload:str):
    #בדיקה על הקלט
    #אם המחרוזת לא מכילה סטירנג ולידי
    #הפקודה תסיים את ההרצה ותפלוט הודעת שגיאה מתאימה
    try:
        #אם הקלט תקין המרה ל json והשמה במשתנה
        json_arg = json.loads(payload)
    except json.JSONDecodeError:
        typer.echo("Invalid JSON string")
        raise typer.Exit(code=1)
    
    #יצירת רשימה ריקה במקרה שהקובץ לא קיים
    if not os.path.exists(DATA_FILE):
        data = []
    else:
        #העברת האובייקטים לרשימה (במקרה שהקובץ קיים)
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    #דחיפת האוביקט לרשימה
    data.append(json_arg)
    #כתיבת הרשימה המעודכנת לקובץ
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    #פלט למשתמש
    typer.echo("Successfully appended!")

#יצירת פקודה חדשה
#קבלת 10 אוביקטים אחרונים
@app.command()
def get_10last():
    #העברת האוביקטים שבקובץ לרשימה
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    #העברת עשרה אוביקטים אחרונים לרשימה נוספת
    latest = data[-10:]
    #פלט למשתמש בצורה קריאה
    typer.echo(json.dumps(latest,indent=2))

#Entry Point
if __name__ == "__main__":
    app()