FROM python:3.8
WORKDIR /usr/src/app
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "./src/main.py"]
