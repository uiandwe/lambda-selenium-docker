# lambda-selenium-docker

lambda에서 docker 컨테이너에서  selenium  사용을 위한 기본 파일 입니다. 

2022.11.03 에 마지막 작동 확인했습니다!!


빌드시 반드시 '--platform linux/x86_64' 해당 옵션을 넣어주세요.

'''
docker build --platform linux/x86_64 -t lambda-selenium-docker -f Dockerfile .
'''
