import numpy as np
import pandas as pd
import statsmodels.api as sm


loansData = pd.read_csv('loansData_clean.csv')

loansData['Interest.Rate.lt.12'] = loansData['Interest.Rate'].map(lambda x: True if x <= 12 else False)
loansData['Intercept'] = loansData['Interest.Rate'].map(lambda x: '1.0')
loansData['Intercept'] = loansData['Intercept'].astype(float)


intercept = loansData['Intercept']
ilt12 = loansData['Interest.Rate.lt.12']
loanamt = loansData['Amount.Funded.By.Investors']
fico = loansData['FICO.Score']


X = sm.add_constant(intercept)

cols = ['FICO.Score', 'Amount.Funded.By.Investors']# , 'Intercept']

ind_vars = loansData[cols]
ind_vars = sm.add_constant(ind_vars)

#logit = sm.Logit(X, ind_vars)
logit = sm.Logit(loansData['Interest.Rate.lt.12'], ind_vars)
result = logit.fit()
coeff = result.params 
print coeff
