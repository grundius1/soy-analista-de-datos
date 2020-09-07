import re

def valuechanger(old, new, indexlist):
    '''
    this function changes an specific value or data from a dataset,the imputs are the index old name/value to change,
    the new value and the list where the data will be changed, the return is a list.
    '''
    alist = list(indexlist)
    index = alist.index(old)
    alist[index] = new
    return alist

def valueschanger(old, indexlist):
    '''
    this function allows you to make a list with the values you want to change of a list and ask you to promptthe new values for 
    each or value in the list
    '''
    for item in old:
        new = input(f"which value do you wat to put instead of {item}: ")
        indexlist = valuechanger(item,new,indexlist)
    return indexlist



def countrychanger(serie):
    '''this finction uses a dictionary to replace the 2 letters country by its name
    '''
    countries = {
        'Belgium':'BE',
        'Greece':'EL',
        'Lithuania':'LT',
        'Portugal':'PT',
        'Bulgaria':'BG',
        'Spain':'ES',
        'Luxembourg':'LU',
        'Romania':'RO',
        'Czechia':'CZ',
        'France':'FR',
        'Hungary':'HU',
        'Slovenia':'SI',
        'Denmark':'DK',
        'Croatia':'HR',
        'Malta':'MT',
        'Slovakia':'SK',
        'Germany':'DE',
        'Italy':'IT',
        'Netherlands':'NL',
        'Finland':'FI',
        'Estonia':'EE',
        'Cyprus':'CY',
        'Austria':'AT',
        'Sweden':'SE',
        'Ireland':'IE',
        'Latvia':'LV',
        'Poland':'PL',
        'United Kingdom':'UK',
        'Iceland':'IS',
        'Norway':'NO',
        'Liechtenstein':'LI',
        'Switzerland':'CH',
        'Montenegro':'ME',
        'North Macedonia':'MK',
        'Albania':'AL',
        'Serbia':'RS',
        'Turkey':'TR', 
        'EU Total': 'TOTAL'  
    }
    #print(type(countries))
    #print(type(serie))
    #print(serie)
    for k,v in countries.items():
        #print(k,v)
        x = re.findall(rf',{v}(\b|,)', serie)
        #print(x)
        if x != []:
            return f"{k}"
    
    return serie














if __name__ == "__main__":
    x = ['Austria passengers', 'Belgium passengers', 'Bulgaria passengers',
       'Croatia passengers', 'Cyprus passengers', 'Czechia passengers',
       'Denmark passengers', 'Estonia passengers',
       'European Union - 28 countries (2013-2020) passengers',
       'Finland passengers', 'France passengers',
       'Germany (until 1990 former territory of the FRG) passengers',
       'Greece passengers', 'Hungary passengers', 'Iceland passengers',
       'Ireland passengers', 'Italy passengers', 'Latvia passengers',
       'Lithuania passengers', 'Luxembourg passengers', 'Malta passengers',
       'Montenegro passengers', 'Netherlands passengers',
       'North Macedonia passengers', 'Norway passengers', 'Poland passengers',
       'Portugal passengers', 'Romania passengers', 'Serbia passengers',
       'Slovakia passengers', 'Slovenia passengers', 'Spain passengers',
       'Sweden passengers', 'Switzerland passengers', 'Turkey passengers',
       'United Kingdom passengers']