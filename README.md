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
    - `twitter-roberta-base-sentiment`  
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
2. **Install dependencies**
    pip install -r requirements.txt
3. **Prepare the data**
    You can either download both datasets and use the clean scripts to generate cleaned datasets
    or just download the cleaned pre_ai dataset here: https://drive.google.com/file/d/1N8RGOshx9SEwvd27XnCiPgkDw23Y2_gw/view?usp=sharing 
4. **Run sentiment models**
    

1) https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NHLEJL
2) https://github.com/Guillaumeserres31/Twitter-Sentiment-Analysis-on-Generative-AI-Adoption/blob/main/Dataset/GenerativeAI%20tweets.csv