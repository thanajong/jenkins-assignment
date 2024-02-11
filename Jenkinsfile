def vm2=[:]
vm2.name = 'vm2'
vm2.host = '127.0.0.1'
vm2.user = 'adminadmin'
vm2.port = 2022
vm2.password = '12345678'
vm2.allowAnyHosts = true

def vm3=[:]
vm3.name = 'vm3'
vm3.host = '127.0.0.1'
vm3.user = 'adminadmin'
vm3.port = 2023
vm3.password = '12345678'
vm3.allowAnyHosts = true


pipeline {
    agent any

    stages {
        stage('UnitTest on Vm2') {
            steps {
                echo 'Testing..'
                 script {
                    echo 'git pull'
                    sshCommand(remote: vm2, command: 'cd /api-jenkins-assignment && git pull')
                
                    echo 'Run unit test'
                    sshCommand(remote: vm2, command: 'cd /api-jenkins-assignment && python3 unit_test.py')
                }
            }
        }
        stage('Build on Vm2') {
            steps {
                echo 'Building..'
               
            }
        }
        stage('RobotTest on Vm2') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy on Vm3') {
            steps {
                echo 'Deploying.....'
            }
        }
    }
}