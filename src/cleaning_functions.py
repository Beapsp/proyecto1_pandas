#Aquí solo voy a meter las funciones que vaya utilizar
def mes (x):
    for i in x:
        if "Jan" in x:
            return "January"
        elif "Feb" in x:
            return "February"
        elif "Mar" in x:
            return "March"
        elif "Apr" in x:
            return "April"
        elif "May" in x:
            return "May"
        elif "Jun" in x:
            return "Juny"
        elif "Jul" in x:
            return "July"
        elif "Aug" in x:
            return "August"
        elif "Sep" in x:
            return "September"
        elif "Oct" in x:
            return "October"
        elif "Nov" in x:
            return "November"
        elif "Dec" in x:
            return "December"
        else:
            return "Other"