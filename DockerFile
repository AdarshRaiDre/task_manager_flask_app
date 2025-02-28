FROM python: 3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no--cche--dir -r requirements.txt

COPY . .

EXPOSE 8004

cmd ["python", "app.py"]
