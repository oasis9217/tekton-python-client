# FastAPI implementation for Tekton API

## dev
```
cd tekton-python-client
python setup.py sdist bdist_wheel --dist-dir /tmp/dist

cd tekton-fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload
```
