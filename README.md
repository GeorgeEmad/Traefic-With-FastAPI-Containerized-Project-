# FastAPI Dockerized with Traefik Reverse Proxy

This repository demonstrates how to dockerize a simple FastAPI application and leverage Traefik as a reverse proxy for secure and scalable API access. It follows the guidelines from the 
[Traefik tutorial](https://traefik.io/resources/traefik-fastapi-kuberrnetes-ai-ml/?utm_campaign=Influencer:%20Sebastian%20Ramirez,%20FastAPI%20&amp;utm_content=155438367&amp;utm_medium=social&amp;utm_source=twitter&amp;hss_channel=tw-4890312130 )
  

## Key Components
FastAPI Application: A minimal FastAPI application defines dummy APIs in the main.py only to showcase no logic actual in it.

Dockerfile: This file specifies the instructions for building a Docker image containing the application and its dependencies.

docker-compose.yml: This configuration file defines the backend service running the image build by the dockerfile and has labels  for dynamic traefic configurations.

docker-compose.traefik.yml: Contains the Traefik reverse proxy static and dynamic configurations.



**Note**: docker compose files and traefic routing rules host uses domains defined in a .env file which you should use
