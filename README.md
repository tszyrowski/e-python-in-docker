Setap for python develpement inside constainers
===============================================

# Usage
Build docker image:
```
docker build -t fastapi-image .
```
Run:
```
docker run --name fastapi-container -p 80:80 fastapi-image
```
Or in detached mode
```
docker run --name fastapi-container -p 80:80 -d fastapi-image
```
To stop it:
```
docker stop fastapi-container
```
**To develope with the same code on local to be seen at the container:**
Run with volume mounted:
```
docker run --name fastapi-container -p 80:80 -d -v `pwd`:/code fastapi-image
```
> Note the backtick to evaluate the pwd. The `$()` can also be used instead of backticks. There may be a problem when evaluating with usual expansion as the `${pwd}` variable is being evaluated by the shell before the command is passed to `docker`. So, the command that is actually being executed by Docker is `docker run -v :/code ...`
The code bellow may not work:
```
docker run --name fastapi-container -p 80:80 -d -v ${pwd}:/code fastapi-image
```
Although above mounts all correctly, the local dev vscode doesn't have access to installed modules, hence for example autocompletion will not work.

The solution to this is to run **`dev container`** vscode extension and attach to running container.

## Running with docker compose

The single file can stand-up all services. Note the version entry on top of the file. Without it the `docker-compose up` can give errors.

After adding **`docker-compose.yml`** all services can e added with single command:
`docker-compose up`.</br>
To stop the services run: `docker-compose down`