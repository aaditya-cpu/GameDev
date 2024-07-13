# Create a virtual environment for the project
python3 -m venv games
source games/bin/activate


# Install Flask and other dependencies
pip install Flask Flask-SQLAlchemy Flask-Mail Flask-SocketIO bcrypt itsdangerous
pip install mysqlclient
pip install brython

# Setup MySQL Database
sudo mysql -u root -p

Inside MySQL shell:

sql

CREATE DATABASE game_db;
CREATE USER 'game_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON game_db.* TO 'game_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Backend APIs

    User Registration and Login
        /register (POST): Register a new user with email and password.
        /login (POST): Login user with email and password.

    Game Management
        /create_game (POST): Create a new game lobby.
        /join_game (POST): Join an existing game lobby with a key.
        /move_player (POST): Move a player in the game.

# Frontend Pages

    Registration and Login Pages
    Lobby Creation and Joining Pages
    Game Board Page for Snakes and Ladders
    Game Board Page for Uno

# Get it up 
Steps

    Run the Flask server:

    bash

cd backend
flask run
