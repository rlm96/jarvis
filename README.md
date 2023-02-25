# M.O.N.T.E.R.O's J.A.R.V.I.S.
My Own Naughty Telegram-Engineered Robot Operator aka J.A.R.V.I.S.

This repository contains all parts involved in the automation of my day to day tasks. You will find here code related to domotics and automation using primarily Python and C#. Feel free to use it if you need :wave:

## Background

Just A Rather Very Intelligent System (J.A.R.V.I.S.) was originally Tony Stark's natural-language user interface computer system, named after Edwin Jarvis, in honor of the butler who worked for Howard Stark and the Stark household.

Over time, he was upgraded into an artificially intelligent system, tasked with running business for Stark Industries as well as security for Tony Stark's Mansion and Stark Tower.

## Contents

### Telegram bot (~/telegram)

Telegram bot developed using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Rename ``.env-template`` file to ``.env`` and configure all parameters used in ``main.py``.

### Watchman (~/watchman)

Send door contact sensor information via Telegram from recorded UDP packages. The sensor is a WiFi low-power (Tuya) sensor, so it will send UDP broadcast packages (UDP port 6667) when notices a change (open or close).

The watchman also send videos from an IP camera capturing the images via RTSP protocol when the sensor notices an event. 

Rename ``.env-template`` file to ``.env`` and configure all parameters used in ``main.py``.

### Energy saver (~/energy-saver)
