공유폴더지정 해서 컨테이너 만들
```python
docker run -it -v D:/Docker_mypython:/container-folder --name mypython python:3.10-buster python3
```

컨테이너 정지
```python
docker stop mypython
```

컨테이너 삭제
```python
docker rm mypython
```

실행중인 컨테이너 접속
```python
docker exec -it mypython bash
```

---


도커 장고 세팅 순서
먼저 manage.py 이 있는 곳에다가 Dockerfile을 만든다. 확장자없이내용은 아래
# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

2. 그리고 requirements.txt파일에 설치할 패키지를 적고 같은 위치에 놓는다
3. git clone https://github.com/your-username/django_Pinterest.git
4. docker build -t my-django-app .
5. docker run -p 8001:8000 -d --name django_app django_pinterest




---
도커 연결
docker run -it -p 8001:8000 -v D:/Docker_Django:/root -v D:/Docker_Django/.git:/root/.git --name mypython2 python


웹드라이버 주소
C:\Users\Administrator\.wdm\drivers\chromedriver\win64\115.0.5790.111\chromedriver-win32/chromedriver.exe


