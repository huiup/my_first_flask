务必使用pycharm打开本项目文件，还需pip安装pymysql和flask三方库。
（使用数据库时，请注意连接参数是否正确）

static：存放网页中使用的css、js、img的文件

templates：运行于flask的网页模板文件，运行启动程序后打开才能展示完整的html网页。

venv：虚拟环境

app.py：flask启动程序

utils.py：从数据库中获取交互的数据

若环境配置无误后，直接运行app.py程序启动整个项目，之后在程序运行窗口点击http://127.0.0.1:5000/ 或在浏览器输入localhost:5000就能够访问到可视化网页。若打开的网页出现格式错乱等问题，请检查链接static中文件的url是否正确。
