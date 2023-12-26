pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
			credentialsId: 'jenkins',
			url: 'git@github.com:Denskerz/first-blog.git'
		sh "ls -la"
      }
        }

        stage('Build') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'python manage.py migrate'
                        sh 'python manage.py collectstatic --noinput'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python manage.py runserver'
                    }
                }
            }
        }
    }
}
