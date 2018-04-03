import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': "【A生鲜】您的验证码是{}".format(code)
        }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yunpian = YunPian('39274892d11133e9d5e0221a8cb95ea1')
    yunpian.send_sms('2018', '18036233180')
