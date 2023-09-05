import argparse
import requests

# 定义参数
parser = argparse.ArgumentParser(description='Send post request to API with title, desp, and url')
parser.add_argument('--api', type=str, help='The API to send the post request to')
parser.add_argument('--title', type=str, help='The title of the post request')
parser.add_argument('--desp', type=str, default='', help='The description of the post request')
parser.add_argument('--url', type=str, default='', help='The URL as a part of post data')
parser.add_argument('--quiet', action='store_true', help='Quiet mode')

# 解析参数
args = parser.parse_args()

# 发送post请求
data = {'title': args.title, 'desp': args.desp, 'url': args.url}
response = requests.post(args.api, data=data)

# 如果 --quiet 参数被提供，则不提示错误
if not args.quiet and response.status_code != 200:
    print(f'Error: Failed to send post request, status code: {response.status_code}')
