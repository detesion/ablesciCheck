# -*- coding: utf-8 -*-
"""
new Env('科研通签到');
"""
import os
import requests
from utils import check

class AbleSci:
    name = "科研通签到"

    def __init__(self):
        # 从环境变量中获取 Cookie
        self.cookie = os.getenv("ABLESCI_COOKIE")
        if not self.cookie:
            raise ValueError("未找到环境变量 ABLESCI_COOKIE，请检查配置")

    def sign(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": self.cookie,
            "DNT": "1",
            "Referer": "https://www.ablesci.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        url = "https://www.ablesci.com/user/sign"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return {"name": "签到状态", "value": "签到成功", "response": response.json()}
        else:
            return {"name": "签到状态", "value": "签到失败", "response": response.text}

    def main(self):
        result = self.sign()
        return result


@check(run_script_name="科研通签到", run_script_expression="ablesci")
def main(*args, **kwargs):
    return AbleSci().main()


if __name__ == "__main__":
    main()
