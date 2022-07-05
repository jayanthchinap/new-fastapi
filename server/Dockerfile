# 
FROM python:3.10.5

# 
WORKDIR /app

# 
COPY ./sql_app/requirements.txt /requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
COPY . .

# 
## CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "80"]

