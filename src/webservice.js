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
var currentUrl = "http://ec2-16-171-199-141.eu-north-1.compute.amazonaws.com";

let webService = axios.create({
      headers: {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "Access-Control-Allow-Origin": "*",
      },
    baseURL: currentUrl + '/api',
    withCredentials: true,  
});

export default webService;