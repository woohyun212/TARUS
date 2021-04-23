from bs4 import BeautifulSoup
import requests


class LectureParser:
    def __init__(self, url, login_info):
        self.url_login = url
        self.login_info = login_info
        self.sess = requests.Session()
        # HTTP POST request: 로그인을 위해 POST url 과 함께 전송될 data 를 넣어주자.
        self.login_req = self.sess.post(self.url_login, data=login_info).text
        self.lect_list = self.GetLectList()

    def GetLectList(self):
        # Session 생성, with 구문 안에서 유지
        # 파싱된 메인화면에서 course_box 클래스를 갖는 태그를 가져오자
        soup = BeautifulSoup(self.login_req, 'html.parser')

        # 파싱한 데이터를 {강좌 이름 : 강좌 링크} 로 저장하자
        lect_name_list = [element.find('h3').text for element in soup.findAll('div', class_="course-title")]
        lect_link_list = [element['href'] for element in soup.findAll('a', class_="course_link", href=True)]
        return dict(zip(lect_name_list, lect_link_list))

    def GetLectTodo(self, lecture_name):
        # 이번주에 들어야하는 강좌 파싱하기
        url_course = self.lect_list[lecture_name]
        course_req = self.sess.post(url_course, data=self.login_info)
        soup = BeautifulSoup(course_req.text, 'html.parser')
        class_smcc_avmd = soup.find(class_='section main clearfix current')
        # 만약 이번주에 들어야하는 동영상이 목록에 없으면
        if class_smcc_avmd is None:
            return dict(zip("None", ""))
        class_smcc_avmd = class_smcc_avmd.findAll(class_="activity vod modtype_vod")

        # 파싱한 데이터를 {강의명 : 기한} 로 저장하자
        title = [BeautifulSoup(str(bs4_element), 'html.parser').find(class_='instancename').text.strip() for bs4_element
                 in class_smcc_avmd]
        deadline = [element.find(class_="text-ubstrap").text[:42].split("~")[1].strip() for element in class_smcc_avmd]
        return dict(zip(title, deadline))

