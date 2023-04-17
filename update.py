import pandas as pd 
from pathlib import Path


def excel2csv(inputfile, csvfile):
    df = pd.read_excel(inputfile, index_col='Equipment').T
    df = df.reset_index()
    df = df.rename(columns={'index': 'Equipment'})
    df = df.reset_index()
    df.insert(loc=0, column='SN', value=df['index'] + 1)
    df = df.drop(columns=['index'])
    df =df.reset_index(drop=True).dropna(axis=1, how='all')
    df.to_csv(csvfile, sep =';', index=False)
    return df


entries = Path('../SEIT equipment/')
files = [file for file in entries.iterdir() if (file.suffix=='.xlsx') or (file.suffix=='.xls')]


inputfile='../SEIT equipment/SmartSecLab equipment-ENViSEC-refine.xlsx'
csvfile='table/smartseclab-equip.csv'

excel2csv(inputfile, csvfile)
print('\n================================')
print('The updated file is saved at :', csvfile)
print('================================')