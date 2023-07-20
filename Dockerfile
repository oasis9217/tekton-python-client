FROM registry.access.redhat.com/ubi8/python-311:1-13

WORKDIR /opt
COPY . .

WORKDIR /opt/tekton-fastapi
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80

