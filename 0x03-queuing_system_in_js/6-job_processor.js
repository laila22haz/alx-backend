const Kue = require('kue');
const queue = Kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber , message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});