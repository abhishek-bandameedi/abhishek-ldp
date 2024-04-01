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
                    cd /var/lib/jenkins/workspace/kafka_final_assignment/final_assignment/producer &&
                    mvn clean package
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