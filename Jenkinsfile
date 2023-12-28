pipeline {
    agent any
    
    options{
	ansiColor('xterm')
	timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
		echo "\033[35m Checkout was complited. \033[0m"
      }
        }

        stage('Build') {
            steps {
                script {
		    sh 'pip3 --version'
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 manage.py migrate'
                    sh 'python3 manage.py collectstatic --noinput'
		    echo "\033[35m Build was complited. \033[0m"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3 manage.py test'
		    echo "\033[35m Tests were complited. \033[0m"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml up -d && sleep 10'
		    echo "\033[35m Web-server has been launched for a 10 seconds. \033[0m"
		    sh 'docker stop $(docker ps -a -q)'
		    echo "\033[35m Web-server has been stopped. \033[0m"
		    sh 'docker rm $(docker ps -a -q)'
		    echo "\033[35m Cash has been removed. \033[0m"
		    echo "\033[35m Deploy was complited. \033[0m"
                }
            }
        }
    }
}
