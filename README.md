# Phân tích cảm xúc trong tiếng Việt - Sentiment Analysis Vietnamese
## Responsible Person: NVoz aka Võ Văn Nam

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
Data Train: [Data](https://drive.google.com/drive/folders/1sPZbs3MqreJA02J364LxkmkNBhEjWQ1q?usp=sharing)

Trained Model: [Model RNN](https://drive.google.com/drive/folders/1-KxZ3F_8OGifimZXUuQkeL7ZDSyUnvN5?usp=sharing)

Website: [Website Of Team](https://sentiment-analysis-vietnamese.streamlit.app)
### Install dependencies / libs
```python
pip install -r requirements.txt
```

### Run in terminal
- Chạy API
```pthon
uvicorn services:app --reload
```
- Chạy UI
```python
python -m streamlit run .\main.py
```
