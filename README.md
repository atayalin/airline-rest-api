# rest-airline-api

A simple REST API that handles airlines and aircrafts. The project is presented to me as a case study.

## Installation without Docker.

1. Clone the project from this repo.

```bash
git clone <project_url>
```

2. Create an environment (Optional).

```bash
python -m venv env
source env/bin/activate # Linux/Mac
env\Scripts\activate # Windows
```

3. Install requirements.

```bash
pip install -r requirements.txt
```

4. Run run.sh file. (or the lines inside of it, respectively.)

```bash
./run.sh
```

## Installation with Docker

1. Clone repo.

```bash
git clone <project_url>
```

2. Build and run images.

```bash
docker-compose up --build
```
