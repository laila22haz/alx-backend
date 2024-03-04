import redis from "redis";
const {promisify} = require('util');


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client); 
// now getAsync is a promisified version of client.get:

client.on('error', (err) => { 
    console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', () => {
    console.log('Redis client connected to the server')
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(`Error setting value: ${err}`);
        } else {
            redis.print('Replay: OK');
        }
    });
}

const displaySchoolValue = async (schoolName) => {
    const res = await getAsync(schoolName);
    console.log(res);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');