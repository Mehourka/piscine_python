FROM python:3.10

WORKDIR /setup

COPY requirements.txt ./
COPY script.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["python", "./script.py"]
