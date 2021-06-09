# pollenparser

This pollen parser takes data from the [meteo.be](https://www.meteo.be/nl/weer/verwachtingen/stuifmeelallergie-en-hooikoorts) and parses it and gives back the date and risk for stuifmeelallergie.

## Run locally

Install the requirements
```pip3 inistall -r requirements.txt```
And run the app
```python3 app.py```

### Run with Docker

To run this project locally in Docker, you need to:
* Clone the repo
* Build it locally

```
  git pull https://github.com/Kwinnieprince/pollenparser.git
  cd pollenparser
  docker build kwintend/pollenparser:latest
  docker run -p 5000:5000 pollenparser
```

#### DockerHub

This project is available on [DockerHub](https://hub.docker.com/repository/docker/kwintend/pollenparser)

## Live site

* You can see the API [here](https://api.kwinten.me/v1/pollenparser)
* The website where it is used can be found [here](https://weg.kwinten.me)

## Credits

many thanks to [Kevin-De-Koninck](https://github.com/Kevin-De-Koninck/pollen-parser) for inspiring this version of his pollen parser
