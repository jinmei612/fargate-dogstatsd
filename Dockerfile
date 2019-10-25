FROM ubuntu:18.04
COPY . /app
RUN apt-get update -y
RUN apt-get install python -y
RUN apt install python-pip -y
RUN pip install datadog
EXPOSE 8125
entrypoint ["python", "/app/dogstatsd.py"]
