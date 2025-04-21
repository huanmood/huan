# [自动化测试]()

# [概况]()

* 本项目支持app ui自动化测试
* 本项目由以下工具组成
  * pytest：python的一个单元测试框架,https://docs.pytest.org/en/latest/
  * pytest-xdist：pytest的一个插件,可多进程同时执行测试用例,https://github.com/pytest-dev/pytest-xdist
  * allure-pytest：用于生成测试报告,http://allure.qatools.ru/
  * PyHamcrest：一个匹配器对象的框架，用于断言，https://github.com/hamcrest/PyHamcrest
  * requests：http请求框架,http://docs.python-requests.org/en/master/
  * Appium：移动端的自动化测试框架,https://github.com/appium/appium/tree/v1.15.1
  * Pillow：用于图片处理,https://pillow.readthedocs.io/en/latest/
  * PyMySQL：用于操作MySQL数据库,https://github.com/PyMySQL/PyMySQL
  * redis：redis客户端,https://pypi.org/project/redis/
  * python-binary-memcached：用于操作memcached，https://github.com/jaysonsantos/python-binary-memcached
* 当前仅支持Python>=3.6，建议安装Python V3.6.8版本

# [使用]()

## 一、环境准备

### 1、脚本运行环境准备

#### 1.1、安装系统依赖

* Linux-Ubuntu:
  * apt-get install libpq-dev python3-dev 【用于psycopg2-binary所需依赖】
  * apt-get install g++ libgraphicsmagick++1-dev libboost-python-dev 【用于pgmagick所需依赖】
  * apt-get install python-pgmagick 【pgmagick所需依赖】
* Linux-CentOS:
  * yum install python3-devel postgresql-devel 【用于psycopg2-binary所需依赖】
  * yum install GraphicsMagick-c++-devel boost boost-devel【用于pgmagick所需依赖】
* Windows:
  * 安装Microsoft Visual C++ 2019 Redistributable，下载地址：https://visualstudio.microsoft.com/zh-hans/downloads/ 【jpype1、图像识别字库所需依赖】

#### 1.2、安装python依赖模块

* pip3 install -r requirements.txt
* 安装pgmagick
  * Linux:
    * pip3 install pgmagick==0.7.6
  * Windows:
    * 下载安装对应版本：https://www.lfd.uci.edu/~gohlke/pythonlibs/#pgmagick
* 安装xmind-sdk-python
  * 下载地址:https://github.com/xmindltd/xmind-sdk-python

#### 1.3、安装allure

* 源安装
  * sudo apt-add-repository ppa:qameta/allure
  * sudo apt-get update 
  * sudo apt-get install allure
  * 其他安装方式：https://github.com/allure-framework/allure2
* 手动安装
  * 下载2.7.0版本:https://github.com/allure-framework/allure2/releases
  * 解压allure-2.7.0.zip
  * 加入系统环境变量:export PATH=/home/john/allure-2.7.0/bin:$PATH

#### 1.4、安装openjdk8或jdk8

* sudo add-apt-repository ppa:openjdk-r/ppa
* sudo apt-get update
* sudo apt-get install openjdk-8-jdk

#### 1.5、安装maven

* 完成maven的安装配置

#### 1.6、安装Oracle Instant Client

* Linux

  * 安装libaio包

    * Linux-CentOS:yum install libaio
    * Linux-Ubuntu:apt-get install libaio1

  * 配置Oracle Instant Client

    * 下载地址:http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

    * 下载安装包instantclient-basic-linux.x64-18.3.0.0.0dbru.zip

    * 解压zip包,并配置/etc/profile

      * unzip instantclient-basic-linux.x64-18.3.0.0.0dbru.zip
      * export LD_LIBRARY_PATH=/home/john/oracle_instant_client/instantclient_18_3:$LD_LIBRARY_PATH

    * 中文编码设置

      ```python 
      import os
      os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
      ```

* Windows

  * 下载地址:http://www.oracle.com/technetwork/topics/winx64soft-089540.html
  * 下载安装包instantclient-basic-windows.x64-11.2.0.4.0.zip
  * 解压zip包,并配置环境变量
    * 系统环境变量加入D:\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2
    * 配置中文编码,环境变量创建NLS_LANG=SIMPLIFIED CHINESE_CHINA.UTF8  
  * 注意:如果使用64位,python和instantclient都需要使用64位

#### 1.7、图像识别字库准备

* 下载对应字库:https://github.com/tesseract-ocr/tessdata

* 将下载的字库放到common/java/lib/tess4j/tessdata/

* Linux

  * 安装依赖

    * Linux-Ubuntu:sudo apt install pkg-config aclocal libtool automake libleptonica-dev
    * Linux-CentOS:yum install autoconf automake libtool libjpeg-devel libpng-devel libtiff-devel zlib-devel

  * 安装leptonica，下载leptonica-1.78.0.tar.gz，下载地址：https://github.com/DanBloomberg/leptonica/releases

    * 安装步骤同tesseract-ocr的安装
    * 修改/etc/profile添加如下内容，然后source

    ```
    export LD_LIBRARY_PATH=$LD_LIBRARY_PAYT:/usr/local/lib
    export LIBLEPT_HEADERSDIR=/usr/local/include
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    ```

  * 安装tesseract-ocr，下载tesseract-4.1.1.tar.gz，下载地址：https://github.com/tesseract-ocr/tesseract/releases

    * ./autogen.sh
    * ./configure
    * sudo make
    * sudo make install
    * sudo ldconfig

* Windows

  * 安装Microsoft Visual C++ 2019 Redistributable，下载地址：https://visualstudio.microsoft.com/zh-hans/downloads/

### 2、appium server运行环境准备

#### 2.1、安装jdk1.8,并配置环境变量

* export JAVA_HOME=/usr/lib/jvm/jdk8
* export JRE_HOME=${JAVA_HOME}/jre 
* export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
* export PATH=${JAVA_HOME}/bin:$PATH

#### 2.2、安装配置appium server

* 安装appium desktop server
  * 下载Appium-windows-1.15.1.exe
  * 下载地址:https://github.com/appium/appium-desktop/releases
  * 以管理员身份启动服务

* Android环境准备
  * 安装java(JDK),并配置JAVA_HOME=/usr/lib/jvm/jdk8
  * 安装Android SDK,并配置ANDROID_HOME="/usr/local/adt/sdk"
  * 使用SDK manager安装需要进行自动化的Android API版本

* IOS环境准备
  * 由于测试IOS真实设备没办法直接操作web view，需要通过usb，实现通过usb创建连接需要安装ios-webkit-debug-proxy
  * 下载安装地址：https://github.com/google/ios-webkit-debug-proxy/tree/v1.8.5

* 手机chrome环境准备
  * 确保手机已安装chrome浏览器
  * 下载chrome浏览器驱动：https://chromedriver.storage.googleapis.com/index.html
  * 驱动支持的最低浏览器版本：https://raw.githubusercontent.com/appium/appium-chromedriver/master/config/mapping.json
  * 在appium desktop上设置驱动的路径

* 混合应用环境准备
  * 方法一：安装TBS Studio工具查看webview内核版本：https://x5.tencent.com/tbs/guide/debug/season1.html
  * 方法二：打开地址（该地址在uc开发工具中可查到）查看webview内核版本：https://liulanmi.com/labs/core.html
  * 下载webview内核对应的chromedriver版本：https://chromedriver.storage.googleapis.com/index.html
  * 配置文件进行驱动路径的配置
  * 注：webview需要开启debug模式

* Windows环境准备
  * 支持Windows10及以上版本
  * 设置Windows处于开发者模式
  * 下载WinAppDriver并安装(V1.1版本),https://github.com/Microsoft/WinAppDriver/releases
  * \[可选\]下载安装WindowsSDK,在Windows Kits\10\bin\10.0.17763.0\x64内包含有inspect.exe用于定位Windows程序的元素信息

* 其他更多配置：https://github.com/appium/appium/tree/v1.15.1/docs/en/drivers

## 二、修改配置

* config/data.json 配置参数化测试信息
* config/android_caps.yaml 配置安卓测试环境信息
* config/ios_caps.yaml 配置苹果测试环境信息
* config/email.cfg 配置邮箱信息

## 三、运行测试

* TestCase目录下，运行py文件为单元测试。
* 运行run_main.py为集成测试，会运行所有符合条件的测试用例。
  * add_case方法可自定义运行的测试用例。


## 四、生成测试报告

```
运行run_main.py，会自动生成测试报告
```

## 五、项目说明

### app ui测试

* 元素的显式等待时间默认为15s
* 封装的显式等待类型支持：Page/BasePage.py/WebDriverWait(self.driver, 15)
* 项目
  * TestDemoAndroid 例子项目

# [项目结构]()

* app　测试对象
* common　基础方法类
* config　配置文件
* logs　日志目录
* page　页面对象封装
  * init　元素地址初始化
  * BasePage　封装公用方法类
* reports　测试报告输出目录
* screenshots　截图输出目录
* TestCase　存放测试用例
* README.md　项目说明
* run_main.py　运行测试主脚本

# [编码规范]()

* 统一使用python 3.8
* 编码使用-\*- coding:utf8 -\*-,且不指定解释器
* 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
* 局部代码注释使用#号
* 所有中文都直接使用字符串，不转换成Unicode，即不是用【u'中文'】编写
* 所有的测试模块文件都以test_projectName_moduleName.py命名
* 所有的测试类都以Test开头，类中方法(用例)都以test_开头
* 每一个模块中测试用例如果有顺序要求【主要针对ui自动化测试】，则自上而下排序，pytest在单个模块里会自上而下按顺序执行

# [注意点]()

* app ui测试
  * 能用id、name、link(不常变化的链接)定位的，不使用css定位，能使用css定位，不使用xpath定位
  * 如需要上传文件到手机或者从手机下载文件，请确保有手机对应目录的读写权限
  * 视频录制统一对单个单个case进行，保证录制时间不超过3分钟，且录制文件不要过大，否则会引起手机内存无法存储视频
        * 确认手机是否能进行视频录制执行命令adb shell screenrecord /sdcard/test.mp4，能正常执行即可
  * 设备屏幕坐标系原点都在最左上角，往右x轴递增，往下y轴递增
