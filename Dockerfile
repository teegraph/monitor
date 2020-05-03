FROM python:3.7.7 as builder

RUN mkdir /paytaxi
WORKDIR /paytaxi
COPY req.txt /paytaxi/
RUN pip install -r req.txt

FROM python:3.7.7-slim
RUN apt-get update && apt-get install -y --no-install-recommends libmariadb3 && rm -rf /var/lib/apt/lists/*
RUN mkdir /paytaxi
WORKDIR /paytaxi
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/
COPY . /paytaxi/
ENV FLASK_APP=monitor.py
ENTRYPOINT flask run --port 8080
