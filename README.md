
# Weather

### API Endpoints
##### Register
Method: `POST`  
Endpoint: `/registration/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password1": "PASSWORD",  
    "password2": "PASSWORD",  
    "email": "OPTIONAL_EMAIL"  
}`
##### Login
Method: `POST`  
Endpoint: `/login/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password": "PASSWORD"  
}`

##### Logout
Method: `POST`  
Endpoint: `/logout/`  
Headers: `Authorization: JWT YOUR_TOKEN_HERE`  

##### Weather
Method: `POST`  
Endpoint: `/weather/`  
