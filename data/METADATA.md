# Classifying Public Sentiment Toward Artificial Intelligence on Twitter Before and After the Public Launch of GenAI  

**Group:** BME - Ben Szeto (Leader), Eddie Zhang, Masato Takedai  
**Course:** DS 4002 – 001 – 1pm  
**Date:** 9/19/25  

---

## Hypothesis and Goal Statement  

Apply pretrained sentiment analysis models to classify Twitter posts about AI as positive or negative and compare sentiment before (2017–2021) and after (2022–present) the launch of generative AI.  

**Hypothesis:** Public sentiment toward AI has increased since the launch of generative AI.  

---

## Executive Summary  

We want to focus on sentiment shifts in AI discourse after generative AI tools like ChatGPT were released to the public. To do this, we will use pretrained sentiment models on two datasets of AI-related tweets — one before generative AI and one after.  

---

## Dataset Establishment  

- **Pre-GenAI Dataset (2017–2021):**  
  - Collected via Twitter API, 36 raw variables, with 19 non-sensitive variables retained.  
  - From a study conducted by Daniel Kolouski (Springer Nature, Feb 2025).  
  - Available on Harvard Dataverse.  

- **Post-GenAI Dataset (2022–2023):**  
  - Focused on tweets with hashtag **#GenerativeAI**.  
  - Collected via Twitter API.  
  - Published on GitHub by *Guillaumeserres31* (2025).  

**Licenses:**  
- Pre-GenAI dataset: **CC BY-NC 4.0** (free to use, modify, distribute).  
- Post-GenAI dataset: no license → **fair use claimed** for educational purposes.  

---

## Data Dictionary  

### Pre-GenAI Dataset  
| Column           | Description                          | Example(s) |
|------------------|--------------------------------------|------------|
| id               | Tweet ID                             | 958708077116739584 |
| conversation_id  | Conversation ID                      | 958707754025168896 |
| created_at       | Date and time of tweet               | 2018-01-31 09:27:27 EST |
| date             | Date                                 | 9/27/19 |
| time             | Time                                 | 21:17:37 |
| timezone         | Timezone                             | -400 |
| tweet            | Text of the tweet                    | “RT BourseetTrading: 🏆Top 10 hot #ArtificialIntelligence …” |
| language         | Tweet language                       | en, es |
| urls             | Links in tweet                       | [http://news.google.com/…] |
| photos           | Attached photos                      | [https://pbs.twimg.com/media/C3cirGtWIAAAClh.jpg] |
| replies_count    | Number of replies                    | 0, 1 |
| retweets_count   | Number of retweets                   | 0, 1 |
| likes_count      | Number of likes                      | 0, 1 |
| hashtags         | Hashtags used                        | ['artificialintelligence', 'ai'] |
| cashtags         | Cashtags used                        | [] |
| retweet          | Retweet indicator                    | FALSE |
| quote_url        | Quote tweet URL                      | NA |
| video            | Video indicator                      | 0, 1 |
| thumbnail        | Thumbnail link                       | NA, [https://pbs.twimg.com/media/C3cisLJXUAAJtgw.jpg] |

### Post-GenAI Dataset  
| Column    | Description                  | Example(s) |
|-----------|------------------------------|------------|
| Datetime  | Time tweet was sent          | 2023-04-19 21:27:19+00:00 |
| Tweet ID  | Tweet ID                     | 1648800467206672384 |
| Text      | Tweet body (with hashtags)   | “From Studio Gangster to Synthetic Gangster 🎤…” |
| Username  | Twitter username             | Resembleai, VirtReview |

---

## Ethical Considerations  

- Usernames removed in pre-GenAI dataset, but present in post-GenAI dataset.  
- Tweets are publicly available via Twitter API.  

---

## Data Exploration  

- **Pre-GenAI dataset:** steady tweet distribution across timeframe.  
- **Post-GenAI dataset:** spike in tweets post-ChatGPT release.  

We mitigated by excluding pre-release tweets from the post-GenAI dataset.  

---

## Exploratory Plots  

- **Figure 1:** Count of Tweets over time (pre-ChatGPT).  
- **Figure 2:** Count of Tweets over time (post-ChatGPT).  

---

## Analysis Plan  

### Goal  
Determine whether public sentiment toward AI has shifted before vs. after ChatGPT.  
- A **≥5% difference** in positive sentiment between datasets indicates a shift.  

### Preprocessing  
- Keep only **tweet/Text** columns.  
- Remove empty rows, duplicates, and URLs.  
- Remove pre-ChatGPT rows from post-dataset.  

### Sentiment Analysis Models  
- **VADER**: Social media sentiment analysis.  
- **Twitter-roberta-base-sentiment**: Fine-tuned on tweets.  
- **Bert-base-multilingual-uncased-sentiment**: Multilingual product reviews.  
- **Distilbert-base-uncased-emotion**: Emotion detection.  

Using multiple models allows comparison and validation.  

### Evaluation  
- Sentiment classification:  
  - Positive: [0.6, 1]  
  - Negative: [0, 0.4]  
  - Neutral: (0.4, 0.6)  

- Success criteria: At least **two models agree** on direction of sentiment change.  

---

## References  

1. W. Intayoad, *Tweets-AI*, GitHub, 2025. [https://github.com/warint/tweets-ai](https://github.com/warint/tweets-ai)  
2. G. Serres, *Twitter Sentiment Analysis on Generative AI Adoption*, GitHub, 2025. [https://github.com/Guillaumeserres31/Twitter-Sentiment-Analysis-on-Generative-AI-Adoption](https://github.com/Guillaumeserres31/Twitter-Sentiment-Analysis-on-Generative-AI-Adoption)  
3. C.J. Hutto, *vaderSentiment*, GitHub, 2025. [https://github.com/cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment)  
4. F. Pascual, “Getting Started with Sentiment Analysis using Python,” Hugging Face, 2022. [https://huggingface.co/blog/sentiment-analysis-python](https://huggingface.co/blog/sentiment-analysis-python)  