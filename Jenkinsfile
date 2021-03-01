pipeline {
    agent any
    stages {
        stage('Initializing') {
            steps {
                echo 'Initializing Jarvis'
                echo 'Welcome'
            }
        }
        stage('Installing httpd') {
            steps {
                echo 'Installing httpd'
                sh """
                <<EOF
                yum -y install httpd
                systemctl enable httpd
                systemctl start httpd.service
                EOF"""
                
                echo 'We are in Build stage: Httpd started'
            }
        }
        stage('Deploy'){
            steps {
                echo 'We are in Deploy'
            }
        }
    }
}