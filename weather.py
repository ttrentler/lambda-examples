import http.client
def lambda_handler(event, context):
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    payload = ''
    headers = {'Authorization': 'Basic Y2lzY286MTIzNA=='}
    conn.request("GET", "/data/2.5/weather?zip=34698,us&APPID=YourOpenWeather.orgIdGoesHere", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
