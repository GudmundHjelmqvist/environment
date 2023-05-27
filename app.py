import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def read_csv(source:str,skiprows:int=0)->pd.DataFrame:
    """
    Read csv-files
    """
    df=pd.read_csv(source, skiprows=skiprows)
    return df
 
def read_excel(source:str, skiprows:int=0)->pd.DataFrame:
    """
    Read excel-files
    If you want to choose specific sheet add 
    sheetname=sheet -> pd.read_excel(source, skiprows=skiprows, sheetname=sheet)
    """
    skiprows=0
    df=pd.read_excel(source, skiprows=skiprows)
    return df

def change_column_dtype(df, col, data_types_dict):
    """
    Change dtype of a column
    data_types_dict = {'column': dtype}

    possible dtypes: 
        'datetime64[ns, <tz>]'
        'category'
        'period[<freq>]'
        'Sparse', 'Sparse[int]', 'Sparse[float]'
        'interval', 'Interval', 'Interval[<numpy_dtype>]', 'Interval[datetime64[ns, <tz>]]', 'Interval[timedelta64[<freq>]]'
        'Int8', 'Int16', 'Int32', 'Int64', 'UInt8', 'UInt16', 'UInt32', 'UInt64'	
        'Float32', 'Float64'
        'string'
        'boolean'

    """
    return df.astype(data_types_dict)


a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]
c=[1,2,3,4,5,6,7,8,9,10]
df=pandas.DataFrame(index=a)
df['a']=a
df['b']=b
fig = plt.figure(figsize=(10, 4))
sns.lineplot(df)
st.pyplot(fig)