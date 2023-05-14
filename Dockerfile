FROM python:3.11

COPY . .

EXPOSE 80

RUN pip install -r requirements.txt

CMD uvicorn main:app --port 80 --host 0.0.0.0