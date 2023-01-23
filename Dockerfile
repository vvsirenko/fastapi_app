FROM python:3.8
WORKDIR /usr/fastapi
LABEL version="1.0"
LABEL description="This is testing app"
ADD ./requirements.txt /usr/fastapi/requirements.txt
RUN pip install --no-cache-dir -r /usr/fastapi/requirements.txt
COPY ./app /usr/fastapi/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#EXPOSE 8000
#ENV PYTHONPATH "${PYTHONPATH}:/usr/app/app"
#CMD ["python", "./app/main.py"]
