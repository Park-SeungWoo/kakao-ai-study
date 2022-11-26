import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
# pd.set_option('expand_frame_repr', False)  # same as above
# pd.describe_option('display')  # show options

df = pd.read_excel('./lecture_datas/crime/관서별 5대범죄 발생 및 검거.xlsx', engine='openpyxl')

# print(type(df))
# print(df.head(3))
# print(df.tail(3))
# print(df.info())
# print(df.describe().iloc[:,2:])
# print(df.info())
# print(df[df['살인(발생)']==141]['관서명'])
# print(df)

#### remove totaled row and columns
# df_datas_only = df.drop([0])
# df_datas_only = df.drop(list(df[df['관서명']=='계'].index))
# df_datas_only.drop(['소계(발생)', '소계(검거)'], axis=1, inplace=True)
# print(df_datas_only.describe())

### show the max values each of crimes
# print(df_datas_only.max(numeric_only=True))
### check specific location's data that has the max value in '살인(발생)'
# print(df_datas_only[df_datas_only['살인(발생)']==12])

# print(df.head(3))

###### group as the state of polices
police_to_gu = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
                '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
                '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
                '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
                '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
                '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구',
                '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구',
                '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}
df_new = df.drop([0])
# df_new['state'] = df_new['관서명'].apply(lambda x: police_to_gu.get(x, '구 없음'))
df_new['state'] = df_new['관서명'].apply(lambda x: police_to_gu[x])
# print(df_new.isna().sum())
df_temp = df_new.set_index('state')
# print(df_temp.head())
df_temp.sort_index(inplace=True)
# print(df_temp)
# df_temp = df_temp.reset_index()
# print(df_temp.head())

#######pivot table
state_df = pd.pivot_table(df_temp, index='state', aggfunc=np.sum)
# print(state_df.info())
# print(len(state_df))
state_df['강간(검거율)'] = state_df['강간(검거)'] / state_df['강간(발생)'] * 100
state_df['강도(검거율)'] = state_df['강도(검거)'] / state_df['강도(발생)'] * 100
state_df['절도(검거율)'] = state_df['절도(검거)'] / state_df['절도(발생)'] * 100
state_df['살인(검거율)'] = state_df['살인(검거)'] / state_df['살인(발생)'] * 100
state_df['폭력(검거율)'] = state_df['폭력(검거)'] / state_df['폭력(발생)'] * 100
state_df['검거율'] = state_df['소계(검거)'] / state_df['소계(발생)'] * 100
# print(state_df)

###### drop column
state_df.drop(['강간(검거)', '강도(검거)', '절도(검거)', '살인(검거)', '폭력(검거)', '소계(검거)', '소계(발생)'], inplace=True, axis=1)
# print(state_df)
state_df[state_df[['강간(검거율)', '강도(검거율)', '절도(검거율)', '살인(검거율)', '폭력(검거율)']] > 100] = 100  # Just to show the way to access columns simultaneously.
print(state_df)
print(state_df.loc[['강남구', '송파구'], '검거율'])
state_df.loc[['강남구', '송파구'], '검거율'] = 100
print(state_df.loc[['강남구', '송파구'], '검거율'])

