pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup venv') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'venv\\Scripts\\python -m flake8 app.py tests/'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python -m pytest -v'
            }
        }
    }
}



