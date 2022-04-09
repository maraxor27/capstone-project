# capstone-project

## Required tools to run this project:
- Docker 20.10.7
- Docker-compose 1.29.2

## Installation processe of the github repository

>git clone --recurse-submodules https://github.com/maraxor27/capstone-project.git
>cd capstone-project

## How to run our docker containers
Those specific command work on linux. MacOS and Windows users have ever so slightly different commands that are equivalent

To build:
- sudo docker-compose build 

To run:
- sudo docker-compose up (must be done twice on first run wait until capstone-project-postgres-1 displays server started)

The flask config:
- Listening on port 5000
- Currently in debug mode (auto reload on file modification)
- Static_url_path is set to src/static which means anything in that folder is directly accessible through http request
