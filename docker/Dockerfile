FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]