#Aquí solo voy a meter las funciones que vaya utilizar
def sustitucion(s,b):

    """
    Con esta función conseguiré que todos los valores de s que estén en b,
    me aparezcan en la lista b como Unknown.
     
    """
    for i,p in enumerate(s):
        if p in b:
            b[i]="Unknown"
        return b



def mes (x):

    """
    Con esta función filtaré la columna Date, para que en cualquier valor que figure un mes
    me indique solamente dicho mes y ningún dato más
    
    """
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


