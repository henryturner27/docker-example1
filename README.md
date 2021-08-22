## Requirements
- Docker

## To Run
1. Clone this repo
1. Navigate to this project in your terminal
1. Make sure Docker has been started and is running
1. Build the image: `docker build -t flask_app .`
1. Run the container: `docker run -p 8000:8000 -it flask_app`