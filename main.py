# 码动未来
# appid 81063858
# apikey m94szVWpTPDbOC44X8gKbnyg
# secretkey rMvwgOwuXMy93X9m1GACVej1lBKpXB2H
import requests


def main():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XXQVeq5RwQkeWJmSWrwOlGLw&client_secret=OWPCJOBkarw7L1ANA31SvgmU29mH3hqx"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    main()
