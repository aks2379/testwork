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
                systemctl start apache2
                systemctl status apache2
                """                              
                echo 'We are in Build stage: Httpd started'
            }
        }
        stage('Deploy'){
            steps {
                echo "This is a beautiful world > /var/www/html/index.html"
                }
        }
    }
}