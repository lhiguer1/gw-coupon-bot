FROM python:3.9.6
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "bot.py" ]
