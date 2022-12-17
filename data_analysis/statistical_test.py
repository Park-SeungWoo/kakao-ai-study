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
df_anova = df.copy(deep=True)
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
# independant
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

# sns.distplot(male_satisf_all, kde=False, fit=stats.norm, hist_kws={'color': 'r', 'alpha': 0.2}, fit_kws={'color': 'r'})
# sns.distplot(female_satisf_all, kde=False, fit=stats.norm, hist_kws={'color': 'g', 'alpha': 0.2}, fit_kws={'color': 'g'})
# plt.show()

# Paired
# print(df_ttest[['satisf_b', 'satisf_i']].describe())

rel_ttest = stats.ttest_rel(df_ttest['satisf_b'], df_ttest['satisf_i'])
# Null hypo : don't have any correlation
# Alternative hypo : have correlation

# print(rel_ttest)

# sns.distplot(df_ttest['satisf_b'], kde=False, fit=stats.norm, hist_kws={'color': 'r', 'alpha': 0.2}, fit_kws={'color': 'r'})
# sns.distplot(df_ttest['satisf_i'], kde=False, fit=stats.norm, hist_kws={'color': 'g', 'alpha': 0.2}, fit_kws={'color': 'g'})
# plt.show()

""" ANalysis Of VAriance (ANOVA)"""
# anova f test
# print(df_anova)

social_satisf = df_anova[df_anova['decision'] == 1].satisf_al
mental_satisf = df_anova[df_anova['decision'] == 2].satisf_al
appear_satisf = df_anova[df_anova['decision'] == 3].satisf_al
# print(social_satisf.mean())
# print(mental_satisf.mean())
# print(appear_satisf.mean())

anova = stats.f_oneway(social_satisf, mental_satisf, appear_satisf)
# Null hypo : no correlations
# ALternative hypo : there are at least one correlation.
# print(anova)

# sns.distplot(social_satisf, kde=False, fit=stats.norm, hist_kws={'color': 'r', 'alpha': 0.2}, fit_kws={'color': 'r'})
# sns.distplot(mental_satisf, kde=False, fit=stats.norm, hist_kws={'color': 'g', 'alpha': 0.2}, fit_kws={'color': 'g'})
# sns.distplot(appear_satisf, kde=False, fit=stats.norm, hist_kws={'color': 'b', 'alpha': 0.2}, fit_kws={'color': 'b'})
# plt.show()

"""find correlation"""
df_cor = df_ttest[['decision', 'satisf_b', 'satisf_i', 'satisf_al', 'repurchase']]

# print(df_cor.head(5))

# pearson coefficient
# print(df_cor.corr())

# sns.pairplot(df_cor)
# plt.show()

"""additional"""

iris = sns.load_dataset('iris')
# print(iris.head())
cor = iris.corr()
print(cor)

sns.set(style="ticks", color_codes=True)
sns.pairplot(iris, kind='reg')
plt.show()