#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Necessary dependencies:
# Pandas, Numpy, Spacy
# Spacy en_core_web_lg
# python -m spacy download en_core_web_lg

import pandas as pd 
import numpy
import spacy
import csv

nlp = spacy.load('en_core_web_lg')

emissions = pd.read_csv('shared_data_read_only/Agriculture Dataset.csv')
products = pd.read_csv('shared_data_read_only/Crop Production.csv')

products = products.drop_duplicates(subset='Item')
productset = products.iloc[:,3].to_numpy()

emissions2 = emissions.columns
emission3 = emissions2.to_numpy(dtype=str)

print ( emissions )


correlate = dict() 

lilticker = 0
for i in range( len(productset) ):
    
    max = 0;
    correlate[ productset[i] ] = ""

    for j in range ( len(emission3) ):

        if  ( ( emission3[j] != 0 ) or ( emission3[j] != None ) or ( emission3[j] != 'NaN' ) ):

            product = nlp( productset[i] )
            emission_str = numpy.array2string(emission3[j])
            
            print(emission_str)
            print( type(emission_str).__name__ )
            
            emission = nlp( emission_str )
            
            n = product.similarity(emission) 
        
            if ( n > max  ):
                max = n 
                correlate[ productset[i] ] = emission_str
#   print(lilticker)
    lilticker+=1
    
print( correlate )


# In[ ]:





# In[ ]:




