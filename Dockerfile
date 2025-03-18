FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY Streamlit .

CMD streamlit run home.py --server.port=$PORT