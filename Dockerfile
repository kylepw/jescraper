FROM python:3.7-alpine

ENV WORD missing

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY jes.py .

CMD python ./jes.py "$WORD"