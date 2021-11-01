#Aquí solo voy a meter las funciones que vaya utilizar
import re


def limpiar_activity(x): #cada elemento que entra en la columna

    """
    Con esta función en realidad estoy haciendo un diccionario donde la key es la columna
     y el value es el patrón de regex. Itero en ese diccionario para que devuelva el valor indicado
     si cumple la condición, y sino me devuelva el valor "other".
    """
    dicc_actividades = {"Fishing":re.search(".*[Ff](ishing|ISHING).*",str(x)),"Swimming":re.search(".*[Ss](wimming|WIMMing).*",str(x)),"Kite":re.search(".*[Kk](ite|ITE).*",str(x)),"Walking":re.search(".*[Ww](alking|ALKING).*",str(x)),"Boogie Board":re.search(".*[Bb](oogie|OOGIE).*",str(x)),"Body Boarding":re.search(".*[Bb](ody|ODY).*",str(x)),"Wind Surfing":re.search(".*[wW](ind|IND).*",str(x)),"Boat":re.search(".*[Bb](oat|OAT).*",str(x)),"Interact with sharks":re.search(".*[Ss](hark|HARK).*",str(x)),"Diving":re.search(".*[Dd](iving|IVING).*",str(x)),"Standing in water":re.search(".*[Ss](tand|TAND).*",str(x)),"Paddling":re.search(".*[Pp](addl|ADDL).*",str(x)),"Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),"OverBoard":re.search(".*[Oo](verb|VERB).*",str(x)),"Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),"Floating":re.search(".*[Ff](loat|LOAT).*",str(x)),"Jumping":re.search(".*[Jj](ump|UMP).*",str(x))}
    for key,values in dicc_actividades.items():
        if values:
            return key
        
    return "other"


def limpiar_species(x):
    dicc_especies = {
            "White shark":re.search(".*[Ww](hite|HITE).*",str(x)),
            "Tiger shark":re.search(".*[Tt](iger|IGER).*",str(x)),
            "Lemon shark":re.search(".*[Ll](emon|EMON).*",str(x)),
            "Hammerhead shark":re.search(".*[Hh](ammerhead|AMMERHEAD).*",str(x)),
            "Bull shark":re.search(".*[Bb](ull|ULL).*",str(x)),
            "Blue shark":re.search(".*[Bb](lue|LUE).*",str(x)),
            "Silvertip shark":re.search(".*[Ss](ilvertip|ILVERTIP).*",str(x)),
            "Nurse shark":re.search(".*[Nn](urse|URSE).*",str(x)),
            "Whaler shark":re.search(".*[Ww](haler|HALER).*",str(x)),
            "Blacktip shark":re.search(".*[Bb](lacktip|LACKTIP).*",str(x)),
            "Mako shark":re.search(".*[MM](ako|AKO).*",str(x)),
            "Sand shark":re.search(".*[Ss](and|AMD).*",str(x)),
            "Wobbegong shark":re.search(".*[Ww](obbegong|OBBEGONG).*",str(x)),
            "Galapagos shark":re.search(".*[Gg](alapagos|ALAPAGOS).*",str(x)),
            "Grey shark":re.search(".*[Gg](rey|REY).*",str(x)),
            "Leopard shark":re.search(".*[Ll](eopard|EOPARD).*",str(x)),
            "Zambesi shark":re.search(".*[Zz](ambesi|AMBESI).*",str(x)),
            "Blacktail shark":re.search(".*[Bb](lacktail|LACKTAIL).*",str(x)),
            "Red shark":re.search(".*[Rr](ed|ED).*",str(x)),
            "Dusky shark":re.search(".*[Dd](usky|USKY).*",str(x)),
            "Raggedtooth shark":re.search(".*[Rr](aggedtooth|AGGEDTOOTH).*",str(x)),
            "Spinner shark":re.search(".*[Ss](pinner|PINNER).*",str(x)),
            "Cow shark":re.search(".*[Cc](ow|OW).*",str(x)),
            "Porbeagle shark":re.search(".*[Pp](orbeagle|ORBEAGLE).*",str(x)),
            "Caribbean reef shark":re.search(".*[Cc](aribbean|ARIBBEAN).*",str(x)),
            "Sandbar shark":re.search(".*[Ss](and|AND).*",str(x)),
            "Silky shark":re.search(".*[Ss](ilky|ILKY).*",str(x)),
            "Zambezi shark":re.search(".*[Zz](ambezi|AMBEZI).*",str(x)),
            "Sevengill shark":re.search(".*[Ss](evengill|EVENGILL).*",str(x)),
            "Copper shark":re.search(".*[Cc](opper|OPPER).*",str(x)),
            "Angel shark":re.search(".*[Aa](ngel|NGEL)\s",str(x)),
            "Salmon shark":re.search(".*[Ss](almon|ALMON).*",str(x)),
            "Goblin shark":re.search(".*[Gg](oblin|OBLIN).*",str(x)),
            "Thresher shark":re.search(".*[Tt](hresher|HRESHER).*",str(x)),
            "Dogfish shark":re.search(".*[Dd](ogfish|OGFISH).*",str(x)),
            "Involvement not confirmed":re.search("[^.?!]*involvement[^.?!]*",str(x))}
    for key,values in dicc_especies.items():
        if values:
            return key

    return "other_specie"


def limpiar_injury(x):
    dicc_injury= {"No injury":re.search(".*[Nn](o|O)\s*[Ii](njury|NJURY).*",str(x)),"Hand injury":re.search(".*[Hh](and|AND).*",str(x)),"Minor injury":re.search(".*[Mm](inor|INOR).*",str(x)),"Leg injury":re.search(".*[Ll](eg|LEG).*",str(x)),"Fatal injury":re.search(".*[Ff](atal|ATAL).*",str(x)),"Foot injury":re.search(".*[Ff](oot|OOT).*",str(x)),"Severe injury":re.search(".*[Sv](evere|EVERE).*",str(x)),"Head injury":re.search(".*[Hh](ead|EAD).*",str(x)),"Laceration injury":re.search(".*[Ll](aceration|ACERATION).*",str(x)),"Abdomen injury":re.search(".*[Aa](bdomen|BDOMEN).*",str(x)),"Abrasion injury":re.search(".*[Aa](brasion|BRASION).*",str(x)),"Toe injury":re.search(".*[Tt](oe|OE).*",str(x))}
    for key,values in dicc_injury.items():
        if values:
            return key

    return "other_injury"



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


