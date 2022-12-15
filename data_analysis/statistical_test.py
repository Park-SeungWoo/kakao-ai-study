import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

import scipy as sp
from scipy import stats

import warnings

pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
warnings.filterwarnings('ignore')
plt.rc('font', family='Nanum GaRamYeonGgoc')  # set fon

df = pd.read_csv('./data_analysis/data/cosmetics_.csv')
df_ttest = df.copy(deep=True)
# print(df)

# cross table
cross_tbl = pd.crosstab(df.propensity, df.skin, margins=True, normalize=True)
# cross_tbl = pd.crosstab(df.propensity, df.skin)
cross_tbl.columns = ['건성', '민감성', '중성', '지성', '여드름성', '합계']
cross_tbl.index = ['저렴', '중간', '고가', '합계']

chi_s = stats.chisquare(df.propensity, df.skin)  # chi-square test
# print(chi_s)

df['propensity'] = df['propensity'].replace([1, 2, 3], ['low', 'middle', 'high'])
df['skin'] = df['skin'].replace([1, 2, 3, 4, 5], ['dry', 'sensitive', 'neutral', 'oily', 'complex'])
ct = pd.crosstab(df.propensity, df.skin)
# print(ct)

# ct.plot.bar(stacked=True)
# ct.plot.bar()
# plt.show()


"""t-test"""
male_satisf_all = df_ttest[df_ttest['gender'] == 1].satisf_al.values
male_s_al_mean = df_ttest[df_ttest['gender'] == 1].satisf_al.mean()
female_satisf_all = df_ttest[df_ttest['gender'] == 2].satisf_al.values
female_s_al_mean = df_ttest[df_ttest['gender'] == 2].satisf_al.mean()
# print(male_satisf_all)
# print(female_satisf_all)
# print(male_s_al_mean)
# print(female_s_al_mean)

ind_ttest = stats.ttest_ind(male_satisf_all, female_satisf_all)
# print(ind_ttest)  # p value 0.6213, Null hypothesis adopted

# df_ttest.boxplot(column='satisf_al', by='gender')
# plt.show()

sns.distplot(male_satisf_all, kde=False, fit=stats.norm, hist_kws={'color': 'r', 'alpha': 0.2}, fit_kws={'color': 'r'})
sns.distplot(female_satisf_all, kde=False, fit=stats.norm, hist_kws={'color': 'g', 'alpha': 0.2}, fit_kws={'color': 'g'})
plt.show()