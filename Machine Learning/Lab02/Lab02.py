import pandas as pd


def remove_values(series):
    return series[series == 'KOBIETA']


def reformat_values(series):
    return series.str.title()


sex = pd.Series(['KOBIETA',
                 'KOBIETA',
                 'KOBIETA',
                 'Zofia',
                 'Kobieta',
                 'InneCos'],
                index=[
                    'ZOFIA',
                    'ZUZANNA',
                    'Darek',
                    'Cos1',
                    'Cos2',
                    'KOBIETA'])

sex = remove_values(sex)
print(sex)
sex = reformat_values(sex)
print(sex)
