pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Denskerz/first-blog.git'
		echo "\033[35m Checkout was completed. \033[0m"
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'python manage.py migrate'
                        sh 'python manage.py collectstatic --noinput'
	                echo "\033[35m Build was completed. \033[0m"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python manage.py test'
	                echo "\033[35m Test was completed. \033[0m"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python manage.py runserver'
	                echo "\033[35m Deploy was completed. \033[0m"
                    }
                }
            }
        }
    }
}
