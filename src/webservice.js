// import axios from 'axios';

// const axiosInstance = axios.create({
//   headers: {
//     "Cache-Control": "no-cache",
//     "Content-Type": "application/x-www-form-urlencoded",
//     "Access-Control-Allow-Origin": "*",
//   },
//   baseURL: 'https://postman-echo.com/'
// });

// export default axiosInstance;


import axios from 'axios';
// import router from "../router";
// import { currentURL } from "Helpers/helpers";



//axio create...
var currentUrl = "https://postman-echo.com/" //'http://'+window.location.host;

//console.log('Token is: ', token);
let webService = axios.create({
      headers: {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "Access-Control-Allow-Origin": "*",
      },
    // baseURL: 'http://127.0.0.1:8000/api',
    //baseURL: 'http://phplaravel-421708-1325291.cloudwaysapps.com/api',
    baseURL: currentUrl + '/api'
    //headers: headers,
});

export default webService;