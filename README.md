# M.O.N.T.E.R.O's J.A.R.V.I.S.
My Own Naughty Telegram-Engineered Robot Operator aka J.A.R.V.I.S.

This repository contains all parts involved in the automation of my day to day tasks. You will find here code related to domotics and automation using primarily Python and C#. Feel free to use it if you need :wave:

## Background

Just A Rather Very Intelligent System (J.A.R.V.I.S.) was originally Tony Stark's natural-language user interface computer system, named after Edwin Jarvis, in honor of the butler who worked for Howard Stark and the Stark household.

Over time, he was upgraded into an artificially intelligent system, tasked with running business for Stark Industries as well as security for Tony Stark's Mansion and Stark Tower.

## Contents

### Telegram bot (~/telegram)

Telegram bot developed using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). 

Functionalities:

- Home watchman. Send door contact sensor information (door opened and closed) using Tuya Cloud ecosystem and videos from an IP camera via RTSP protocol when the sensor notices that the door has been opened.

Consider create a ``.env`` file to configure all parameters used in ``main.py``.

```
BOT_API_KEY=<YOUR_API_KEY>
ALLOWED_CHAT_ID=<YOUR_TELEGRAM_CHAT_ID_WITH_BOT>
NOTIFICATION_RATE_S=<SECONDS_NOTIFICATION_RATE>
...
```

### Energy saver (~/energy-saver)
