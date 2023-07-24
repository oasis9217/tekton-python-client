# https://github.com/sclorg/s2i-python-container/blob/master/3.11/README.md
FROM registry.access.redhat.com/ubi8/python-311:1-13

# Prep. The home dir of user 1001 is /opt/app-root/src
USER 0
COPY . .
RUN chown -R 1001:0 ./
USER 1001

# Build tekton-python-client wheel to /tmp/dist where tekton-fastapi would look at. TODO: deploy online
WORKDIR /opt/app-root/src/tekton-python-client
RUN pip install wheel
RUN python setup.py sdist bdist_wheel --dist-dir /tmp/dist

# Install dependencies
WORKDIR /opt/app-root/src/tekton-fastapi
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80

