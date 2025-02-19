class nelko_buttonElement():
    def __init__(cls):
        # *****************************************************************************************************************************************************
        # 编辑器：清除所有元素
        cls.editor_clear = ['XPATH',
                            '//android.widget.LinearLayout[@resource-id="com.labelnize.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
        # *****************************************************************************************************************************************************
        # 编辑器：添加文本按钮
        cls.editor_textBtn = ['XPATH',
                              '(//android.widget.ImageView[@resource-id="com.labelnize.printer:id/item_menu_icon_img"])[1]']
        # 首页：右上角连接
        cls.Homepage_connect = '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]'
        # 首页：我的模板
        cls.Homepage_myTemplate=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_tab_title" and @text="我的模板"]']
        # *****************************************************************************************************************************************************
        # 连接页面：
        # 返回
        cls.connectPage_back = ['XPATH', '//android.widget.ImageView[@resource-id="com.labelnize.printer:id/iv_back"]']
        # 刷新
        cls.connectPage_refresh = ['XPATH', '//android.widget.TextView[@text="刷新"]']
        # 取消连接
        cls.connectPage_disconnect = ['XPATH','//android.widget.TextView[@resource-id="com.labelnize.printer:id/act_two_inch_bt_disconnect_tv"]']
        # 请尝试通过 BLE 搜索连接：连接失败（P21、P31S）晶振问题
        cls.connectPage_connectFail = ['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]']
        # 是否切换BLE连接的确认按钮
        cls.connectPage_sure = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']
        # 断开连接
        cls.connectPage_disconnect = ['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/act_two_inch_bt_disconnect_tv"]']
        #顶部排序连接
        cls.connectPage_title=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]']
        # *****************************************************************************************************************************************************
        cls.Homepage_connectTitle = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]']
        cls.Homepage_Homepage=['XPATH','//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_home_home_btn"]/android.widget.ImageView']
        # 连接页面：使用时允许
        cls.connectPage_Allow_in_use = ['XPATH','//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]']

        #
        cls.deviceName_text = ['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_printer_model"]']
        #

        #
        cls.accredit = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']

        # *****************************************************************************************************************************************************
        # 首次下载获取权限页面：
        # 用户协议和隐私政策
        cls.firstDownload_UserAgreementPrivacyPolicy = ['XPATH',
                                                        '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_title"]']
        # 同意
        cls.firstDownload_sure = ['XPATH',
                                  '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_confirm"]']
        # 稍后连接
        cls.firstDownload_afterConnect = ['XPATH',
                                          '//android.widget.TextView[@resource-id="com.nelko.printer:id/connect_later_tv"]']
        # 选择机型处的确认
        cls.firstDownload_confirm = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ok"]']
        # 首次下载获取权限页面：跳过
        cls.firstDownload_skip = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_right"]']
        # *****************************************************************************************************************************************************
        # 首页教程
        cls.Tutorials_connectDevices = ['XPATH',
                                        '//android.widget.TextView[@resource-id="com.nelko.printer:id/text_view"]']  # 点击连接打印机
        cls.Tutorials_Ikonw = ['XPATH',
                               '//android.widget.Button[@resource-id="com.nelko.printer:id/hint_more_btn_ok"]']  # 点击连接打印机 下的‘我知道了’
        # *****************************************************************************************************************************************************
        cls.MyPage_my=['XPATH','//android.widget.LinearLayout[@resource-id="com.nelko.printer:id/act_home_mine_btn"]/android.widget.ImageView']
        cls.MyPage_login=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/text_user_name"]']
        cls.MyPage_email=['XPATH','//android.widget.AutoCompleteTextView[@resource-id="com.nelko.printer:id/edit_email"]']
        cls.MyPage_password=['XPATH','//android.widget.EditText[@resource-id="com.nelko.printer:id/edit_password"]']
        cls.MyPage_agree=['XPATH','//android.widget.CheckBox[@resource-id="com.nelko.printer:id/checkBox_agreement"]']
        cls.MyPage_loginButton=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/sign_in"]']
        cls.MyPage_Cloud_sync=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_message"]']
        cls.MyPage_open=['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']
# *****************************************************************************************************************************************************
class labelnize_buttonElement():
    def __init__(cls):
        # *****************************************************************************************************************************************************
        # 编辑器：清除所有元素
        cls.editor_clear = ['XPATH',
                            '//android.widget.LinearLayout[@resource-id="com.labelnize.printer:id/act_edit_action_clear_btn"]/android.widget.ImageView']
        # *****************************************************************************************************************************************************
        # 编辑器：添加文本按钮
        cls.editor_textBtn = ['XPATH',
                              '(//android.widget.ImageView[@resource-id="com.labelnize.printer:id/item_menu_icon_img"])[1]']
        # 首页：右上角连接
        cls.Homepage_connectPage_connect = ['XPATH','//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_connect"]']
        # *****************************************************************************************************************************************************
        # 连接页面：
        # 返回
        cls.connectPage_back = ['XPATH', '//android.widget.ImageView[@resource-id="com.labelnize.printer:id/iv_back"]']
        # 刷新
        cls.connectPage_refresh = ['XPATH', '//android.widget.TextView[@text="刷新"]']
        # 取消连接
        cls.connectPage_disconnect = ['XPATH',
                                      '//android.widget.TextView[@resource-id="com.labelnize.printer:id/act_two_inch_bt_disconnect_tv"]']
        # 请尝试通过 BLE 搜索连接：连接失败（P21、P31S）晶振问题
        cls.connectPage_connectFail = '//android.widget.TextView[@resource-id="com.labelnize.printer:id/tv_message"]'
        # 是否切换BLE连接的确认按钮
        cls.connectPage_sure = ['XPATH', '//android.widget.TextView[@resource-id="com.labelnize.printer:id/tv_sure"]']
        # 断开连接
        cls.connectPage_disconnect = ['XPATH',
                                      '//android.widget.TextView[@resource-id="com.nelko.printer:id/act_two_inch_bt_disconnect_tv"]']
        # 顶部排序连接
        cls.connectPage_title = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]']
        # *****************************************************************************************************************************************************
        cls.Homepage_connectTitle = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_title"]']
        # 连接页面：使用时允许
        cls.connectPage_Allow_in_use = ['XPATH', '']

        #
        cls.deviceName_text = ['XPATH',
                               '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_printer_model"]']

        #
        cls.accredit = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_sure"]']

        # *****************************************************************************************************************************************************
        # 首次下载获取权限页面：
        # 用户协议和隐私政策
        cls.firstDownload_UserAgreementPrivacyPolicy = ['XPATH',
                                                        '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_title"]']
        # 同意
        cls.firstDownload_sure = ['XPATH',
                                  '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ui_confirm"]']
        # 稍后连接
        cls.firstDownload_afterConnect = ['XPATH',
                                          '//android.widget.TextView[@resource-id="com.nelko.printer:id/connect_later_tv"]']
        # 选择机型处的确认
        cls.firstDownload_confirm = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_ok"]']
        # 首次下载获取权限页面：跳过
        cls.firstDownload_skip = ['XPATH', '//android.widget.TextView[@resource-id="com.nelko.printer:id/tv_right"]']
        # *****************************************************************************************************************************************************
        # 首页教程
        cls.Tutorials_connectDevices = ['XPATH',
                                        '//android.widget.TextView[@resource-id="com.nelko.printer:id/text_view"]']  # 点击连接打印机
        cls.Tutorials_Ikonw = ['XPATH',
                               '//android.widget.Button[@resource-id="com.nelko.printer:id/hint_more_btn_ok"]']  # 点击连接打印机 下的‘我知道了’
