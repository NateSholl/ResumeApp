#!/bin/bash
app="resume.app"
docker build -t ${app} .
docker run -d -p 80:56733 \
  --name=${app} \
  -v $PWD:/app ${app}
