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
		    sh 'sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
		    sh 'sudo brew install docker docker-compose'
                    sh 'docker-compose -f docker-compose.yml up -d && sleep 10'
		    sh 'docker stop $(docker ps -a -q)'
		    sh 'docker rm $(docker ps -a -q)'
                }
            }
        }
    }
}
