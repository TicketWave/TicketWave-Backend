pipeline { 
    agent any

    stages {
        stage('Clean workspace') {
            steps {
                sh '''
                sudo rm -rf /var/lib/jenkins/workspace/TicketWave-Backend-Pipeline/*
                '''
            }
        }
        stage('Fetch') {
            steps {
                git branch: 'main',
                url: 'https://github.com/TicketWave/TicketWave-Backend.git'
            }
        }
        stage('Prepare env variables') {
			steps {
			    sh '''
			    cp /home/omar/.env /var/lib/jenkins/workspace/TicketWave-Backend-Pipeline/Ticketwave/
			    '''
			}
		}
        stage('Clean and setup') {
            steps {
                sh '''
                sudo rm -rf /home/omar/TicketWave-Backend/*
                sudo mv /var/lib/jenkins/workspace/TicketWave-Backend-Pipeline/* /home/omar/TicketWave-Backend/
                '''
            }
        }
        stage('Docker compose down') {
            steps {
                sh '''
                cd /home/omar
		docker-compose down
                '''
            }
        }
        stage('Docker compose up') {
            steps {
                sh '''
                cd /home/omar
		sudo docker-compose up -d --build
                '''
            }
        }
    }
    post {
        failure {
            echo "======== Tests failed ============="
            mail to: 'omar.atef.ahmed@gmail.com',
    		subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
    		body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}
