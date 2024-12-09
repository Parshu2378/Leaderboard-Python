# Leaderboard Application

This project is a Django-based **Leaderboard Application** that allows you to manage users and their scores dynamically. The application includes features such as adding users, updating their points, deleting users, viewing grouped user statistics, and identifying winners periodically.

---

## **Features**

1. **Leaderboard Management**:
   - Users start with 0 points.
   - Increment or decrement points using `+` or `-` buttons.
   - Add and delete users dynamically.
   - View a user's details by clicking on their name.

2. **User Grouping**:
   - View users grouped by their scores.
   - Each group includes the names and average age of users in that group.

3. **Scheduled Winner Selection**:
   - Every 5 minutes, the user with the highest points is declared a winner.
   - If there’s a tie for the highest points, no winner is selected.

4. **Dynamic Frontend**:
   - Real-time leaderboard updates.
   - Visual representation of grouped data using charts.

---

## **Technologies Used**

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, Bootstrap, JavaScript, Axios
- **Database**: SQLite (default), but can be replaced with PostgreSQL or MySQL
- **Task Scheduling**: Celery with Redis
- **Random Data Generation**: Faker Library
- **Icons**: Font Awesome

---

## **Setup Instructions**

### Prerequisites

1. Python 3.7+
2. Pip
3. Virtualenv (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/leaderboard-app.git
   cd leaderboard-app

## **Documentation**
how to include html file in read (/leaderboard_project/templates/documentation.html)