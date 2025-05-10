📚 Flask Study Platform

🚀 Project Description
Flask Study Platform is a web application built using Flask, Docker, and WSL. It helps students easily share, manage, and exchange study materials such as lecture notes, 
textbooks, and practice exams. Users can securely register, log in, upload study resources, post and reply to study notes, and mark requests as completed. 
An administrative panel allows efficient management of users, materials, and notes.

✨ Features
*User Authentication: Secure registration, login, and logout.
*Material Upload: Easily upload and categorize study materials.
*Note Posting & Reply: Post study requests or notes, reply to others, and mark notes as completed.
*Admin Panel: Manage users, materials, and notes efficiently.
*Password Reset: Users can reset forgotten passwords securely.

🛠 Technologies Used
*Flask:A Python microframework used for building the web app.
*Docker: Containerizes the app for consistent environments.
*WSL (Windows Subsystem for Linux): Enables a Linux development environment on Windows.
*Bootstrap: For responsive UI and sleek styling.
*SQLAlchemy: Database interactions with SQLite.

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

🔧 Installation and Setup
📌 Step 1: Clone the repository
bash
git clone https://github.com/ninoghonghadze/flask-StudyPlatform.git
cd flask-StudyPlatform

📌 Step 2: Run with Docker
Ensure Docker Desktop with WSL integration is running, then:
bash
docker-compose up --build

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


🙌 Credits
Nino Ghonghadze: Project developer & maintainer. [GitHub](https://github.com/ninoghonghadze)

