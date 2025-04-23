# 📘 Profiles REST API

🌐 **Live Demo**: [http://ec2-44-204-231-229.compute-1.amazonaws.com/api/](http://ec2-44-204-231-229.compute-1.amazonaws.com/api/)

---

## 🚀 Project Overview

This is a fully functional REST API built with Django and Django REST Framework. The project supports:

- Creating, updating, and deleting user profiles  
- Authentication with username and password  
- Managing profile feed items (status updates)

---

## 🛠️ Features

- Local development server with Django  
- Custom user model and profile management  
- Token-based authentication system  
- Django admin interface enabled for user management  
- Browsable, self-documenting API with DRF  
- Dockerized setup (alternative to VirtualBox for M1 Macs)  
- Deployed to AWS for real-world testing

---

## 🧰 Tech Stack

- **Python**  
- **Django 2.2**  
- **Django REST Framework 3.9**  
- **Docker**  
- **SQLite** (for development)  
- **AWS** (for deployment)

---

## 🧪 Local Setup

### 🔧 Prerequisites

- Python 3.x (inside the Vagrant box)  
- [Vagrant](https://www.vagrantup.com/)  
- [Docker](https://www.docker.com/)  
- [Git](https://git-scm.com/)

---

### ⚙️ Steps to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/vallabkaranam/profiles-rest-api.git
   cd profiles-rest-api
   ```

2. **Start the Vagrant environment with Docker**  
   This spins up a containerized dev environment using Vagrant and Docker.
   ```bash
   vagrant up --provider=docker
   ```

3. **SSH into the Vagrant machine**
   ```bash
   vagrant ssh
   ```
4.	**Navigate to the project directory and activate the virtual environment**
      ```bash
      cd /vagrant
      source ~/env/bin/activate
      ```

5. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

7. **Access the API in your browser**  
   Visit: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Admin & Auth

- You can access the Django admin panel at:  
  [http://localhost:8000/admin](http://localhost:8000/admin)

- To create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

---

## 🔄 Updating the Deployed App on AWS

To push new changes to the live server:

1. **Push changes to GitHub**
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```

2. **SSH into your EC2 instance**
   ```bash
   ssh ubuntu@your-ec2-public-dns
   ```

3. **Navigate to the app directory**
   ```bash
   cd /usr/local/apps/profiles-rest-api/
   ```

4. **Run the update script**
   ```bash
   sudo sh ./deploy/update.sh
   ```

This script will pull the latest code from GitHub and restart the necessary services.
