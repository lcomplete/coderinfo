# 关于这个开源项目

## 2013 年的故事

这个网站是我 2013 年花了两个晚上的时间做的，原来的域名是 coderinfo.com，一直放在线上直到 2017 年，于 2022 年重新上线。

最初做这个网站的原因：

- 许多网站未提供 RSS，比如知乎收藏夹、知乎日报、微信精选等。
- 打算将采集的文章进行相似度比较，做一个内容热点，这个想法搁置了。相似度比较的算法，我写了一个 dotnet 的版本 [ArticleUtils.cs](https://github.com/lcomplete/WordSegmentation/blob/master/WordSegmentation/ArticleUtils.cs)。

因此，做了这样一个简单的网站，只需要配置网站首页，即可自动抓取文章正文，供自己浏览。

### 关于代码

这仅是我花两个晚上时间做的网站，因此不要跟我说什么框架、架构、设计，我用 python 一把梭。😄

## 2022 年的故事

### 为什么重新上线这个网站？

仅仅是作为一个衔接未来的起点，日后我将上线更多的产品。

### 关于网址 <http://rssletter.xyz/>

关于 rss ：

- 这个网站后续的方向可以是提供 rss 服务，让许多无法通过 rss 订阅的资源，通过这个网站作为一个管道继续订阅。
- 这个方向仅是一个思路，如果要继续做的话，不会再使用这种一次性代码，而是产品化。

关于 letter ：

- 初步的想法是主要通过这个网站来订阅 newsletter 。

关于 .xyz ：

- xyz 域名便宜。

## 特别感谢以下开源项目

- [python-readability](https://github.com/buriy/python-readability)，最早使用这个开源项目来解析 html 正文。
- [newspaper](https://github.com/codelucas/newspaper)，将 readability 换成了 newspaper 来进行解析，代码中预留了可以使用不同解析器的数据结构设计。
- [github-markdown-css](https://github.com/sindresorhus/github-markdown-css) ，这次重新上线前通过这个开源项目来设置内容样式。

## 运行文档

[Get Started 💻](getstart.md)