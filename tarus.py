import e_campus_parser as ecp
from todoist_rest_api import TodoistRESTAPI as tra

url_login = "https://ecampus.changwon.ac.kr/login/index.php"
login_info = {
    "username": "아이디",
    "password": "비밀번호"}

with open('./login_data.txt', 'r') as f:
    login_info['username'], login_info['password'], api_key = f.read().split('\n')

pars = ecp.LectureParser(url_login, login_info)
api = tra(api_key)

key_lect_proj = api.projects['Lectures']
sect_list = api.GetAllSectionsData(key_lect_proj)
key_sect_dict = {}
for i in sect_list:
    key_sect_dict[i['name']] = i['id']

for lect in pars.GetLectList():
    print(lect)
    t_lect = ''
    if lect == '수학및연습1[GEA7001-02]':
        t_lect = '수학 및 연습1'
    elif lect == '컴퓨터개론[GEA7260-00]':
        t_lect = '컴퓨터 개론'
    elif lect == '한국사의이해[GEA7323-01]':
        t_lect = '한국사의 이해'
    elif lect == '포스트모던시대청년의삶과미래설계[GEA7541-00]':
        t_lect = '포스트모던 시대 청년의 삶과 미래 설계'
    elif lect == '대학생활의설계(CDP-C)[GEA8001-01]':
        t_lect = '대학 생활의 설계'
    elif lect == '대학영어Ⅰ[GEA8704-10]':
        t_lect = '대학영어 I'
    for todo in pars.GetLectTodo(lect):
        date = pars.GetLectTodo(lect)[todo][:16]
        print('\t', todo, date)
        api.CreateNewTask(todo, key_lect_proj, key_sect_dict[t_lect], due_string=date)
