"""
Analyze sentiment of tweets using the bhadresh-savani/distilbert-base-uncased-emotion model. https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion?text=I+feel+a+bit+let+down
Output of model:
[[
{'label': 'sadness', 'score': 0.0006792712374590337}, 
{'label': 'joy', 'score': 0.9959300756454468}, 
{'label': 'love', 'score': 0.0009452480007894337}, 
{'label': 'anger', 'score': 0.0018055217806249857}, 
{'label': 'fear', 'score': 0.00041110432357527316}, 
{'label': 'surprise', 'score': 0.0002288572577526793}
]]
"""
from transformers import pipeline
import pandas as pd
import sys

def get_sentiment(classifier ,text):
    prediction = classifier(text)
    return prediction[0]

def process_datset(filename):
    classifier = pipeline(
        "text-classification",
        model='bhadresh-savani/distilbert-base-uncased-emotion',
        return_all_scores=True)
    
    feeling_map = {
        "sadness": [],
        "joy": [],
        "love": [],
        "anger": [],
        "fear":  [],
        "surprise": []
    }
    df = pd.read_csv(filename)
    length = len(df)
    
    for index, row in df.iterrows():
        text = row['Text']
        sentiments = get_sentiment(classifier, text)
        for sent in sentiments:
            feeling_map[sent['label']].append(sent['score'])
        print(f"{index} out of {length} complete")
    
    return feeling_map
        
        
if __name__ == '__main__':
    # Represents the cleaned dataset file 
    # Example run: 
    filename = sys.argv[1]    
    
    sentiments = process_datset(filename)
    
    with open(f"{filename}-distilbert-output.txt", "w") as file:
        for feeling, values in sentiments.items():
            avg_score = sum(values) / len(values) if values else 0
            file.write(f"{feeling}: {avg_score:.2f}\n")
            print(f"{feeling}: {avg_score:.2f}\n")
            
        
    