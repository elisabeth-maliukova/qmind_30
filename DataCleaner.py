import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

file_path = "/Users/nadishagautam/Downloads/analyzed_trump.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(file_path, sheet_name=sheet_name)

def has_allowed_first_data_label(data_list):
    if (isinstance(data_list, list) and
        len(data_list) > 0 and
        isinstance(data_list[0], list) and  # Check if the first element is a list
        len(data_list[0]) > 0 and
        isinstance(data_list[0][0], dict) and  # Check if the first element of the first inner list is a dictionary
        "label" in data_list[0][0] and
        data_list[0][0]["label"] in allowed_labels):
        return True
    return False

def has_allowed_keywords(comment_text, keywords):
    return any(keyword in comment_text.lower() for keyword in keywords)

def is_toxic(comment_text):
    tokenizer = AutoTokenizer.from_pretrained("ZachBeesley/toxic-comments")
    model = AutoModelForSequenceClassification.from_pretrained("ZachBeesley/toxic-comments", from_tf=True)
    
    classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)
    result = classifier(comment_text)[0]
        
    return result['label'] == 'toxic'

allowed_keywords = ["here", "much", "trump", "investigate", "russia", "tax", "evasion", "fraud", "misuse", "charitable", "fund"]

allowed_labels = ['neutral', 'annoyance', 'disapproval', 'disappointment', 'anger', 'disgust']

filtered_data = df['data'].apply(lambda x: has_allowed_first_data_label(eval(x) if isinstance(x, str) else []))

filtered_data_keywords = df['comments'].apply(lambda x: has_allowed_keywords(x.lower() if pd.notna(x) else "", allowed_keywords))

toxicity_data = df['comments'].apply(lambda x: is_toxic(x) if pd.notna(x) else False)

df_filtered = df[filtered_data & ~toxicity_data & filtered_data_keywords & ~(df['comments'].astype(str).isin(['[removed]', '[deleted]']))]

output_file_path = "/Users/nadishagautam/Downloads/filtered_comments.xlsx"

df_filtered.to_excel(output_file_path, index=False)

