# Classifying Public Sentiment Toward AI Before and After the Launch of Generative AI  

## Group  
**BME – Ben Szeto (Leader), Eddie Zhang, Masato Takedai**  
DS 4002 – 001 – 1pm – September 2025  

---

## Contents of Repository  
- **README.md** – Orientation and instructions for reproducing results  
- **LICENSE.md** – MIT License for reuse of this repository  
- **SCRIPTS/** – Source code for preprocessing and sentiment analysis  
- **DATA/** – Raw and cleaned datasets, plus Data Appendix PDF  
- **OUTPUT/** – Figures, tables, and other analysis results  

---

## Software and Platform  
- **Programming Language:** Python 3.10+  
- **Core Libraries:**  
  - `pandas` – data manipulation  
  - `numpy` – numerical processing  
  - `matplotlib`, `seaborn` – visualizations  
  - `vaderSentiment` – lexicon-based sentiment analysis  
  - `transformers` (Hugging Face) – pretrained transformer models  
    - `bert-base-multilingual-uncased-sentiment` 
    - `distilbert-base-uncased-emotion`  
- **Platform:** Code developed and tested on Windows and MacOS  

---

## Project Folder Map  

TODO

---

## Instructions for Reproducing Results  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/SzetoBen/BME-Text-Project
   cd BME-AI-Sentiment-Project
2. **Install dependencies**\
    pip install -r requirements.txt
3. **Prepare the data**\
    You can either download both datasets and use the clean scripts to generate cleaned datasets
    or just download the cleaned pre_ai dataset here: https://drive.google.com/file/d/1N8RGOshx9SEwvd27XnCiPgkDw23Y2_gw/view?usp=sharing 
4. **Run sentiment models**
    1) **Running distilbert model**
        1. Navigate to scripts directory ```cd scripts```
        2. Run ```python ./distilbert_sentiment.py ..\data\cleaned_pre_ai.csv```
        3. Run ```python ./distilbert_sentiment.py ..\data\cleaned_post_ai.csv```
        4. This will output two .txt files containing the average sentiment of the corresponding dataset
        5. Run ```python ./scripts/plot_distilbert.py``` in the project root directory 
        6. Two plots will be generated in the ```output/plots``` directory showing the average sentiment for each dataset
    2. **Running VADER model**
        1. Open the notebook directly in Colab (this opens the same notebook in the browser and lets you run it in Colab's environment):
        https://colab.research.google.com/github/SzetoBen/BME-Text-Project/blob/main/scripts/VADERSentimentAnalysis.ipynb
        2. In Colab, upload data from the repo and ensure naming for files are correct
        3. Run through the entire script with Colab
    3. **Running bert model**
        1. Navigate to scripts directory. ```cd scripts```
        2. Run ```https://github.com/SzetoBen/BME-Text-Project/blob/main/scripts/bert_base_multilingual_uncased_sentiment_both_models.ipynb```
        3. The outputs of the notebook can be matched with the data found in the output folder ```cd outputs```
    
1) https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NHLEJL
2) https://github.com/Guillaumeserres31/Twitter-Sentiment-Analysis-on-Generative-AI-Adoption/blob/main/Dataset/GenerativeAI%20tweets.csv
