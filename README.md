# 🍱 솜슐랭 맛집 리뷰 플랫폼

> 사용자가 솜슐랭에 등록된 식당 상세 정보를 보고 리뷰를 작성하거나 다른 사람의 후기를 볼 수 있는 웹서비스
> Django + Django REST Framework 기반으로 구축되었으며 JWT 인증과 관리자 페이지도 지원합니다.

<br/>

## 📸 실행 화면

### ✅ 식당 상세 페이지
<img width="1440" alt="스크린샷 2025-05-10 오후 9 06 03" src="https://github.com/user-attachments/assets/e30213cd-2253-4797-b319-3de681a25e3a" />

### ✅ 리뷰 작성/목록
<img width="1440" alt="스크린샷 2025-05-10 오후 9 08 13" src="https://github.com/user-attachments/assets/06bd64a7-9f57-4ba1-8c81-0be2838cf524" />
<img width="1440" alt="스크린샷 2025-05-10 오후 9 07 24" src="https://github.com/user-attachments/assets/4cf361ea-3277-448e-b9db-7956b385349d" />

### ✅ 로그인 페이지

<br/>
## 2. Key Features (주요 기능)
- ** 회원가입**:
  - 사용자는 정보 입력(닉네임, 이메일, 비밀번호) 후 가입할 수 있습니다. 
  - 회원가입 시 DB에 유저정보가 등록됩니다.

- **식당 별 상세 페이지**:
  - 식당 상세정보 및 솜슐랭이 추천하는 메뉴를 볼 수 있습니다.
  - 사용자는 각 식당에 대해 개인적인 후기를 남길 수 있습니다.

- **관리자 대시보드**:
  - 관리자는 추천 식당 정보를 등록 및 삭제할 수 있습니다
  - 유저 별 댓글 내용을 관리할 수 있습니다

<br/>

## 3. Technology Stack (기술 스택)

| 구분 | 사용 기술 |
|:---|:---|
| **Frontend** | HTML5, CSS3, Bootstrap5, JavaScript |
| **Backend** | Python 3.12, Django 5.0, Django REST Framework |
| **Database** | MySQL |
| **Authentication** | Simple JWT |
| **Server** | AWS EC2 (Ubuntu 22.04) |
| **Web Server** | Gunicorn 23.0.0, Nginx |
| **Admin** | Django Admin |
| **Version Control** | Git, GitHub |

---

# 5. Project Structure (프로젝트 구조)
```plaintext
restaurant_review_project/
├── config/                    # Django 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│   ...
├── restaurants/               # 식당 앱
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── reviews/                   # 리뷰 앱
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── users/                     # 회원가입, 로그인
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── templates/                 # HTML 템플릿
│   ├── main.html
│   ├── signup.html
│   ├── login.html
│   ├── restaurant_list.html
│   ├── restaurant_detail.html
│   ├── review_list.html
│   └── review_create.html
├── static/                    # CSS, JS 정적 파일
├── media/                     # 이미지 업로드 저장
├── secret.json                # 시크릿 키 파일
├── pyproject.toml             # Poetry 설정
├── manage.py
└── README.md



```

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

