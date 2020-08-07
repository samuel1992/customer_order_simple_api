A simple api for customers and orders.

# Requirements
- python 3.8
- pip
- postgres

# Running it locally
- `pip install -r requirements`
- `python create_db.py`
- `python run.py`

# Running it on docker
### You must have docker and docker-compose installed
- `docker-compose build`
- `docker-compose up`

# Running tests on docker
- `docker-compode run web ./test_and_coverage.sh`
 A faster way is to execute the running container. Ex: `docker exec -it menu_chlg_web_1 ./test_and_coverage.sh`
 Use the command `docker ps` to find your container name.

# Running test locally
- `./test_and_coverage`

