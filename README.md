
# GBP Owner Finder – AI Chrome Extension + NLP API

## 🔧 Backend API (Flask + spaCy)

### Setup Locally

```bash
cd server
pip install -r requirements.txt
python -m spacy download en_core_web_sm
flask run --host=0.0.0.0 --port=10000
```

### Deploy to Render

1. Push this folder to GitHub
2. Go to [Render](https://render.com)
3. Click "New Web Service" > Import GitHub Repo
4. It will auto-detect `render.yaml` and set up the backend for you

## 🔍 Chrome Extension (Plasmo + React)

Plasmo files will be generated separately – just run:

```bash
cd extension
npm install
plasmo dev
```

---

Built by Azlan Yasir. NLP model powered by spaCy.
