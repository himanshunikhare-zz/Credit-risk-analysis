pipeline { 
    environment { 
        registry = "jatinkj/creditrisk" 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git 'https://github.com/himanshunikhare/Credit-risk-analysis.git' 
                echo "Cloned"

            }
        } 
        stage('Email Notification'){
            steps{
                emailext body: 'Well Done Ur Build Failed.', recipientProviders: [brokenBuildSuspects(), brokenTestsSuspects()], subject: 'Jenkins Job!', to: 'jainjatin4146@gmail.com'
           
        }
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
                echo "Image Build"
            } 
        }
        
        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( 'http://registry.hub.docker.com/', registryCredential ) { 
                        dockerImage.push() 
                    }
                echo "Image Deployed"
                } 
            }
        } 
        
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
                echo "Cleanup complete"
            }
        } 
        
    }
}