import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

"""marketing cost & user acquisition"""

marketing_cost = [352, 164, 210, 425, 503, 232, 321, 556, 464, 578, 612, 434]  # marketing costs (* 10,000 won)
user_acquired = [7214, 6122, 6896, 8020, 10982, 9021, 9240, 10210, 9987, 11521, 9792, 9852]  # persons

ad_df = pd.DataFrame({'Marketing_costs': marketing_cost, 'User_acquired': user_acquired})

# print(ad_df)

# calculate simple CAC(Customer acquisition cost, marketing term)
cac = ad_df['Marketing_costs'].sum() / ad_df['User_acquired'].sum()  # won
# print(np.round(cac * 10000).astype(np.int))

cor = ad_df.corr()
# print(cor)

cor_n_pv = stats.pearsonr(ad_df['Marketing_costs'], ad_df['User_acquired'])  # pearson correlation coefficient, p value
# print(cor_n_pv)  # p-value : 0.0016 => 0.16% => Null hypo rejected
# Null hypo : no correlation
# ALternative hypo : there is a correlation between marketing costs and user acquisition.

# check scatters plot
# print(ad_df.corr())
# sns.pairplot(ad_df, kind='reg')
# plt.show()

"""ab test for duration time"""
# testing which is more efficient between case A, and case B -> marketing term ( in this case the data will be the duration time)

web_a = pd.DataFrame([20.5, 12.6, 19.5, 18.8, 13.4, 13.5, 17.5, np.nan, 12.8, 17.8, np.nan, 23.1, 10.6, np.nan, 11.5],
                     columns=['Duration_A'])
web_b = pd.DataFrame([11.8, 10.7, np.nan, 12.5, np.nan, 14.9, 12.1, 13.9, 10.3, 9.0, 13.3, 12.4, 12.5],
                     columns=['Duration_B'])

df = pd.concat([web_a, web_b], axis=1)
# print(df)

# print(web_a.mean())
# print(web_b.mean())

# fill missing datas
# df['Duration_B'].fillna(df['Duration_B'].mean(), inplace=True)
# df['Duration_A'] = df['Duration_A'].fillna(df['Duration_A'].mean())
# print(df)

# drop missing datas
# df.dropna(inplace=True)
# print(df)
web_b.dropna(inplace=True)
web_a.dropna(inplace=True)

# ttest
ttest = stats.ttest_ind(web_a['Duration_A'], web_b['Duration_B'], equal_var=False)  # if there are missing datas, it will not work properly.
# equal_var=True : If two group has equal variance, and same size.
# equal_var=False : If two group has not equal variance, or different size.

# print(ttest)  # 0.008 -> 0.8%

# print(df['Duration_A'].var())
# print(df['Duration_B'].var())
# Null hypo : no differences in averages
# Alternative hypo : there is a significant difference in averages
# reject Null hypo
# case A is better than B

"""ab test for click-through rate and conversion rate"""
# marketing term

a_clicked = 144 # 버튼(배너) 시안 A를 누른 유저의 수
a_unclicked = 2362 # 버튼(배너) 시안 A를 보았으나 누르지 않은 유저의 수

b_clicked = 212 # 버튼(배너) 시안 B를 누른 유저의 수
b_unclicked = 2528 # 버튼(배너) 시안 B를 보았으나 누르지 않은 유저의 수

click_df = pd.DataFrame({'Clicked':[a_clicked, b_clicked],
                         'Unclicked':[a_unclicked, b_unclicked]}, index=['Button_A', 'Button_B'])  # contingency table
# print(click_df)

conversion_rate = click_df['Clicked'] / (click_df['Clicked'] + click_df['Unclicked']) * 100  # percent
# A_con = conversion_rate['Button_A']
# B_con = conversion_rate['Button_B']
# print(A_con, B_con)

chi_p = stats.chi2_contingency([click_df['Clicked'], click_df['Unclicked']])[1]
print(chi_p)  # 0.0049 -> 0.49%
# reject Null hypo

