pipeline {
    agent any

    triggers {
    githubPush()
    }
    stages {
        stage('git') {
            steps {  
                git 'https://github.com/BrianSandiford/REST-API-DOCKER-SQLALCHEMY'
            }
        } 
        stage('Build') {
            steps {
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/build.yml'
            }
        }
        stage('Test') {
            steps {
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/test.yml'

            }
        }

         stage('publish') {
            steps {  
                  withCredentials([sshUserPrivateKey(credentialsId: 'docker_prod_key', keyFileVariable: 'docker_key_variable', passphraseVariable: '', usernameVariable: '')]) {
                    sh 'chmod 777  /var/lib/jenkins/workspace/test/'
                    sh 'scp -r -i $docker_key_variable root@3.16.207.11:/root/demo-dockerfile/REST-API-DOCKER-SQLALCHEMY/reports/path.xml /var/lib/jenkins/workspace/test' 
                    sh 'scp -r -i $docker_key_variable root@3.16.207.11:/root/demo-dockerfile/REST-API-DOCKER-SQLALCHEMY/htmlcov/  /var/lib/jenkins/workspace/test/htmlcov '
                }
            }
        }

        stage('Push') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub', url: 'https://registry.hub.docker.com') {
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/push.yml'
                }
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook credentialsId: 'k8s-managment-server-key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/kubernetes/host', playbook: '/var/lib/jenkins/workspace/test/kubernetes/kubernetes-demodockerfileapp-deployment.yaml'
            }
        }
    }
        post {
         failure {
            mail bcc: '', body: 'Please  verify the build', cc: '', from: 'rooms21@gmail.com', replyTo: '', subject: 'Build has failed', to: 'rooms21@gmail.com'
       
          }
         always {
            junit allowEmptyResults: true, testResults: '**/*.xml'
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '/var/lib/jenkins/workspace/test/htmlcov/htmlcov', reportFiles: 'index.html', reportName: 'RCov Report', reportTitles: ''])
          }

    }
}
