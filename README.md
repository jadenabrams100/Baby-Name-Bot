# BabyNameBot

Depenencies Needed to run:

* discord
* python-dotenv

Install these with ```pip install -r requirements.txt```

Start the bot with ```python main.py```

Source file is current as of 11/03/2024 01:22 PM EST

Thanks to Claire (claireconklin@gmail.com) for aiding in updating the list

Made with assistance from:
* https://github.com/indently/discord_tutorial_2024/tree/main
* https://github.com/elijahwe/wknc-bot


Running with Docker:
1. Create the image from the Dockerfile with ```sudo docker build -t baby-name-bot .```. This will create a docker image with the name ```baby-name-bot```
2. Run the container with ```sudo docker run --name running-baby-name-bot -d baby-name-bot```. This will run the image from step 1 in a container named ```running-baby-name-bot```.

Stopping the container:
1. Stop the container with ```sudo docker container stop running-baby-name-bot```. If this is not the correct container, use ```sudo docker ps -a``` to view the running containers.

Removing image and container:
1. After completing the steps in Stopping the container, run ```sudo docker rm running-baby-name-bot``` to remove the container.
2. run ```sudo docker image remove baby-name-bot``` to remove the image.

Updating the bot.
1. Add in the strings.
2. Generate input JSON files with ```python jsongenerator.py```
3. Go into ```first.json```, ```middle.json```, and ```last.json``` in the editor of your choice and replace all instances of ```\n``` with ``` ```
