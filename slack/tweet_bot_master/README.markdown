# Tweet Bot


![](https://img.shields.io/badge/python-3-brightgreen.svg) ![](https://img.shields.io/badge/tensorflow-0.12.0-yellowgreen.svg)


## Setup


- **pull pretrained model**

```bash
# pull metadata
wget -c 'https://www.dropbox.com/s/d35skwq8hk2ljbr/metadata.pkl?dl=0' -O metadata.pkl
# pull pretrained model
cd ckpt
./pull
cd ..
```

- **setup slack bot**

follow this tutorial to set up slack bot
https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

## Execute


- **chatbot**

```python
import chatbot
# >> Initializing data
# >> Initializing model
# <log> Building Graph </log>
# >> Loading pretrained model
# >> Initialization complete; call respond(msg)
chatbot.respond('Hey! Good morning.. Have a nice day.')
# 'have a wonderful weekend'
```

- **autoreply**

```
python slack_bot.py
```
