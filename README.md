## ConverseAI-ML backend 

This is the documentation for the parsing, and training model on your own discord messages using our API. This also contains a `app.y` file which servers as the backend model for Discord Bot. If you want to JS file which you can use on the server, please look at https://github.com/hydroxyhelium/ConversAI. 


## Prerequisites

You must download request your own messages from discord. For more details see, https://support.discord.com/hc/en-us/articles/360004027692-Requesting-a-Copy-of-your-Data#:~:text=If%20you%20would%20like%20to,Browser%2C%20and%20on%20Mobile!. 

You must set up Cohere API keys and an account for the model to run to over your data. More information can be found here. 
https://docs.aicontentlabs.com/setting-up-api-keys/cohere-api-key/#:~:text=Once%20you%20have%20created%20your,you%20copied%20and%20save%20it.


- Python 3.7 required
- Flask required
- Cohere API keys required

## Installation

```bash
git clone https://github.com/hydroxyhelium/ConversAI-ML-Backend 
```

## Setup up

```bash
echo ${PATH_TO_YOUR_DATA}
echo ${PATH_TO_COHERE_API_KEYS} 
chmod a+x {$PATH_TO_SHELL_SCRIPT}
./shell_script.sh
```

The provided bash script accepts the path to your Discord data, performs preprocessing, and trains the model on your local machine. If you want to expedite the training process, you can connect to Google Colab using the CUDA runtime for faster GPU-accelerated training. The program is designed to automatically detect and utilize available GPU resources.