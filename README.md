Application url:
[HousingPredictor](https://ml4-regression-app.herokuapp.com/)


# Machine-Learning-Project



This is first machine learning project.


Creating conda environment
```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```
```
pip install -r requirements.txt
````
To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To add git command
```
git add .
```

To create version/commit all changes by git 
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```
To check remote  url
```
git remote -v
```


To set up CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL =<>
2. HEROKU_API-KEY=<>
3. HEROKU_APP_NAME=ml4-regression-app



Build Docker Image
```
docker build -t <image_name>:<tagname> .
```

Note: Image name for docker must be lowercase

To list docker image
```
docker images
```


Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel
```
pip install ipykernel
```


Data Drift:
when your dataset stats gets changes we call it as data drift