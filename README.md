# capstone-project

Required tools to run this project:
- Docker 20.10.7
- Docker-compose 1.29.2

To build:
- sudo docker-compose build 

To run:
- sudo docker-compose up (must be done twice on first run)

The flask config:
- Listening on port 5000
- Currently in debug mode (auto reload on file modification)
- Static_url_path is set to src/static which means anything in that folder is directly accessible through http request
