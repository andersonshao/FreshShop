import requests


def get_auth_url():
    """
    取code
    :return:
    """
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_uri = "http://127.0.0.1:8080/complete/weibo/"
    client_id = "2321915185"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={redirect_uri}".format(client_id=client_id, redirect_uri=redirect_uri)
    print(auth_url)


def get_access_token(code):
    """
    取access_token
    :param code: str
    :return:
    """
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url, data={
        "client_id": "2321915185",
        "client_secret": "1b0c20ab487b4a12941917b4c3caae4a",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://127.0.0.1:8080/complete/weibo/",

    })
    pass


def get_user_info(access_token):
    user_url = "https://api.weibo.com/2/users/show.json"
    uid = "5393947686"
    get_url = user_url + "?access_token={at}&uid={uid}".format(at=access_token, uid=uid)
    print(get_url)


if __name__ == '__main__':
    # get_auth_url()
    # get_access_token('366b15d47f3acf05f067dc65e72c641b')
    token = "2.00OM9CtFvMWIXCc133b6b104cKHfaD"
    get_user_info(token)
