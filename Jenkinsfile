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
                command = <<EOT
                #!/bin/sh
                yum -y install httpd
                systemctl enable httpd
                systemctl start httpd.service
                EOT
                echo 'We are in Build stage'
            }
        }
        stage('Deploy'){
            steps {
                echo 'We are in Deploy'
            }
        }
    }
}