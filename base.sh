#!/bin/bash

# Create the main project directory
mkdir -p project_cobra

# Create backend directories and files
mkdir -p project_cobra/backend/utils
mkdir -p project_cobra/backend/templates

touch project_cobra/backend/app.py
touch project_cobra/backend/config.py
touch project_cobra/backend/models.py
touch project_cobra/backend/routes.py
touch project_cobra/backend/utils/__init__.py
touch project_cobra/backend/utils/email_verification.py
touch project_cobra/backend/utils/game_logic.py
touch project_cobra/backend/templates/index.html

# Create frontend directories and files
mkdir -p project_cobra/frontend/static

touch project_cobra/frontend/index.html
touch project_cobra/frontend/static/styles.css
touch project_cobra/frontend/static/script.py

# Create README.md and requirements.txt
touch project_cobra/README.md
touch project_cobra/requirements.txt

echo "Project structure created successfully!"
