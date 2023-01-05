#!/bin/bash

source ../../../venvs/pi-chef/bin/activate

flask --app pi_chef_webapp run &

chromium-broswer --kiosk http://127.0.0.1:5000