def vm2=[:]
vm2.name = 'vm2'
vm2.host = '192.168.56.104'
vm2.user = 'thanapat'
vm2.port = 22
vm2.password = 'thanapat1234'
vm2.allowAnyHosts = true

def vm3=[:]
vm3.name = 'vm3'
vm3.host = '192.168.56.105'
vm3.user = 'thanapat'
vm3.port = 22
vm3.password = 'thanapat1234'
vm3.allowAnyHosts = true


pipeline {
    agent any

    stages {
        stage('UnitTest on Vm2') {
            steps {
                echo 'Testing..'
                 script {
                    echo 'git pull'
                    sshCommand(remote: vm2, command: 'cd jenkins-assignment/ && git pull')
                
                    echo 'Run unit test'
                    sshCommand(remote: vm2, command: 'cd jenkins-assignment/ && python3 unit_test.py')
                }
            }
        }
        stage('Build on Vm2') {
            steps {
                script {
                    echo 'Building..'
                    sshCommand(remote: vm2, command: "cd jenkins-assignment/ && echo 'thanapat1234' | sudo -S docker-compose up -d --build")
                }
            }
        }
        stage('RobotTest on Vm2') {
            steps {
                script {
                    echo 'git pull'
                    sshCommand(remote: vm2, command: 'cd robot-assignment/ && git pull')

                    echo 'Testing..'
                    sshCommand(remote: vm2, command: "python3 -m robot robot-assignment/test_api.robot")
                }
            }
        }
        stage('Push image to gitlab Registry on Vm2') {
            steps {
                script {
                    echo 'gitlab login & push'
                    sshCommand(remote: vm2, command: "cd jenkins-assignment/ \
                    && echo 'thanapat1234' | sudo -S docker login registry.gitlab.com \
                    && echo 'Jimmymonster' \
                    && echo 'glpat-f4dTxzyDBemNLeNr8MZj' \
                    && echo 'thanapat1234' | sudo -S docker build -t registry.gitlab.com/jimmymonster/jenkins-api-unittest . \
                    && echo 'thanapat1234' | sudo -S docker push registry.gitlab.com/jimmymonster/jenkins-api-unittest"
                    )

                }
            }
        }
        stage('Deploy on Vm3') {
            steps {
                echo 'gitlab pull and create container'
                sshCommand(remote: vm3, command: "echo 'thanapat1234' | sudo -S docker login registry.gitlab.com \
                    && echo 'Jimmymonster' \
                    && echo 'glpat-f4dTxzyDBemNLeNr8MZj' \
                    && echo 'thanapat1234' | sudo -S docker pull registry.gitlab.com/jimmymonster/jenkins-api-unittest \
                    && echo 'thanapat1234' | sudo -S docker stop api \
                    && echo 'thanapat1234' | sudo -S docker rm api \
                    && echo 'thanapat1234' | sudo -S docker run -d -p 8001:5000 --name api registry.gitlab.com/jimmymonster/jenkins-api-unittest"
                    )

            }
        }
    }
}