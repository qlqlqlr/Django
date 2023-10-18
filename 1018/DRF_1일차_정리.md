# REST API

## 오늘 강의를 듣고 나서 ?

- API Server 를 구현할 수 있음

- Server 종류
  - 웹 서버
    - 정적인 콘텐츠(html, css, 이미지 등)를 제공하기 위한 서버
    - 대표적으로 Nginx, Apache 등이 있다
  - API 서버
    - 클라이언트가 데이터를 요청하면, 해당 데이터를 제공하기 위한 서버
    - 일반적으로 API 서버는 WAS 위에서 동작
  - WAS (Web Application Server)
    - 동적인 컨텐츠를 제공하기 위한 서버
      - DB 서버, API 서버, 세션 관리, 보안 등을 모두 포함함
    - 이런 것들을 모두 합쳐서 하나의 애플리케이션 실행 환경을 제공하는 서버

- Django 개발 서버
  - 웹 서버, WAS 이런 거 상관없이 그냥 개발 서버
  - 위의 내용들은 모두 배포시 구분되는 것! 
  - 개발 서버와 별개로 생각해야 한다

- asgi.py, wsgi.py + gunicorn
  - Django 를 WAS로 배포할 수 있도록 도와줌 
    - 동적 파일 처리, db 접근 등을 도와줌
  - 정적 파일
    - 일반적으로는 Nginx 등을 활용
    - `python manage.py collectstatic`
 


## REST 란 ?

```python
# 예전 버전
urlpatterns = {
    path('articles/'),
    path('articles/create/'),
    path('articles/<int:pk>/update/'),
    path('articles/<int:pk>/delete/'),
}

    # RESTful 하게 구현
    # 1. 자원을 식별만 하자!
    # 2. 그럼 자원의 행동?
    #   요청할 때 http method 로 구분하자!
    path('articles/'),
    path('articles/<int:pk>'),
```

- REST API 디자인 가이드

1. URL은 리소스를 표현해야한다.
   - 리소스명은 동사보다는 명사를 사용
   - 행위에 대한 표현이 들어가지 말아야한다.

2. 행위는 HTTP Method 로 표현한다.

```
GET /articles/1/delete/ -> 잘못된 URL 구성
DELETE /articles/1/     -> 자원에 대한 표현 + 행위
```

3. 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용한다.

- user 가 가지고 있는 devices 들을 조회

`GET user/{userid}/devices/`

4. 하이픈(-)은 URL 가독성을 높이는 데 사용

5. 언더바(_)는 URL에 사용하지 않는다.

6. URL 에는 소문자만 사용해라 
   - RFC3986(URL 문법 형식 표준)에서 대소문자를 구별하도록 규정
   - 대소문자에 따라 다른 리소스로 인식

7. 파일 확장자는 URL에 포함시키지 않는다.
   - Accept header 를 사용하여 확장자를 표현함
    ```
    GET articles/don.jpg   -> X
    GET articles/dog HTTP/1.1 Host: articles Accept: image/jpg   -> O 
    ```
