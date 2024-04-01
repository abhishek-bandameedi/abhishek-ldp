pipeline {
    agent any

    stages {
        stage("Clone Repository"){
            steps {
                git branch: 'kafka_finalAssignment', credentialsId: 'githubtoken1', url: 'https://github.com/abhishek-bandameedi/abhishek-ldp.git/'
            }
        }
        stage("Build"){
            steps {
                  sh """
                    cd /var/lib/jenkins/workspace/final-assignment/kafka/final-Assignment/producer &&
                    mvn clean package
                """
            }
        }
        stage("Run Tests"){
            steps{
                sh """
                    mvn test
                """
            }
        }
    }
    post {
        always {
            echo "=== Pipeline Completed ==="
        }

        success {
            echo "=== Pipeline Successfully Completed ==="
        }

        failure {
            echo "=== Pipeline Failed ==="
        }
    }
}