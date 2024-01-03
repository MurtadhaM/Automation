const axios = require('axios');
let Origin_CA_Key = '';
let Global_API_KEY = '';

let FINDASNAKE_ZONE_ID = '4db4340ec56d4502efcc5f298f66768b'
let url = 'https://api.cloudflare.com/client/v4/certificates'
let headers = {
    'X-Auth-User-Service-Key': API_KEY,
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
}


    const getCertificates = async () => {
    try {
        const response = await axios.get(url, {headers})
        console.log(response.data)
    } catch (error) {
        console.error(error)
    }
}   

console.log('Getting certificates...')
getCertificates()

getCertificates()
