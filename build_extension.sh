#!/bin/bash

set -ex

clobot_docker_image_name="emailtest"        #docker-compose의 image이름을 입력, manifaset도 같은 이름으로 생성되기에 manifast 에서도 {clobot_docker_image_name},tgz입력 필요함
p=$(pwd)                        #현재 디렉토리 복사

cd extension

rm -rf ./*.spx      #피일 삭제
rm -rf ./*.tgz      #파일 삭제

cd $p
sudo docker build -t ${clobot_docker_image_name} .

cd extension
sudo docker save ${clobot_docker_image_name} | gzip > ./${clobot_docker_image_name}.tgz
tar zcfv ${clobot_docker_image_name}.spx *