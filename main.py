user = str(input("Enter your DoB, and month of birth,separated by semicoloum:"))

x = user.split(":")
day = int(x[0])
month = str(x[1])

def zodiac():
    if month == "01":
        if day <= 19:
            print("You was born in January, with astrology signs as Capricon")
        elif 20 <= day and day <= 31: 
            print("You are Aquaris")
    elif month == "02":
        if day >= 19 :
            print("You are Aquaris")
        elif day >= 19 and day <= 28:
            print("You a Pisces")
    elif month =="03":
        if day <= 20:
            print("You are Pisces")
        elif 21 <= day and day <= 31:
            print("You are Aries")
    elif month == "04":
        if day <= 19:
            print("You are Aries")  
        elif 20 <= day and day <= 30:
            print("You are Taurus")
    elif month == "05":
        if day <= 20:
            print("You are Taurus")
        elif 21 <= day and day <= 31:
            print("You are Gemini")
    elif month == "06":
        if day <= 20:
            print("You are Gemini")
        elif 21 <= day and day <= 30:
            print("You are Cancer")
    elif month == "07":
        if day <= 22:
            print("You are Cancer")
        elif 23 <= day and day <= 31:
            print("You are Leo")
    elif month == "08":
        if day <=22:
            print("You are Leo")
        elif 23 <= day and day <= 31:
            print("You are Virgo")
    elif month == "09":
        if day <= 22:
            print("You are Virgo")
        elif 23 <= day and day <= 30:
            print("You are Libra")
    elif month == "10":
        if day <= 22:
            print("You are Libra")
        elif 23 <= day and day <= 31:
            print("You are Scorpio")
    elif month == "11":
        if day <= 21:
            print("You are Scorpio")
        elif 22 <= day and day <= 30:
            print("You are Sagittarius")
    elif month == "12":
        if day <= 21:
            print("You are Sagittarius")
        elif 22 <= day and day <= 31:
            print("You are Capricorn")
zodiac()