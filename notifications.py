import requests, json

class Notify:

    url = 'https://api.pushover.net/1/messages.json'
    token = ''
    user = ''
    message = ''

    def __init__(self):
        self.DataValues()

    def DataValues(self):
        with open('settings.json') as json_file:
            data = json.load(json_file)

            for i in data['notifications']:
                Notify.token = i['token']
                Notify.user = i['user']
                Notify.message = i['message']
    

    def SendNotification(self, output):
        data = {
            'token': Notify.token,
            'user' : Notify.user,
            'message': Notify.message
        }

        response = requests.post(self.url, data)

        if output == True:
            print(response.text)