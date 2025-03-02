# -*- coding: utf-8 -*-
"""
new Env('科研通签到');
"""
import os
import requests

class AbleSci:
    name = "科研通签到"

    def __init__(self, cookie):
        self.cookie = cookie

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
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 检查响应状态码
            result = response.json()
            return {"status": "success", "message": "签到成功", "data": result}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"签到失败: {str(e)}"}

    def main(self):
        print(f"正在使用 Cookie 签到: {self.cookie[:20]}...")  # 打印部分 Cookie 用于调试
        result = self.sign()
        print(f"签到结果: {result}")
        return result


def main():
    # 从环境变量中获取所有 Cookie
    cookies = os.getenv("ABLESCI_COOKIES")
    if not cookies:
        print("未找到环境变量 ABLESCI_COOKIES，请检查配置")
        return

    # 将多个 Cookie 按分隔符拆分
    cookie_list = cookies.split("&")
    results = []
    for i, cookie in enumerate(cookie_list):
        # print(f"正在签到第 {i + 1} 个账号...")
        try:
            result = AbleSci(cookie).main()
            results.append(result)
        except Exception as e:
            results.append({"status": "error", "message": f"第 {i + 1} 个账号签到失败: {str(e)}"})
        # print(f"第 {i + 1} 个账号签到完成")

    # 输出所有结果
    print("\n签到结果汇总：")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
