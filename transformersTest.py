import pandas as pd
from transformers import pipeline

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

comments = pd.read_excel('rawComments_trudeau.xlsx', index_col=0)  
analyzedData = []
for index in comments.index:
    comment = comments['Comments'][index]
    analysis = classifier(comment, truncation=True)
    analyzedData.append([comment, analysis])

df = pd.DataFrame(analyzedData)
df.to_excel('analyzed_trudeau.xlsx')

'''
for i in range(len(df.index)):
    if (df.loc[i,1][0][0].get('label') == "anger"):
        print(df.loc[i, 0])
'''