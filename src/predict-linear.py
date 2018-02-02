import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
import settings
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# Read in the data
def read_data():
    df = pd.read_csv(os.path.join('..', settings.PROCESSED_DIR, "all_years_with_RT-and-PT.csv"))
    return df

def limit_time_period(df):
    df = df[df['CalendarYear'] >= settings.YEARS_OF_ANALYSES]
    return df

# Fits a linear model using features and 'Response Time (m)' ratings specified here (not set in the settings.py script)
# Prints the summary page to show coefficients, p-values, and R squared
def create_summary_linear(df):
    lr = LinearRegression()
    predictors = ['day_of_week_1', 'day_of_week_2','day_of_week_3', 'day_of_week_4', 'day_of_week_5', 'day_of_week_6', 'Problem_AUTO - Auto Fire', 'Problem_BBQ - Unsafe Cooking', 'Problem_BOX -Structure Fire', 'Problem_BOXL- Structure Fire',  'Problem_DUMP - Dumpster Fire', 'Problem_ELEC - Electrical Fire', 'Problem_GRASS - Small Grass Fire','Problem_TRASH - Trash Fire']
    lr.fit(df[predictors], df['Response Time (m)'])

    X = df[predictors]
    X2 = sm.add_constant(X)
    est = sm.OLS(df['Response Time (m)'], X2)
    est2 = est.fit()
    print(est2.summary())
    pass

# Fits a linear model using features and 'late_response' specified here (not set in the settings.py script)
# Prints the summary page to show coefficients, p-values, and R squared
def create_summary_logistic(df):
    # import chisqprob to prevent error as noted in https://github.com/statsmodels/statsmodels/issues/3931
    from scipy import stats
    stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)
    lr = LogisticRegression()
    # omits to put 'day_of_week_0' or 'Problem_BRSHL - Brush Alarm / Light' in the model as these will be the constants
    predictors = ['day_of_week_1', 'day_of_week_2','day_of_week_3', 'day_of_week_4', 'day_of_week_5', 'day_of_week_6', 'Problem_AUTO - Auto Fire', 'Problem_BBQ - Unsafe Cooking', 'Problem_BOX -Structure Fire', 'Problem_BOXL- Structure Fire',  'Problem_DUMP - Dumpster Fire', 'Problem_ELEC - Electrical Fire', 'Problem_GRASS - Small Grass Fire','Problem_TRASH - Trash Fire']
    lr.fit(df[predictors], df['late_response'])

    X = df[predictors]
    X2 = sm.add_constant(X)
    est = sm.Logit(df['late_response'], X2)
    est2 = est.fit()
    print(est2.summary())


if __name__ == "__main__":
    df = read_data()
    create_summary_linear(df)
    create_summary_logistic(df)
