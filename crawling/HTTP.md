### HTTP 구조
1. Request Line
	- 요청 라인(Request Line): 요청 라인은 HTTP 메서드(GET, POST, PUT, DELETE 등), 요청 대상의 URI, 그리고 사용하는 HTTP 버전으로 구성됩니다. 예를 들어, `GET /index.html HTTP/1.1`은 "HTTP/1.1 버전을 사용하여 /index.html에 대한 GET 요청"을 나타냅니다.
	- Request-Line = Method SP(스페이스바) Request-URL SP HTTP-Version CRLF(엔터) . `GET /index.html HTTP/1.1`
	
1. 0개 이상의 헤더
	- 헤더(Header): 헤더는 클라이언트와 서버가 요청 또는 응답에 대한 추가 정보를 교환하는 공간입니다. 헤더는 한 개 이상일 수 있으며, 각 헤더는 헤더 이름과 헤더 값으로 구성됩니다. 예를 들어, "Content-Type(body): text/html"은 "해당 문서의 타입이 HTML임"을 나타냅니다.
3. 빈 라인
	- 빈 라인: 헤더와 바디 사이에는 반드시 빈 라인이 있어야 합니다. 이 빈 라인은 "\r\n"(carriage return과 line feed)으로 표현됩니다. 이 빈 라인은 헤더가 끝나고, 바디가 시작되는 구분자 역할을 합니다.
4. 바디
	- 바디(Body): 바디는 실제로 전송할 데이터를 담고 있습니다. 예를 들어, POST 요청에서는 HTML 폼에 입력한 데이터가 이 부분에 들어갑니다. GET 요청에서는 바디가 없을 수도 있습니다.

### HTTP Methods
- GET : 주지는 않고 웹사이트에게 받기만 하겠다는 표시
- POST : 내가 데이터를 주고 거기에 맞게 처리해서 응답하라는 뜻
