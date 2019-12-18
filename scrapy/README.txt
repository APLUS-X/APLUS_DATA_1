1. 该项目需要python3+, 需要安装scrapy、Redis 
2. 在运行爬虫前，请运行zib_scrapy/tool/update_redis_proxy.py以更新代理, 运行之前修改上文件中代码中的91行中validation的函数以更针对快速地过滤失效代理
3. 京东评论爬虫流程: 在项目根目录执行 python3 cmdline.py crawl jd_comment -> 运行zib_scrapy/data_handling/dj_comment_redis2pgsql.py以上传至数据库
4. 天猫评论爬虫部分已基本完成，但还无法正常运行
5. 爬虫开始执行时可能异常退出，多尝试几次即可


