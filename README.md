# GBF Bookmaker Auto Generator

一个 GBF 团战马票走势图生成器

**本项目大概率会重写**

## How to use

chrome 文件夹中是一个扩展，在马票界面打开扩展面板点击 "Get" 会收集当前的数据。

目前发送位置是我的 VPS 上，你可以修改 chrome/popup.js 中的 `xhr.open` 中的第二个参数来修改。

python 文件夹中是图片生成器，使用 `python ./httpserver.py` 来运行它。

扩展收集到数据后，在确保图片生成器启动的状态下，点击 Send, 数据就会发送到生成器中并生成折线图。

目前程序中预设了12个时间点，分别在 0800, 1000, 1200, 1400, 1600, 1715, 1730, 1745, 1800, 2000, 2200, 2400, 请在这些时点附近生成图片以避免太大的误差。

在 Python 目录下新建 `twitter.json`, 将你的 Twitter App 信息填入，在 [Twitter Apps](https://apps.twitter.com) 上可以获取到。

```JSON
{
    "consumerKey": "",
    "consumerSecret": "",
    "accessToken": "",
    "accessTokenSecret": ""
}
```

## Dependency

Python 脚本需要以下依赖：

- matplotlib
- tweepy

使用 `pip install` 来安装它们

## To Do

- [x] 发推功能
- [ ] 定时自动生成
- [ ] 每日数据的保存
- [ ] 其他优化

Pull Request is welcomed.