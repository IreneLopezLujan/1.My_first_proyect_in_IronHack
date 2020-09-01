import re

def muertes_si_no (x):

    if x in ["Y", "y"]:
            return "Yes"
    elif x in ["N"," N"," N"]:
            return "No"    
    return "Unknown"

def comparing_cols (column_1, column_2,column_3=None):
    """
    Compara el numero de valores iguales de 1 o dos columnas con respecto a otra principal
    """
    
    comparativa_1=column_1.isin(column_2).sum()
    comparativa_2=column_1.isin(column_3).sum()
    
    if comparativa_1 >comparativa_2 :
        return "la columna 2 tiene mas valores iguales:"+ str(comparativa_1)
    #f"{}tiene mas coincidencias ({})con column_1 que {}".format(column_2.name,comparativa_1,column_3.name)  
    #no entiendo porque format no me funciona en esta def. 
    else:
        return "la columna 3 tiene más valores iguales:" +str(comparativa_2)
    #f"{}tiene mas coincidencias ({})con column_1 que {}".format(column_3.name,comparativa_2,column_2.name)
    
  


def sex_def (x):
    """
    normaliza la columna sex
    """
    if x in ['N', '.', 'lli', 'M ', 'F', 'M']:
        return "Undefined"   
    return "Unknown"



def year(x):
    """
Clasifica años por decadas
    """
    if x >= 1930 and x <=1939:
        return "1930's"
    if x >= 1940 and x <=1949:
        return "1940's"
    if x >= 1950 and x <=1959:
        return "1950's"
    if x >= 1960 and x <=1969:
        return "1960's"
    if x >= 1970 and x <=1979:
        return "1970's"
    if x >= 1980 and x <=1989:
        return "1980's"
    if x >= 1990 and x <=1999:
        return "1990's"
    if x >= 2000 and x <=2010:
        return "2000's"
    if x >= 2010:
        return "2010's"
    

def get_ing (activities):

    lista=[]
    for activity in activities:    
        a = re.findall('ing', activity)
        if len(a) > 0:
            lista.append(activity)
        else:
                lista.append('Unknown')
    return lista
