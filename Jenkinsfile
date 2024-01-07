pipeline {
    agent any
    
    options{
	ansiColor('xterm')
    }

    environment {
	def projectName = "first-blog"
	def imageName = "${projectName}"
	def dateNow = new Date().format('yyyyMMddHHmm')
	def buildID = "${env.BUILD_ID}"
	def jobName = "${env.JOB_NAME}"
	def jenkinsURL = "${JENKINS_URL}"
	def urlRepo = "https://github.com/Denskerz/first-blog.git"
	registry = "denskerz/work.sberb"
        registryCredential = 'dockerhub_id'
	dockerImage = ''    
    }

    stages {
	 stage('Init secret information'){
            environment {
                SERVICE_CREDS = credentials(${registryCRedential})
            }

            steps {
                echo 'Service user is $SERVICE_CREDS_USR'
                echo 'Service password is $SERVICE_CREDS_PSW'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
		echo "\033[35m Project name is ${projectName} from ${urlRepo}. \033[0m"
		echo "\033[35m Checkout was complited. \033[0m"
	    }
        }

        stage('Working with image') {
            steps {
                script {
		    stage('Build') {
			echo "\033[35m Image name: ${imageName} \033[0m"
		        echo "\033[35m Running attemp №${buildID} of ${projectName} on ${jenkinsURL}... \033[0m"
                        dockerImage = docker.build registry + ":${imageName}-${dateNow}"
			echo "\033[35m Build was complited. \033[0m"
		    }
		    stage('Publish'){
			docker.withRegistry( '', registryCredential ) {
				dockerImage.push()
		        }
			echo "\033[35m Image has been pushed. \033[0m"
		    }
		    stage('Cleaning up'){
			sh "docker image prune --all --force"
			echo "\033[35m Image has been pruned. \033[0m"
			sh "docker images"
		    }
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
                    sh 'docker-compose -f docker-compose.yml up -d && sleep 20'
		    echo "\033[35m Web-server has been launched at ${dateNow} for a 10 seconds. \033[0m"
		    sh 'docker stop $(docker ps -a -q)'
		    echo "\033[35m Web-server has been stopped. \033[0m"
		    sh 'docker rm $(docker ps -a -q)'
		    sh "docker image prune --all --force"
		    echo "\033[35m Cash has been removed. \033[0m"
		    sh "docker images"
		    echo "\033[35m Deploy was complited. \033[0m"
                }
            }
        }
    }
}
