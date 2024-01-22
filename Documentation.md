# Documentation
*Author Willy Matthew Xamountry wixait01*

This Document will briefly describe what i did in this Lab. It will
describe its' functions and where i had difficulties.

## Architecture

- The Project is simply the Task List implemented. 
- I used a PostgreSQL Database from the Docker Hub and Containerized it's execution. Any API with the Database is on the Port 5432.
- For Backend i used a Flask Server which handles any routing to the Database. To establish the connection to the Database was fairly easy, i just provided the User Information and the Port. Any Routing to the Backend is handled RESTful and as a Ressource. The Backend Port for the API with it is 5000.
- The Frontend is implemented in React. I made a simple single Page Web application which onload calls the /tasks API with method GET to get a JSON of the current Tasks in the database. One can also call the /tasks API with Method POST and a JSON to update the database with a new task.
To delete or mark a Task as completed the Web app calls the API /tasks/$id whereas $id is the id of the task. Depending on the method (GET,POST, DELETE) the task is searched, updated or deleted respectively.

## Difficulties

As the connection between Database and Backend was fairly simple and also how to add, delete or update Data, i couldn't really get the connection between backend and frontend to work on Docker Container level. So i made the Port of the backend public and just addressed the API with the Public Address.

I tried multiple ways to setup the proxy for the frontend. By either creating a new Docker Network, editing existing ones, trying to link them in the Docker Compose.yaml setting up new Ports and editing Enviromental Variables but nothing really seemed to work.

## Additional Functionality

I've tried to implement the openTelemetry in the backend Python code. Also the Data is actually persistent on the database so that when the docker container is shut down all the data still persists.

## Endpoints

The Ports of the Containers are each defined in their **Dockerfile** and in the **docker-compose.yaml**. User Credentials for the DB are defined in the **app.py** in the flaskbackend folder. API Endpoints from frontend to backend are in the **App.js** in the reactfrontend folder.

## Known Issues

By Storing User Data in the Source Code it's not very secure. Same with the Hardcoded Endpoints from frontend to backend. Should at some point this gitpod execution change from my User credentials to someone elses you would need to change those hard coded endpoints too. That's why a proxy setting would have been favorable as you can then specify the Endpoints relative to the host.

## Further Improvements

OpenTelemetry for the frontend Javascript code, but as it's only a Website one can just inspect the payload and console logs, etc. on the Developer tools of a Browser. Trying to a get the connection on the Docker Container Level to work between frontend and backend.
