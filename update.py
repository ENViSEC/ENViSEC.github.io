import pandas as pd
from pathlib import Path
from tabulate import tabulate


def excel2csv(inputfile, csvfile):
    print(f'Processing at: {f}')
    df = pd.read_excel(inputfile, index_col='Equipment')
    df = df.reset_index()
    df = df.rename(columns={'index': 'Equipment'})
    df = df.rename_axis('SN', axis=1)
    df = df.reset_index(drop=True).dropna(axis=1, how='all')
    df = df[['Equipment', 'Quantity', 'Applications']]
    # print(tabulate(df))
    df.to_csv(path_or_buf=csvfile,
              sep=';',
              encoding='utf-8',
              quotechar='"',
              doublequote=True,
              index=False,
              )
    print(f'The updated file is saved at: {csvfile}')
    print('='*30)
    return df


if __name__ == "__main__":
    entries = Path('../SEIT/')
    files = [file for file in entries.iterdir() if (file.suffix == '.xlsx')
             or (file.suffix == '.xls')]

    for f in files:
        if len(pd.read_excel(f)):
            excel2csv(
                inputfile=f,
                csvfile='table/' + f.stem + '.csv'
            )
        else:
            print(f'{f} is empty')
            print('='*30)
