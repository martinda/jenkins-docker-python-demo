node {
    step([$class: 'WsCleanup'])
    checkout scm
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("${env.JOB_NAME}:${env.BUILD_NUMBER}")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && python setup.py test'
        }
    }
    stage('collect test results') {
        junit 'nosetests.xml'
    }
}
