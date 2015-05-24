概述：	本程序用作在固定网站框架内添加app
	 共有tornado，框架，app定义，app解释四个部分组成,
	
	tornado：	负责http相应
	框架：		是网站的基本结构
	app定义包含：	viewer试图定义app的菜单，action
		     	数据模型python，url
	app解释程序：	负责处理app定义，根据模版文件和app定义的viewer视图文件生成html文件
程序运作流程：
	1.start读取配置文件，app目录，app名称，app应用
	2.start扫描App目录
	3.读取viewer文件，读取model文件生成index，appmodel等页面视图
	4.读取数据模型，修改www文件
	5.运行www
网站框架：

div contain
	div top
		div logo
		div top-nav	（对象）
				ul
				li
		div users
	div body
		div left
			div left-nav（对象）
				span
				ul
				li
		div right-mini-nav（对象）
			span
		div right
			div right-nav
				form right-nav（对象）
					
					
			div right-content（对象）
				
	div buttom

left-nav,right-nav,rhght-content响应由jquery 请求
viewer文件：
	语法：
	    
	    对象类名:
		element:{(value:$value)(element:$element,name:$name)}
例：
(
left-nav,(
	span,({value:请假单}),
	ul,({li:li1},{li:li2},{id:ul-qingjiadan}),
	li1,({element:a},{name:a1}),
	a1,({href:#},{value:事假}),
	li2,({element:a},{name:a2}),
	a2,({href:#},{value:调休}),
	),
)
解释器：
	对象类：
	top-nav,left-nav,right-mini-nav,right-nav,right-content
	对象定义文件：style-element.py	
	
