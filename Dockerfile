FROM python:3.7.7 as builder

RUN mkdir /monitor
WORKDIR /monitor
COPY req.txt /monitor/
RUN python -m venv venv
RUN venv/bin/pip install -r req.txt
COPY . /monitor/

FROM python:3.7.7-slim
RUN apt-get update && apt-get install -y --no-install-recommends libmariadb3 && rm -rf /var/lib/apt/lists/*
RUN mkdir /monitor
WORKDIR /monitor
RUN python -m venv venv
COPY --from=builder /monitor/venv/bin /monitor/venv/bin
COPY --from=builder /monitor/venv/lib/python3.7/site-packages /monitor/venv/lib/python3.7/site-packages
COPY . /monitor/
RUN chmod +x boot.sh
ENV FLASK_APP monitor.py
ENTRYPOINT ["./boot.sh"]
