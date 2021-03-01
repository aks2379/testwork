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
                sudo apt-get install apache2 -y
                systemctl 
                """                              
                echo 'We are in Build stage: Httpd started'
            }
        }
        stage('Deploy'){
            steps {
                sh """
                echo 'Hello World from Ashish' > /var/www/html/Index.html
                """
            }
        }
    }
}