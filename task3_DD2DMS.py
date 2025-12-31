def dd2dms(dd, is_latitude = True):
    #קביעת כיוון (לפי חיובי/שלילי וערך הרוחב שהפונקציה קיבלה)
    direction = ""
    if is_latitude:
        direction = 'N' if dd >= 0 else 'S'
    else:
        direction = 'E' if dd >= 0 else 'W'
    #שימוש בערך המוחלט לצורך החישובים
    dd = abs(dd)
    #שליפת המספר השלם
    degrees = int(dd)
    #שליפת דקות +שניות
    min_sec = (dd-degrees)*60
    #הפרדת דקות למשתנה
    minutes = int(min_sec)
    #השמת ערך השניות למשתנה
    seconds = (min_sec-minutes)*60
    return [degrees, minutes, round(seconds, 2), direction]
