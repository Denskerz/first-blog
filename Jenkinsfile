pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
      }
        }

        stage('Build') {
            steps {
                script {
		    sh 'pip3 --version'
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 manage.py migrate'
                    sh 'python3 manage.py collectstatic --noinput'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                   
                    sh 'python3 manage.py test'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'python3 manage.py runserver'
                }
            }
        }
    }
}
