# accountBook
## 웹크롤링으로 계좌거래내역조회 (24-06-03 ~ 진행중)
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python-&logoColor=white">
**개요** 
엑셀로 가계부를 쓰시는 부모님을 위해 자동화

**내용**
국민은행에서 계좌거래내역을 엑셀다운로드 후 가계부 작성하는 과정을
파이썬으로 배치 파일을 만들어 자동화하려고 계획

**과정**
* 파이썬 환경 구성 (파이썬 설치 / vs코드 )
* 라이브러리 선정 ➡️ selenium / BeautifulSoup

**이슈**
* 웹크롤링 보안 문제
* 국민은행 개발자모드 접금 금지
* 금융결제원 api 유료
* 국민은행 빠른조회 서비스 신청 필요

**방안**
국민은행 빠른조회 서비스를 통해 html 소스에 접근 계획
-> 계속해서 방안 고민하면서 해결 예정
