import pandas as pd
import seaborn as sns

import scipy as sp
from scipy import stats

import warnings

pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
warnings.filterwarnings('ignore')

df = pd.read_csv('./data_analysis/data/cosmetics_.csv')
# print(df)

# cross table
cross_tbl = pd.crosstab(df.propensity, df.skin, margins=True, normalize=True)
cross_tbl.columns = ['건성', '민감성', '중성', '지성', '여드름성', '합계']
cross_tbl.index = ['저렴', '중간', '고가', '합계']
# print(cross_tbl)

chi_s = stats.chisquare(df.propensity, df.skin)  # chi-square test
print(chi_s)