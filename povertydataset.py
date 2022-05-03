import pandas as pd

povertyrate = pd.read_csv('datasets/Poverty Rate.csv')
agdata = pd.read_csv('datasets/Agriculture Dataset.csv')

newpoverty = povertyrate.dropna()

#mergedDf = agdata.merge(newpoverty, on='Year')


#diff_cols = agdata.columns.difference(newpoverty.columns)
#df3 = agdata[diff_cols]

# merged = pd.concat([agdata, newpoverty], axis = 1, join = 'inner')
merged = pd.merge(povertyrate, agdata, how='inner', left_on=['Country','Year'], right_on=['Area','Year'])
merged = merged.drop(['Unnamed: 0_y', 'Area', 'Area Code'], 1)
#merged.drop([col for col in merged.columns if 'drop' in col], axis=1, inplace=True)
#merged = merged.drop('Country', 1)
# merged['New Year'] = merged['Year'] + merged['Year']
#merged.drop_duplicates()

#cols_to_use = newpoverty.columns.difference(agdata.columns)
merged.shape
#newdata = pd.merge(newpoverty, agdata)

merged.to_csv('/Users/ashfi/Documents/povertydataset.csv')