# ClickUP API

## Usage

you should first find the task id you want to submit to, you can do this by going to the task and looking at the url, it should look something like this:

```
https://app.clickup.com/t/860qzc0v3
```

the id is the last part of the url, in this case `860qzc0v3`

then you should get your api token from [here](https://help.clickup.com/hc/en-us/articles/6303426241687-Getting-Started-with-the-ClickUp-API)

add api token and task id to the .env file like this:

```
API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxx"
TASK_ID="xxxxxxxxx"
```

then you can run the script like this:

```
python3 clickup.py
```