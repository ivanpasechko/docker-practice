#!/bin/bash
docker run -d \
  --name mosquitto_broker \
  -p 1883:1883 \
  -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf \
  -v mosquitto_data:/mosquitto/data \
  -v mosquitto_log:/mosquitto/log \
  eclipse-mosquitto:2.0