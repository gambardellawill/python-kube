FROM python:3.8-alpine

LABEL author="William Gambardella <williamcampo@gmail.com>"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]