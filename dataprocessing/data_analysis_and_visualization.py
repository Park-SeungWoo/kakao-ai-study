import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
state_df[state_df[['강간(검거율)', '강도(검거율)', '절도(검거율)', '살인(검거율)',
                   '폭력(검거율)']] > 100] = 100  # Just to show the way to access columns simultaneously. (masking technique)

# for row_idx, row in state_df.iterrows():
#     print(row_idx, row, sep="\n")

# print(state_df[state_df['살인(발생)'] > 7])
# print(state_df[state_df[["살인(발생)"]] > 7])
# state_df[state_df['살인(발생)'] > 7] = 0

# state_df.drop(list(state_df[state_df['살인(발생)'] > 7].index), inplace=True)  # drop

# print(state_df)
# state_df[state_df[['살인(발생)']] > 7] = 0
# print(state_df)

# print(state_df[(state_df['살인(발생)'] > 7) & (state_df['폭력(발생)'] > 2000)])
# print(state_df[(state_df['살인(발생)'] > 7) | (state_df['폭력(발생)'] > 2000)])
# print(state_df[~(state_df['살인(발생)'] < 5)])
# print(state_df[~(state_df['살인(발생)'] > 5)])

# print(list(state_df[state_df['살인(발생)'] == 0].index))
state_df['살인(검거율)'].fillna(100, inplace=True)
# print(state_df.loc[['도봉구']])

state_df.rename(columns={
    '강간(발생)': '강간',
    '강도(발생)': '강도',
    '살인(발생)': '살인',
    '절도(발생)': '절도',
    '폭력(발생)': '폭력'}, inplace=True)
# print(state_df)

########## merge with population data

# a.join(b) - it will work well even if unsorted, But a, b dataframes' index column should be same.
# pd.merge(a, b, left_on='', right_on='', how='inner') - should set detailed props, work well with unsorted dataframe, doesn't matter when if two dataframes have not same index
# pd.concat([a, b], axis=0) - it doesn't follow the index columns, can be done by rows or columns. Often used when adding new rows.

popul_df = pd.read_csv('./lecture_datas/crime/pop_kor.csv', encoding='utf-8')
# popul_df = pd.read_csv('./lecture_datas/crime/pop_kor.csv', encoding='utf-8', index_col='구별')  # set_index too
popul_df.rename(columns={'구별': 'state'}, inplace=True)
popul_df.set_index('state', inplace=True)

tot_df = state_df.join(popul_df)
# print(tot_df)

tot_df.sort_values(by='검거율', ascending=False, inplace=True)

# print(tot_df)

##############font
# from matplotlib import font_manager as fm
#
# for f in fm.fontManager.ttflist:
#     if ('Nanum' in f.name) or ('Gothic' in f.name):
#         print(f)

# import matplotlib as mlp
# print(mlp.matplotlib_fname())
# print(mlp.get_cachedir())

####### use seaborn(heatmap)
plt.rc('font', family='Nanum GaRamYeonGgoc')  # font setting (Korean)
# sns.heatmap(tot_df[['강간', '강도', '살인', '절도', '폭력']])
# plt.show()

max_vals = tot_df[['강간', '강도', '살인', '절도', '폭력']].max()
# min_max_crime_count = tot_df[['강간', '강도', '살인', '절도', '폭력']] - min_vals / max_vals - min_vals  # it returns some negative values
# std_crime_count = tot_df[['강간', '강도', '살인', '절도', '폭력']] - mean_vals / std_vals
# print(min_max_crime_count)
# print(std_crime_count)
norm_df = tot_df[['강간', '강도', '살인', '절도', '폭력']] / max_vals  # temporary normalization
# print(norm_df)

# plt.figure(figsize=(10, 8))
# plt.subplot(1, 2, 1)
# sns.heatmap(norm_df.sort_values(by="살인", ascending=False), cmap="rocket_r", annot=True, fmt="f", linewidth=.5)
# plt.title('Crime Occurrences without population')

# plt.subplot(1, 2, 2)
# sns.heatmap(norm_df.sort_values(by="절도", ascending=False), cmap="rocket_r", annot=True, fmt="f", linewidth=.5)
# plt.title('Crime Occurrences sorted by Thieves')
# plt.show()

norm_df = norm_df.div(tot_df['인구수'], axis=0) * 100000
# print(norm_df.head(5))

# plt.subplot(1, 2, 2)
# sns.heatmap(norm_df.sort_values(by="살인", ascending=False), cmap="rocket_r", annot=True, fmt="f", linewidth=.5)
# plt.title('Crime Occurrences with population')
# plt.show()

norm_df['total'] = norm_df.mean(axis=1)
# print(norm_df)

# sns.heatmap(norm_df.sort_values(by="total", ascending=False), cmap="rocket_r", annot=True, fmt="f", linewidth=.5)
# plt.show()

##############folium

import json

geo_path = './lecture_datas/crime/skorea-2018-municipalities-geo.json'
# geo_path = './lecture_datas/crime/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, 'r', encoding='utf-8'))  # get geo datas

# print(geo_str)
# print(geo_str['features'][0])

import folium
import webbrowser


def show_geo(m):
    m.save('./dataprocessing/geo_html/geomap.html')
    webbrowser.open(url=f'file://{os.getcwd()}/dataprocessing/geo_html/geomap.html')


geo_map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

# geo_map.choropleth(geo_data=geo_str,
#                    data=tot_df['살인'],
#                    columns=[tot_df.index, tot_df['살인']],
#                    fill_color='PuRd',
#                    # key_on='feature.id'
#                    key_on='properties.name'
#                    )

# geo_map.choropleth(geo_data=geo_str,
#                    data=norm_df['total'],
#                    columns=[norm_df.index, norm_df['total']],
#                    fill_color='PuRd',
#                    key_on='properties.name')
# show_geo(geo_map)

GEOCODE_KEY = json.load(open('./keys.json', 'r', encoding='utf-8'))['GEOCODE']
# print(GEOCODE_KEY)
station_name = []
for name in df_new['관서명']:
    station_name.append(f'서울{name[:-1]}경찰서')

# print(station_name)
df_new['police'] = station_name
df_new['arrest rate'] = df_new['소계(검거)'] / df_new['소계(발생)'] * 100


# print(df_new)  # similar arrest rate

# print(df_new['arrest rate'])

def my_min_max(x, mini, maxi, min_range, max_range):
    return ((x - mini) * (max_range - min_range) / (maxi - mini)) + 1


df_new['score'] = my_min_max(df_new['arrest rate'], df_new['arrest rate'].min(), df_new['arrest rate'].max(), 1, 100)
# print(df_new.sort_values(by='score', ascending=False))

############################################ geocoding

# import googlemaps
#
# gmaps = googlemaps.Client(key=GEOCODE_KEY)
# # location_info = gmaps.geocode('서울중부경찰서', language='ko')
# # print(location_info[0]['geometry']['location'])
#
# lat = []
# long = []
#
# for station in df_new['police']:
#     tmploc = gmaps.geocode(station)
#     lat.append(tmploc[0]['geometry']['location']['lat'])
#     long.append(tmploc[0]['geometry']['location']['lng'])
#
# df_new['lat'] = lat
# df_new['long'] = long

# print(df_new)

df_geo = pd.read_excel('./lecture_datas/crime/관서별 5대범죄 발생 및 검거(with lat & lng).xlsx', engine='openpyxl')
# print(df_geo)

# geo_map.choropleth(geo_data=geo_str,
#                    data=norm_df['total'],
#                    columns=[norm_df.index, norm_df['total']],
#                    fill_color='PuRd',
#                    # key_on='feature.id'
#                    key_on='properties.name'
#                    )

############################################draw circle
# for i in df_geo.index:
#     folium.CircleMarker((df_geo['lat'][i], df_geo['lng'][i]),
#                         radius=df_geo['점수'][i] * 0.5,
#                         color="#3186cc",
#                         fill=True,
#                         fillcolor="#3186cc").add_to(geo_map)


# show_geo(geo_map)

#################################choropleth only seoul
# print(geo_str['features'][0]['properties'])
seoul_geo = []
for item in geo_str['features']:
    if item['properties']['code'][:2] == '11':
        seoul_geo.append(item)

# print(len(seoul_geo))
geo_str['features'] = seoul_geo

geo_map.choropleth(geo_data=geo_str,
                   data=tot_df['살인'],
                   columns=[tot_df.index, tot_df['살인']],
                   fill_color='PuRd',
                   # key_on='feature.id'
                   key_on='properties.name'
                   )

for i in df_geo.index:
    folium.CircleMarker((df_geo['lat'][i], df_geo['lng'][i]),
                        radius=df_geo['점수'][i] * 0.5,
                        color="#3186cc",
                        fill=True,
                        fillcolor="#3186cc").add_to(geo_map)

show_geo(geo_map)