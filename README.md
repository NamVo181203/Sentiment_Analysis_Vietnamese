# Phân tích cảm xúc trong tiếng Việt - Sentiment Analysis Vietnamese
## Rresponsible Person: NVoz aka Võ Văn Nam

### Init venv
```python
python -m venv venv
```

### Activate venv to download dependencies
```python 
Window: .\venv\Scripts\activate
Linux: source venv/bin/activate
```

### Download data from drive - *tokenized_reviews.pt* and *vi_word2vec.pt*
[Data](https://drive.google.com/drive/folders/1sPZbs3MqreJA02J364LxkmkNBhEjWQ1q?usp=sharing)

[Model RNN](https://drive.google.com/drive/folders/1-KxZ3F_8OGifimZXUuQkeL7ZDSyUnvN5?usp=sharing)
### Install dependencies / libs
```python
pip install -r requirements.txt
```

### Run streamlit in cmd
```python
python -m streamlit run .\vsa_api\main.py
```
