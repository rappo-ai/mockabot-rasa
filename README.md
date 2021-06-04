# mockabot-rasa
Rasa version of Mockabot

# Build steps

## Environment Variables

Set the Telegram bot token and Telegram bot username in .env file.

## Launch with Docker

#### Install Docker
Install docker and docker-compose (see instructions on https://www.docker.com/)

### Quick Launch (no debugging)

```bash
docker-compose up
```

### Launch and Attach (supports debugging)

1.  ### First build and run the debug Docker image
    ```bash
    docker-compose -f docker-compose.debug.yml up --build
    ```

2.  ### Attach to Rasa SDK server (actions server)
    In VSCode 'Run and Debug' tab, select 'docker attach rasa run actions' and click Start Debugging.

3.  ### Attach to Rasa open-source server (core/nlu server)
    In VSCode 'Run and Debug' tab, select 'docker attach rasa run' and click Start Debugging.
