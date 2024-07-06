import requests
import base64
'''
通用文字识别
'''

# 动物图像识别
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
# f = open('a.jpg', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 通用物体和场景识别
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
# f = open('b.jpg', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 图像主体识别
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
# f = open('b.jpg', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 车辆属性识别
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
# f = open('c.jpg', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 通用文字识别
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
f = open('g.png', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}

# 网络图片文字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
# f = open('d.png', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 表格文字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/table"
# f = open('d.png', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 身份证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
# f = open('f.png', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

# 车辆检测
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
# f = open('e.png', 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}

access_token = '24.5c23e917884594a13ac6af35fe08b146.2592000.1722491941.282335-89980475'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())