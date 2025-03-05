## 🌐 Network - A Social Media Web App

#### 🔗 Live Demo: []

### 📜 Overview
Network is a Django-based social media web application where users can create posts, follow others, like posts, and engage with an interactive timeline. The app dynamically updates content using JavaScript to provide a smooth user experience.

### 🚀 Features

✅ **User Authentication** – Register, log in, and log out

✅ **Create Posts** – Users can compose and publish text-based posts

✅ **All Posts Feed** – View all posts from all users in reverse chronological order

✅ **Profile Pages** – View user profiles with follower and following counts

✅ **Follow/Unfollow Users** – Follow other users to see their posts in your personalized feed

✅ **Following Feed** – See posts exclusively from users you follow

✅ **Like & Unlike Posts** – Toggle likes on posts, updated asynchronously

✅ **Edit Posts** – Edit your own posts without reloading the page

✅ **Pagination** – Navigate through posts with "Next" and "Previous" buttons

### 🛠️ Installation & Setup

#### Clone the Repository
```sh
git clone https://github.com/Martina-Talan/network.git
cd network
```

#### Install Dependencies
```sh
pip install -r requirements.txt
```

#### Apply Database Migrations
```sh
python manage.py makemigrations network
python manage.py migrate
```
#### Create a Superuser (Optional for Admin Access)
```sh
python manage.py createsuperuser
```
#### Start the Development Server
```sh
python manage.py runserver
```
#### Open the app in your browser: http://127.0.0.1:8000/

### 🔗 API Routes

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/posts/all` | Fetch all posts in reverse order |
| GET    | `/posts/following` | Fetch posts from followed users |
| GET    | `/profile/<username>` | View a user's profile and their posts |
| POST   | `/posts/new` | Create a new post |
| PUT    | `/posts/<int:post_id>` | Edit an existing post |
| PUT    | `/posts/<int:post_id>/like` | Like/unlike a post |
| POST   | `/follow/<username>` | Follow/unfollow a user |


### 📌 Usage
1️⃣ **Register/Login** – Create an account and sign in

2️⃣ **Create & View Posts** – Publish posts and browse content from all users

3️⃣ **Profile Pages**– Click on a username to view their profile, followers, and following

4️⃣ **Follow Users** – Follow/unfollow users and see their posts in the "Following" feed

5️⃣ L**ike & Unlike** – Interact with posts by toggling likes

6️⃣ **Edit Posts** – Modify your own posts inline without reloading

7️⃣ **Paginated Feeds** – Navigate through posts efficiently

### 🛠️ Technologies Used
- __Django__ – Backend framework

- __JavaScript__  – Dynamic frontend interactions

- __HTML & CSS__ – UI structure and styling

- __Bootstrap__ – Responsive design

### 🏆 Acknowledgments
This project is part of the Harvard CS50W: Web Programming with Python and JavaScript course.

