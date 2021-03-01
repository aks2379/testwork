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
                sh sudo apt -y install httpd
                             
                echo 'We are in Build stage: Httpd started'
            }
        }
        stage('Deploy'){
            steps {
                echo 'Hello World' > var/www/html/Index.html
            }
        }
    }
}