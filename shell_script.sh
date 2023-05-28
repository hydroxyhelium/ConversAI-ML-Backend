#!/bin/sh
python3 discord-data/handle.py
mv discord-data/output.txt model/data/input.txt
python3 model/data/discord_data prepare.py
python3 train.py mode/config/finetune_discord.py


