
# League Highlights




## Acknowledgements

 - [Django Documentation](https://docs.djangoproject.com/en/3.2/)
 - [Rapid Api](https://rapidapi.com/)
 - [Database Models](https://dbdiagram.io/home)

  
## API Reference
 - [Rapid Api](https://rapidapi.com/)

#### Get all items

```http
  GET /api/data
```

| Parameter | Type      | Description                |
| :-------- | :-------  | :------------------------- |
| `api_key` | `varchar` | **Required**. Your API key |

#### Get item

```http
  GET /api/profile/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



  
## Authors

- [@j.kimani](https://www.github.com/JKimani77)

  
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## Demo

[Demo](https://docs.google.com/presentation/d/1Z96BiO1M9zq6CTGcBM-yrvJ7T8yl7VDJKvThyPHdTiU/edit?usp=sharing)

  
## Documentation

[README](https://github.com/JKimani77/statz/blob/master/README.md)

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`DEBUG` 
`DB_NAME`
`DB_USER`
`DB_PASSWORD`
`MODE`
`ALLOWED_HOSTS`
`DATABASE_URL`
`EMAIL_USE_TLS`
`EMAIL_HOST`
`EMAIL_HOST_USER`
`EMAIL_HOST_PASSWORD`
`x-rapidapi-key`
`x-rapidapi-host`



  
## Feedback
Incorporates use of django channels to serve websockets as asgi app in project.

If you have any feedback, please reach out to us at mail@mail.com.com

  
## Installation 

Install projec-site with django

```ps1 
  mkdir statz
  cd statz

```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Screenshots


![DBDIAGRAM](https://github.com/JKimani77/statz/blob/master/raw/dbd.png?raw=true)

![HOMEPAGE](https://github.com/JKimani77/statz/blob/master/raw/home.png?raw=true)


  
## Used By

Any user who registers a user account on the site and logs in successfully.

  
## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

  
## Support

For support, email jkkimani77@gmail.com or join me on Discord.

  
## Tech Stack

**Client:** Python Django

**Server:** localhost

  
## Roadmap

- Additional browser support

- Add more integrations

- Redis Installation

  
## Run Locally

Clone the project

```Ps1
  git clone https://github.com/JKimani77/statz.git/
```

Configure database settings and env variables 

```Ps1
    python manage.py makemigrations highlights
```

```Ps1
    python manage.py migrate
```


Go to the project directory

```Ps1
  cd statz
```

Install dependencies

```Ps1
  pip install -r requiements,txt;pip freeze
```

Start the server

```Powershell 1
  python manage.py runserver
```

  