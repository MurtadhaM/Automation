const axios = require('axios');
let Origin_CA_Key = 'v1.0-168e05cdd87fbf2657db0dd5-f03917a54f0776a62ca1ddd46f1b4898fc35db85563d9ed4ad2dbde74c1b078f204729d4c2abfaffbf8479c0e146f3974864211c508a439f65815fc5ccce3e5abd3544f5608746656e';
let Global_API_KEY = '97a37ff5b52c3a7f273b5c930546fd0e3e65e';

let FINDASNAKE_ZONE_ID = '4db4340ec56d4502efcc5f298f66768b'
let url = 'https://api.cloudflare.com/client/v4/certificates'
let headers = {
    'X-Auth-User-Service-Key': API_KEY,
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
}
/**
 * curl -X GET "https://api.cloudflare.com/client/v4/zones/cd7d0123e3012345da9420df9514dad0" \ 
-H "Content-Type:application/json" \ 
-H "Authorization: Bearer 1234567893feefc5f0q5000bfo0c38d90bbeb"
 */

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
