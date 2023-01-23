FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#EXPOSE 8000
#ENV PYTHONPATH "${PYTHONPATH}:/usr/app/app"
#CMD ["python", "./app/main.py"]
