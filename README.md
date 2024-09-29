# nsmcourse-backend

Backend of the natural systems modeling course site.

## Installation
First add actual database credentials to .env file. 
For example: 
```bash
POSTGRES_HOST=main_db
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_URL=postgresql://postgres:postgres@main_db/postgres
```
Then make [virtual environment](https://docs.python.org/3/library/venv.html)
```bash
python -m venv venv
```
and activate it.
```bash
venv\Scripts\activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install -r requirements.txt
```

To start a server run
```bash
uvicorn src.main:app --reload
```
