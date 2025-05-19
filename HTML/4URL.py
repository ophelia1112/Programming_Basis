# URL(uniform resource locator)定位资源所在位置
# 例如https://chatgpt.com/c/67108032-4e18-8004-b3da-bf7fbd383b69
"""
组成：八部分
协议(protocol)，如http或者https(hyper text transfer protocol)超文本传输协议，用来访问网站的
https，更为安全的协议，网页一般为http协议，不显示，如使用其他协议如https，需要写出来
ftp(file transfer protocol)，文件传输协议，用来访问服务器上的文件的，例如ftp://ftp.itany.com/note/1 HTML.md
file，文件协议用来访问本地文件

主机名(hostname)，服务器的地址，例如上文网址chatgpt.com服务器地址

端口(port)，端口号码，出现在主机名后面，使用冒号隔开，端口号一般省略，不同协议使用不同端口号，http 80，ftp 21，https 443，这是默认端口号，不更改的话无需陈述
更改端口号需要陈述，例如https://chatgpt.com:443/c/67108032-4e18-8004-b3da-bf7fbd383b69

路径(path)：目标文件所在的路径结构，如https://www.baidu.com/web/html/images/bd_logol.png，路径为web/html/images/

资源(resource)：访问的目标文件bd_logol.png

查询字符串(query string)，也称参数，例如https://www.w3cschool.cn/courses?direction=0&tag=2123&type=0&condition=0&order=0
在我们请求的资源如course后面以?开头的一组名称和值，名称与值通过=连接，多个名称与值用&隔开，实际上为传参数
在浏览器搜索中，https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIKCAEQABixAxiABDIKCAIQABixAxiABDIKCAMQABixAxiABDIKCAQQABixAxiABDIKCAUQABixAxiABDIKCAYQABixAxiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTMyMjdqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8
里面有q,oq后面都是搜索的关键词，关键词更改，网址内容更改，在网址中更改关键词，会跳转关键词内容
百度是wd

锚点(anchor)：在资源后面使用#开头的文本，字符串和锚点可能都有，也可能只有一个，锚点连接到指定锚点
https://en.wikipedia.org/wiki/Java_(disambiguation)#Entertainment
查询Java跳转到锚点entertainment，#后面的锚点名称根据开发者的定义显示

身份认证(authentication)，访问需要密码，针对ftp://ftp.itany.com/note/1 HTML.md，不想输入账号密码，可以直接在网址输入
ftp://账户：密码@ftp.itany.com/note/1 HTML.md

"""