FROM python:latest

COPY ./ /

WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]