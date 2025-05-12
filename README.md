📚 Flask Study Platform

🚀 Project Description
Flask Study Platform is a web application built using Flask, Docker, and WSL. It helps students easily share, manage, and exchange study materials such as lecture notes, 
textbooks, and practice exams. Users can securely register, log in, upload study resources, post and reply to study notes, and mark requests as completed. 
An administrative panel allows efficient management of users, materials, and notes.

-----------------------------------------
✨ Features

🔐 User authentication (Sign up, login, logout)
📝 Post notes to request study materials
📂 Upload and categorize study materials
💬 Reply to classmates' notes
✅ Mark "requests" as fulfilled
🛠 Admin panel to manage users, notes, and uploads

-----------------------------------------
📦 Technologies Used

🐍 Python 3.12
🔥 Flask
🐬 SQLite (with SQLAlchemy ORM)
🐳 Docker & Docker Compose
🖼 HTML/CSS (Bootstrap), JavaScript
💻 WSL2 for development on Window

-----------------------------------------
📂 Project Structure
website/
├── static/
│   ├── uploads/
│   └── images/
├── templates/
│   ├── login.html
│   ├── sign_up.html
│   ├── home.html
│   ├── upload.html
│   ├── materials.html
│   ├── admin.html
│   └── reset_password.html
├── __init__.py
├── auth.py
├── views.py
└── models.py
Dockerfile
docker-compose.yml
requirements.txt
main.py

------------------------------------------
🔧 Installation

1. ✅ Make sure Docker Desktop with WSL2 integration is enabled
2. 📁 Clone the repository:

git clone https://github.com/ninoghonghadze/flask-StudyPlatform.git
cd flask-StudyPlatform

3. 🐳 Build and run the application:

docker-compose up --build

4. 🔗 Access the application at:

http://localhost:5000

-----------------------------------------
👥 User Roles

Student can:

Sign up, log in/out
Post notes (requests)
Upload & categorize study materials
Reply to notes
Edit/delete own notes

Admin can:

Everything students can do ✅
View/delete users, materials, and all notes
Access a dedicated /admin panel

-----------------------------------------
🖱 How to Use
*Register/Login: Create an account or log in.
*Upload Materials: Use the "Upload Material" page.
*Post Notes: Share your study notes or requests from the home page.
*Admin Panel: If you are an admin, manage content through `/admin`.

📸 Screenshots
🏠 Home Page
[Home Page](static/images/screenshot_home.png)
📝 Sign-Up Page  
[Sign-Up Page](static/images/screenshot_sign-up.png)
🔐 Login Page
[Login Page](static/images/screenshot_log-in.png)
📤 Upload Material
[Upload](static/images/screenshot_upload.png)
[Upload](static/images/screenshot_upload(1).png)
📚 View Materials  
[Materials Page](static/images/screenshot_material.png)
[Materials Page](static/images/screenshot_material(1).png)
🛡 Admin Panel
[Admin Panel](static/images/screenshot_admin.png)

-----------------------------------------
🙌 Credits
Nino Ghonghadze: Project developer & maintainer. [GitHub](https://github.com/ninoghonghadze)

