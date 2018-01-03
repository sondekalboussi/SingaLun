import pandas as pd  
import numpy as np 
from sklearn.preprocessing import Imputer

def data_to_df(filename,file_extension,sep,sheet='',x):
    'this function read a files(csv,excel,table) and convert it into a pandas dataframe'
    if file_extension=='csv' or file_extension=='txt':
        df=pd.read_file_extension(filename,sep=sep,skiprows=x,error_bad_lines=False)#multidelimeter files with information rows
    if file_extension=='xslx':
        df=pd.read_excel(filename, sheet_name=sheet)
    #df.drop('Unnamed: 0', axis=1, inplace=True)#drop first umpty column with NA or empty cells
    #dfs.to_csv('Metabolite.txt', sep='\t',encoding='utf-8', index=False)
    print ('DataFrame from the ',filename,' has been created. Size= ',str(df.size),'.')
    return df
    
def na_handeling(df,drop=True,impute=True,column_extension=''):
    '''1-Check if the some columns are redundante, remove the duplication extension in the column name to find them and remove these columns
     2-Check if the dataset contains missing values if do get rid of them either by dropping them or imputing them
    '''
    column_names=[col for col in df.columns]
    #method1
    new=[]#column names without any extension
    for col in column_names:
        if column_extension in col:
            n=col.split(column_extension)[0]
            new.append(n)
        else:
            n=col
            new.append(n)
    df.columns=new  #change the column names          
    duplicates=df.columns.duplicated()
    df=df.loc[:,~duplicates]
    #method2
    redundant=''
    for i in range(len(column_names)):
        if column_names[i].endswith('.1'):
            redundant=column_names[i]
    df.columns.get_loc(redundant)
    df=data.drop(redundant,axis=1)
    #check if there are missing values
    nbre_missing=df.isnull().sum().sum()
    if nbre_missing==0:
        clean_data=df
        print ('There are no missing values in your dataset!')
        return clean_data
    else:
    #Na_drop
        if drop and not impute:
            data_clean=df.dropna()
            print ('The clean_dataframe size is: ',str(data_clean.shape))
            return clean_data
     #Amputation   
        else:
            my_imputation=Imputer(strategy='median')
            clean_data=my_imputation.fit_transform(df)
            print ('The clean_dataframe size is: ',str(data_clean.shape))    
            return clean_data    
