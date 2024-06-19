FROM gorialis/discord.py:alpine-minimal

WORKDIR /baby-name-bot

COPY requirements.txt .

COPY first.json .

COPY middle.json .

COPY last.json .

COPY .env .

COPY responses.py .

COPY main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]