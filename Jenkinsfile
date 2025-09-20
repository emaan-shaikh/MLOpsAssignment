pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh '. venv/bin/activate && flake8 app.py tests/'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }
    }
}
