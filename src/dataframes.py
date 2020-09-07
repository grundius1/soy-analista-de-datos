import pandas as pd
import numpy as np
import re


def cargofilter(df,countries = 0 ):
    '''
    this function takes a dataframe and a list of countries to filter all the dataframe to a dataframe with the statics of cargo from 2008 to 2020 if available of the countries in the list

    if no list is given, the function displays all the countries in the dataframe
    returns a dataframe
    '''
    file = pd.DataFrame(columns = df.columns)
    if countries != 0:
        for item in countries:
            if item not in list(df.Country):
                raise ValueError(f"{item} is not in the list of countries")
            file = pd.concat([file, df[(df.Traffic_type == "Cargo") & (df.Country == f"{item}")]])
        file = file.replace(0,np.nan).dropna(axis=1,how="all")
        return file
    else:
        file = df[(df.Traffic_type == "Cargo")].replace(0,np.nan).dropna(axis=1,how="all")
        return file


def personfilter(df,countries = 0):
    '''
    this function takes a dataframe and a list of countries to filter all the dataframe to a dataframe with the statics of passengers from 2008 to 2020 if available of the countries in the list

    if no list is given, the function displays all the countries in the dataframe
    returns a dataframe
    '''
    file = pd.DataFrame(columns = df.columns)
    if countries != 0:
        for item in countries:
            if item not in list(df.Country):
                raise ValueError(f"{item} is not in the list of countries")
            file = pd.concat([file, df[(df.Traffic_type == "passengers") & (df.Country == f"{item}")]])
        file = file.replace("0",np.nan).dropna(axis=1,how="all")
        return file
    else:
        file = df[(df.Traffic_type == "passengers")]
        return file


def yearsfilter(df, years, qrt = 1):
    '''
    this function takes a dataframe a year or list of two years to obtain all the statistics of cargo and passengers from 2008 to 2020 if available in the dataframe
    the value of qrt={1,2,3} 
        1=gives youall columns, years and quarters
        2= gives you only the years
        3= gives you only quarters
    returns a dataframe
    '''
    columns = []
    if type(years) == int:
        years = [years]
    for item in list(df.columns)[2:]:
        if int(re.findall(r'\d{4}',item)[0]) < years[0]:
            pass
        else:
            columns.append(item)  
    file = pd.DataFrame(df[["Country","Traffic_type"]])
    if len(years) == 1:
        if qrt == 1:
            for item in columns:
                file = pd.concat([file,df[[item]]], axis=1)
        elif qrt == 2:
            for item in columns:
                if "Q" in item:
                    pass
                else:
                    file = pd.concat([file,df[[item]]], axis=1)
        elif qrt == 3:
            for item in columns:
                if "Q" in item:
                    file = pd.concat([file,df[[item]]], axis=1)
                else:
                    pass
        else:
            raise SyntaxError("qrt shoud be 1, 2 or 3")
    elif len(years) == 2:
        end = years[1]
        for item in columns:
            x = re.findall(r'\d{4}', item)
            if int(x[0]) < end:
                if qrt == 1:
                    file = pd.concat([file,df[[item]]], axis=1)
                elif qrt == 2:
                    if "Q" in item:
                        pass
                    else:
                        file = pd.concat([file,df[[item]]], axis=1)
                elif qrt == 3:
                    if "Q" in item:
                        file = pd.concat([file,df[[item]]], axis=1)
                    else:
                        pass
                else :
                    raise SyntaxError("qrt shoud be 1, 2 or 3")
    else:
        raise SyntaxError("array must have 2 ints max")
    return file


def quartersum(df):
    '''
    this function takes a dataframe with only the qurters statistics, and returns a new dataframe with the sum yearly of the quarters given
    
    returns a dataframe
    '''
    
    file = df[["Country"]] 
    for item in range(0,len(df.columns)-1,2):
        x = re.findall(r'\d{4}', df.columns[item])
        if "Q" not in df.columns[item]:
            pass
        else:
            a= df[df.columns[item]]
            b= df[df.columns[item+1]]
            file[x]= a+b
    file = file.set_index("Country")
    file  = file.replace("0",np.nan).dropna(axis=1,how="all")
    return file


if __name__ == "__main__":
    pass