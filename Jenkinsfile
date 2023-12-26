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
                    sh 'python manage.py migrate'
                    sh 'python manage.py collectstatic --noinput'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                   
                    sh 'python manage.py test'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'python manage.py runserver'
                }
            }
        }
    }
}
