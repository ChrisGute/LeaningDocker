FROM python:3-alpine

WORKDIR /usr/src/hello_server

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python main.py