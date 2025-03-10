# 科研通青龙签到脚本

一个基于青龙面板的科研通自动签到工具，支持多账号管理、推送通知和异常处理。

![img](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2738%27%20height=%2710%27/%3e)![image](https://img.shields.io/github/stars/sheetung/ablesciCheck)![img](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2739%27%20height=%2710%27/%3e)![image](https://img.shields.io/github/forks/sheetung/ablesciCheck)![img](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2745%27%20height=%2710%27/%3e)![image](https://img.shields.io/github/issues/sheetung/ablesciCheck)

## 🌟 功能特性

1. **多账号管理**：支持同时管理多个科研通账号，自动循环签到
2. **智能识别状态**：自动判断签到结果（成功 / 失败 / 已签到）
3. **多推送通知**：
   - 钉钉机器人消息提醒（支持 Markdown 格式）
   - Bark 消息推送（iOS 专属，未测试）
4. **异常处理机制**：自动捕获网络错误、Cookie 失效等问题
5. **日志记录**：控制台输出详细的签到过程和结果

## 🚀 使用方法

### 1. 订阅配置

在青龙面板「订阅管理」中添加：

- **名称**：科研通打卡
- **链接**：`https://github.com/sheetung/ablesciCheck.git`
- **分支**：`master`
- **定时规则**：`0 0 1 1,7 *`（每月 1 号和 7 号凌晨 1 点执行）
- **文件后缀**：`py`

### 2. 环境变量配置

在青龙面板「环境变量」中设置：

```bash
# 多个Cookie用&分隔
export ABLESCI_COOKIES="cookie1&cookie2&cookie3"
```

在青龙面板「配置文件」中设置：

```bash
# 钉钉推送配置（可选）
export DD_BOT_TOKEN="your_dingtalk_token"
export DD_BOT_SECRET="your_dingtalk_secret"

# Bark推送配置（可选，未测试）
export BARK_PUSH="your_bark_key"
```



## 📦 部署说明

1. 确保青龙面板已安装 Python 环境
2. 通过 Git 或手动上传方式部署脚本
3. 首次运行前检查环境变量是否正确配置

## 📝 运行示例

```bash
正在签到第 1 个账号...
正在使用 Cookie 签到: abcdefghijklmnopqr...
签到结果: {'status': 'error', 'message': '签到失败，您今天已于 [07:00:01] 签到'}
第 1 个账号签到完成

签到结果汇总：
{'status': 'error', 'message': '签到失败，您今天已于 [07:00:01] 签到'}
✅ bark推送成功
✅ 钉钉推送成功
```

## ⚠️ 注意事项

1. 钉钉推送功能需要正确配置机器人权限，例如关键词和`DD_BOT_SECRET`
2. 本工具仅用于学习交流，禁止用于商业用途

## 📜 声明

```plaintext
本项目所有代码仅用于学习和研究目的，严禁用于商业用途。
用户需遵守《科研通用户协议》及相关法律法规。
下载后请在24小时内删除，否则一切法律后果自负。
```

## 📢 反馈与贡献

- 提交问题：[GitHub Issues](https://github.com/sheetung/ablesciCheck/issues)
- 代码贡献：[Fork & Pull Request](https://github.com/sheetung/ablesciCheck/pulls)
- 联系作者：sheetung@example.com

> 开源协议：MIT License