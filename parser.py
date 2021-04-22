from bs4 import BeautifulSoup
import requests

session = requests.session()
loginInfo = {
    "username": "아이디",
    "password": "비밀번호"}
# 깃허브에 보이면 안되니까 파일에서 불러오자
with open('./login_data.txt', 'r') as f:
    loginInfo['username'], loginInfo['password'] = f.read().split('\n')

url_login = "https://ecampus.changwon.ac.kr/login/index.php"
# Session 생성, with 구문 안에서 유지
with requests.Session() as sess:
    # HTTP POST request: 로그인을 위해 POST url 과 함께 전송될 data 를 넣어주자.
    login_req = sess.post(url_login, data=loginInfo).text
    # 파싱된 메인화면에서 course_box 클래스를 갖는 태그를 가져오자
    soup = BeautifulSoup(login_req, 'html.parser')
    course_name_list = soup.findAll(class_="course-title")
    course_link_list = soup.findAll(class_="course_link")
    # 파싱한 데이터를 {강좌 이름 : 강좌 링크} 로 저장하자
    name_link_dict = {}
    for index in range(len(course_name_list)):
        name = str(course_name_list[index])
        link = str(course_link_list[index])
        name_link_dict[name[name.find("<h3>") + 4:name.find("</h3>")].strip()] = link[link.find('href=') + 6:link.find(
            '">')].strip()

    # 이번주에 들어야하는 강좌 파싱하기
    url_course = name_link_dict['수학및연습1[GEA7001-02]']
    course_req = sess.post(url_course, data=loginInfo)
    soup = BeautifulSoup(course_req.text, 'html.parser')
    w = soup.find(class_='section main clearfix current')
    instance_name = w.findAll(class_="instancename")
    text_ubstrap = w.findAll(class_="text-ubstrap")

    # 파싱한 데이터를 {할 일 : 기한} 로 저장하자
    lect_deadline_dict = {}
    for index in range(len(instance_name)):
        instance_name[index] = str(instance_name[index]).strip().lstrip('<span class="instancename">')
        instance_name[index] = instance_name[index].replace('<span class="accesshide">', '').replace('</span></span>',
                                                                                                     '')
        text_ubstrap[index] = \
            str(text_ubstrap[index]).strip().lstrip('<span class="text-ubstrap">')[:42].strip().split(' ~ ')[1]
        lect_deadline_dict[instance_name[index]] = text_ubstrap[index]
