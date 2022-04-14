from selenium.common.exceptions import SessionNotCreatedException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import wx
import random
from threading import *
#import atexit
#import re
import keyboard
from tkinter import Tk
import mouse
import tkinter.messagebox as tmb
from wx.lib.embeddedimage import PyEmbeddedImage


#############################
appVersion = "0.35"
AppIcon = PyEmbeddedImage("""
    iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAD30lEQVR42u2aP0wTURzHGSDRAQkOAsGFoAMMaMJkjO39qSVKIokuGgfoXdug4MBA37t3NVx6h8of2TvBAMRFFwZw1xDCBCuSymaDC4MIgYC/ayMRw597R/vuCu+SXyhw1+v3837v969XVubjQ+pMNkqq3isp+rSs6MuSQjbA9sD2ZYVsw88M/O+zpBILfhcFwygvK/WjNR6vkFW9E8Qt2EJpTFa0LIAYFqKJ6yUpPhRNPgYhq7TCj7AtsNEHz40rJSG8/QWuBjf+WADhhz1CJWv3I1rQ76veVKBVP9pUsgPboseX4sUUugVBbr1o4g+B0JO+Eh82kw2iibJMxB8EyaQ/POFOX99l0cRLgon2WQKwtwN4QsB71zfRmC2eOYA8hLVHSqLS030vWGjXMwD5eDDiGQDBxDN/xXsGwK4TuvV65uLlN1ozrP6eGwCQ0+fBfVEoqndISjIsKVoMyuNJsF/uagR9iL37W+j9v+IdAVDJN6gVhGOzSffANThnih6ClmXeO4D7f6cBAAXMol0lOmqcIM/TQjgJbMGPgNl/83/xJwKAAqktTuqouscIpSdAF8kMQNDqf0YFQCGvqGNMlNTAdZvOCyMyx9L9DQoAv93makovyDAMgDjtGIBKvrgeoijJGIUHbLPzAAuPUwCYcg8Ah2niAMstMOEUAOToiTO018KFBgCBsCU3J3Ro5w6Abw8OgAPgAM4ngNA7VJUXd4pZaIWiElyxIZxmoTiq8n5lh43ao4Q5tbMMNh6+NGo5AA6AA+AAOAAOgAPgADgAXgrzZogD4AA4AA7A1QebdWryIGk5hwBo8jYWLjQAycRht/cRzcQ0RR0wzgyAaKJtpwCCJoqd4T5fHXuAQtLsPMBCGcdeYOFJN/e4O5SohOu3KDxggCWAOYptsAmBsIb2HpKJXtH0ArJKnrLMAhZNHIBtQPXV9b1BUgfX/aQBIKj4BksAAm0HBwHttZP3bn+Lq+H8RcpukN1TGzkAhlFuP7TsAsL0SdshB9bCK7TtMATAUeZVmmihIZf9/CbAm5JMLWanSHifDtHEGvx93uU8YE+OaM3MAUiWXn9clC62HV59fca7Wt1CIx4D2LWf7vAMgJ2rwZ3XPAOgkjHPOzbJQgH4UDseAFgSuoxLPmlbUQ9TABEtG44mG3zWuyd0RgDWhS5y26cDjJwnFG07QMpcDZiJJl9PceyYECxGYEyhT21G39WSGGXlOrl8itwqxKqLFn5SkjM9u1gSU3bFiH+4EL4gpHBXazpdUfrDTegd8g2U3UXiWXDnzMFQxUJ7sGU24PUyBNIP0Av0SmZ/o5/1/AGhykTVJBDRTgAAAABJRU5ErkJggg==
""")

# Define notification event for thread completion
EVT_RESULT_ID = wx.NewIdRef()
EVT_RESULT_ID2 = wx.NewIdRef()
EVT_RESULT_ID3 = wx.NewIdRef()

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

#############################

def ChangeToDeepl(event):
    browser.stop_client()
    browser.get('https://www.deepl.com/translator#en/zh/')

def deepl(rawText):
    inputArea = browser.find_element_by_class_name('lmt__textarea.lmt__source_textarea.lmt__textarea_base_style')
    inputArea.clear()
    inputArea.send_keys(rawText)
    time.sleep(random.uniform(3,5))
    cookedText = browser.find_element_by_id('target-dummydiv').get_attribute('innerHTML').strip('\r\n')
    return cookedText

def ChangeToYoudao(event):
    browser.stop_client()
    browser.get('https://fanyi.youdao.com')

def youdao(rawText):
    #WebDriverWait(browser, 10).until(lambda broswer: not browser.find_element_by_xpath(xpath))
    xpath = '//div[@id=\'transTarget\']/p[1]/span'
    inputArea = browser.find_element_by_id('inputOriginal')
    try:
        browser.find_element_by_id('inputDelete').click()
    except:
        pass
    #inputArea.clear()
    #WebDriverWait(browser, 10).until_not(lambda broswer: browser.find_element_by_xpath(xpath))
    inputArea.send_keys(rawText)
    #time.sleep(random.uniform(2,3))
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_xpath(xpath))
    if ' ' in rawText:
        text = browser.find_elements_by_xpath(xpath)
        joinedtext = ''
        for index in range(len(text)):
            joinedtext += text[index].text
        return joinedtext
    else:
        try:
            WebDriverWait(browser, 1).until(lambda broswer: browser.find_element_by_class_name('dict__relative'))
            dictionaryComment = browser.find_element_by_class_name('dict__relative').text
            cookedText = '【词典】\n' + dictionaryComment
        except:
            cookedText = browser.find_elements_by_xpath(xpath)[0].text
        return cookedText

def ChangeToCaiyun(event):
    browser.stop_client()
    browser.get('https://fanyi.caiyunapp.com/')

def caiyun(rawText):
    inputArea = browser.find_element_by_class_name('textinput')
    #inputArea.clear()
    try:
        browser.find_element_by_class_name('text-delete').click()
    except:
        pass
    inputArea.send_keys(rawText)
    xpath = '//div[@id=\'texttarget\']/p[1]/span'
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_xpath(xpath))
    if ' ' in rawText:
        cookedText = browser.find_element_by_xpath(xpath).text
    else:
        try:
            WebDriverWait(browser, 1).until(lambda broswer: browser.find_element_by_class_name('dictionary-box'))
            cookedText = browser.find_element_by_class_name('dictionary-box').text.replace(';', '；')
        except:
            cookedText = browser.find_element_by_xpath(xpath).text
    return cookedText

def ChangeToGoogle(event):
    browser.stop_client()
    browser.get('https://translate.google.cn/')

def google(rawText):
    inputArea = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
    #inputArea.clear()
    try:
        browser.find_element_by_class_name('VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.qiN4Vb.GA2I6e').click()
    except:
        pass
    inputArea.send_keys(rawText)
    #time.sleep(random.uniform(3,4))
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_class_name('VIiyi'))
    cookedText = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[3]').get_attribute('data-text')
    return cookedText

def ChangeToBaidu(event):
    browser.stop_client()
    browser.get('https://fanyi.baidu.com/')

def baidu(rawText):
    inputArea = browser.find_element_by_id('baidu_translate_input')
    #inputArea.clear()
    try:
        browser.find_element_by_class_name('textarea-clear-btn').click()
    except:
        pass
    inputArea.send_keys(rawText)
    #time.sleep(random.uniform(2,3))
    #xpath = '//div[@id=\'output-bd\']'
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_class_name('ordinary-output.target-output.clearfix'))
    if ' ' in rawText:
        textelementlist = browser.find_elements_by_class_name('ordinary-output.target-output.clearfix')
        textlist = []
        for i in textelementlist:
            textlist.append(i.text)
        cookedText = ''.join(textlist)
        #cookedtext = re.sub(r'<(.+?)>', '', halfcookedtext)
        return cookedText
    else:
        try:
            WebDriverWait(browser, 2).until(lambda broswer: browser.find_element_by_class_name('dictionary-output'))
            cookedText = ""
            dictionaryComment = browser.find_element_by_class_name('dictionary-comment').text.replace('.\n', '.').replace(';', '；')
            dictionaryPronunciations = browser.find_elements_by_class_name('phonetic-transcription')
            dictionaryAEPronunciation = dictionaryPronunciations[-1].text.replace('美', '【美式发音】\n')
            cookedText = dictionaryAEPronunciation + '\n\n【词典】\n' + dictionaryComment
        except:
            cookedText = browser.find_element_by_class_name('ordinary-output.target-output.clearfix').text
        return cookedText

def ChangeToSogou(event):
    browser.stop_client()
    browser.get('https://fanyi.sogou.com/text?keyword=&transfrom=auto&transto=zh-CHS&model=medical&fr=default')

def sogou(rawText):
    inputArea = browser.find_element_by_id('trans-input')
    try:
        browser.find_elements_by_class_name('btn-clear')[0].click()
    except:
        pass
    #inputArea.clear()
    inputArea.send_keys(rawText)
    #time.sleep(random.uniform(2,3))
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_id('trans-result'))
    if ' ' in rawText:
        cookedText = browser.find_element_by_id('trans-result').get_attribute('innerHTML')
    else:
        try:
            WebDriverWait(browser, 2).until(lambda broswer: browser.find_element_by_class_name('item-wrap'))
            cookedText = browser.find_element_by_class_name('item-wrap').text.replace('.\n', '.')
        except:
            cookedText = browser.find_element_by_id('trans-result').get_attribute('innerHTML')
    return cookedText

def ChangeToTencent(event):
    browser.stop_client()
    browser.get('https://fanyi.qq.com/')

def tencent(rawText):
    inputArea = browser.find_element_by_class_name('textinput')
    try:
        browser.find_element_by_class_name('textpanel-tool.tool-close').click()
    except:
        pass
    #inputArea.clear()
    inputArea.send_keys(rawText)
    #time.sleep(random.uniform(2,3))
    WebDriverWait(browser, 10).until(lambda broswer: browser.find_element_by_class_name('text-dst'))
    cookedTextList = browser.find_elements_by_class_name('text-dst')
    cookedText = ''
    for i in cookedTextList:
        cookedText += i.get_attribute('innerHTML')
    return cookedText


def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data

# Thread class that executes processing
class WorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window, rawText, app):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self._rawText = rawText #传递进进程？
        self._cookedText = ''
        self._app = app
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        """Run Worker Thread."""
        if self._app == 'deepl':
            self._cookedText = deepl(self._rawText)
        elif self._app == 'baidu':
            self._cookedText = baidu(self._rawText)
        elif self._app == 'youdao':
            self._cookedText = youdao(self._rawText)        
        elif self._app == 'google':
            self._cookedText = google(self._rawText)        
        elif self._app == 'caiyun':
            self._cookedText = caiyun(self._rawText)
        elif self._app == 'sogou':
            self._cookedText = sogou(self._rawText)
        elif self._app == 'tencent':
            self._cookedText = tencent(self._rawText)
        wx.PostEvent(self._notify_window, ResultEvent(self._cookedText))

    def abort(self):
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1

def EVT_RESULT2(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID2, func)

class ResultEvent2(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID2)
        self.data = data

class KbListener(Thread):
    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        self.Run = True
        self.appClose = False
        Thread.__init__(self)        
        self._notify_window = notify_window
        self.start()


    def run(self):
        keyboard.wait('ctrl')
        keyboard.press_and_release('ctrl+c')

        while not self.appClose:
            if self.Run:
                wx.PostEvent(self._notify_window, ResultEvent2(Tk().clipboard_get()))
                keyboard.wait('ctrl')
                keyboard.press_and_release('ctrl+c')
            else:
                keyboard.wait('ctrl')


def EVT_RESULT3(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID3, func)

class ResultEvent3(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID3)
        self.data = data

class MouseListener(Thread):
    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        self.appClose = False
        self.Run = True
        Thread.__init__(self)
        self._notify_window = notify_window
        self.start()

    def run(self):
        mouse.wait(button='left', target_types='down')
        #print('down')
        tempPosition = mouse.get_position()
        mouse.wait(button='left', target_types='up')
        #print('up')
        while not self.appClose:
            if self.Run:
                if tempPosition != mouse.get_position():
                    #print('drag')
                    keyboard.press_and_release('ctrl+c')
                    #print('copy')
                    try:
                        wx.PostEvent(self._notify_window, ResultEvent2(Tk().clipboard_get()))
                    except:
                        pass    
                    #print('send')
                    mouse.wait(button='left', target_types='down')
                    #print('down')
                    tempPosition = mouse.get_position()
                    mouse.wait(button='left', target_types='up')
                    #print('up')
                else:
                    #print('press')
                    mouse.wait(button='left', target_types='down')
                    #print('down')
                    tempPosition = mouse.get_position()
                    mouse.wait(button='left', target_types='up')
                    #print('up')
            else:
                mouse.wait(button='left', target_types='down')
                tempPosition = mouse.get_position()
                mouse.wait(button='left', target_types='up')
               



# GUI Frame class that spins off the worker thread
class MainFrame(wx.Frame):
    """Class MainFrame."""
    def __init__(self, parent, id):
        """Create the MainFrame."""
        wx.Frame.__init__(self, parent, id, 'Ftranslator v{}'.format(appVersion), size=(600, 400))

        self.SetIcon(AppIcon.GetIcon())

        self.menubar = wx.MenuBar()
        self.helpMenu = wx.Menu()
        self.onTop = wx.MenuItem(self.helpMenu, wx.ID_ANY, '置顶', kind = wx.ITEM_CHECK)
        self.helpMenu.Append(self.onTop)
        self.helpMenu.AppendSeparator()
        self.aboutm = self.helpMenu.Append(wx.ID_ABOUT, '关于')
        self.Bind(wx.EVT_MENU, self.ToggleTop, self.onTop)
        self.Bind(wx.EVT_MENU, self.aboutw, self.aboutm)
        self.menubar.Append(self.helpMenu, '菜单')

        self.appMenu = wx.Menu()
        self.YOUDAO = self.appMenu.Append(wx.ID_ANY, '有道', kind = wx.ITEM_RADIO)
        self.DEEPL = self.appMenu.Append(wx.ID_ANY, 'DeepL', kind = wx.ITEM_RADIO)
        self.BAIDU = self.appMenu.Append(wx.ID_ANY, '百度', kind = wx.ITEM_RADIO)
        self.GOOGLE = self.appMenu.Append(wx.ID_ANY, 'Google', kind = wx.ITEM_RADIO)
        self.CAIYUN = self.appMenu.Append(wx.ID_ANY, '彩云', kind = wx.ITEM_RADIO)
        self.SOGOU = self.appMenu.Append(wx.ID_ANY, '搜狗（生物医学）', kind = wx.ITEM_RADIO)
        self.TENCENT = self.appMenu.Append(wx.ID_ANY, '腾讯', kind = wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, ChangeToDeepl, self.DEEPL)
        self.Bind(wx.EVT_MENU, ChangeToYoudao, self.YOUDAO)
        self.Bind(wx.EVT_MENU, ChangeToBaidu, self.BAIDU)
        self.Bind(wx.EVT_MENU, ChangeToGoogle, self.GOOGLE)
        self.Bind(wx.EVT_MENU, ChangeToCaiyun, self.CAIYUN)
        self.Bind(wx.EVT_MENU, ChangeToSogou, self.SOGOU)
        self.Bind(wx.EVT_MENU, ChangeToTencent, self.TENCENT)
        self.menubar.Append(self.appMenu, '翻译引擎')

        self.modeMenu = wx.Menu()
        self.MANUAL = self.modeMenu.Append(wx.ID_ANY, '手动', kind = wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onMenual, self.MANUAL)
        self.kb = self.modeMenu.Append(wx.ID_ANY, '按键（CTRL）', kind = wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onKb, self.kb)
        self.ms = self.modeMenu.Append(wx.ID_ANY, '划选', kind = wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onMouse, self.ms)
        self.menubar.Append(self.modeMenu, '模式')


        self.SetMenuBar(self.menubar)


        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hint = wx.StaticText(panel, label='原文')
        hbox1.Add(self.hint, flag=wx.EXPAND, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.inputbox = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        hbox2.Add(self.inputbox, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 15))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.result = wx.StaticText(panel, label='译文')
        hbox3.Add(self.result)
        vbox.Add(hbox3, flag=wx.LEFT, border=10)

        vbox.Add((-1, 10))
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.inputbox2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        font1 = wx.Font(12, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL, False, u'Microsoft YaHei')
        self.inputbox2.SetFont(font1)
        hbox4.Add(self.inputbox2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox4, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 15))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btnRun = wx.Button(panel, label='翻译', size=(90, 30))
        btnRun.Bind(wx.EVT_BUTTON, self.OnTextChange)
        hbox5.Add(btnRun)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        

        panel.SetSizer(vbox)

        # Set up event handler for any worker thread results
        EVT_RESULT(self,self.OnResult)
        EVT_RESULT2(self,self.OnResult2)
        EVT_RESULT3(self,self.OnResult3)

        # And indicate we don't have a worker thread yet
        self.worker = None
        self.worker2 = None
        self.worker3 = None

    def aboutw(self, e):
        dialog = wx.Dialog(self, title='关于', size=(500, 180))
        dialog.Centre()
        panel = wx.Panel(dialog)
        sizer = wx.GridSizer(5, 1, 0, 0)
        label_0 = wx.StaticText(panel,  label='版本：v{}'.format(appVersion))
        label_1 = wx.StaticText(panel,  label='')
        label_2 = wx.StaticText(panel, label='Made by Koshiro | Powered by Python')
        #btnIndex = wx.Button(panel, id=wx.ID_ANY, label='项目主页', size=(70, 30))
        #btnIndex.Bind(wx.EVT_MOUSE_EVENTS, self.OnClick)
        btnOK = wx.Button(panel, id=wx.ID_OK, label='关闭', size=(90, 30))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #hbox.Add(btnIndex, flag=wx.RIGHT | wx.BOTTOM, border = 10)
        hbox.Add(btnOK, flag=wx.LEFT | wx.BOTTOM, border=10)
        sizer.Add(label_0, flag=wx.ALIGN_CENTER | wx.UP, border=20)
        sizer.Add(label_1, flag=wx.ALIGN_CENTER | wx.UP, border=20)
        sizer.Add(label_2, flag=wx.ALIGN_CENTER | wx.UP, border=20)
        sizer.Add((-1,30))
        sizer.Add(hbox, flag=wx.ALIGN_CENTER)
        panel.SetSizer(sizer)
        dialog.ShowModal()
    
    '''
    def changetodeepl(self, event):
        ChangeToDeepl(event)
        self.OnTextChange(event)
    
    def changetobaidu(self, event):
        ChangeToBaidu(event)
        self.OnTextChange(event)
    
    def changetogoogle(self, event):
        ChangeToGoogle(event)
        self.OnTextChange(event)

    def changetocaiyun(self, event):
        ChangeToCaiyun(event)
        self.OnTextChange(event)

    def changetoyoudao(self, event):
        ChangeToYoudao(event)
        self.OnTextChange(event)
    '''
    
    def OnTextChange(self, event):
        self.inputbox2.Value = ''
        """Start Computation."""
        if self.DEEPL.IsChecked():
            self.app = 'deepl'
        elif self.BAIDU.IsChecked():
            self.app = 'baidu'
        elif self.YOUDAO.IsChecked():
            self.app = 'youdao'
        elif self.GOOGLE.IsChecked():
            self.app = 'google'
        elif self.CAIYUN.IsChecked():
            self.app = 'caiyun'
        elif self.SOGOU.IsChecked():
            self.app = 'sogou'
        elif self.TENCENT.IsChecked():
            self.app = 'tencent'
        rawText = self.inputbox.GetValue().replace('\n', ' ').replace('  ', ' ').strip()
        self.inputbox.Value = rawText
        self.worker = WorkerThread(self, rawText=rawText, app=self.app)
        #self.worker.join()


    def OnResult(self, event):
        """Show Result status."""
        self.inputbox2.Value = event.data
        self.worker = None

    def ToggleTop(self, event):
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
    
    def onMenual(self, event):
        if self.worker2 != None:
            self.worker2.Run = False
        if self.worker3 != None:
            self.worker3.Run = False
    
    def onKb(self, event):
        if self.worker3 != None:
            self.worker3.Run = False
        if self.worker2 == None:
            self.worker2 = KbListener(self)
        else:
            self.worker2.Run = True

    def OnResult2(self, event):
        self.inputbox.Value = event.data
        self.OnTextChange(event)
    
    def onMouse(self, event):
        if self.worker2 != None:
            self.worker2.Run = False
        if self.worker3 == None:
            self.worker3 = MouseListener(self)
        else:
            self.worker3.Run = True
            
    def OnResult3(self, event):
        self.inputbox.Value = event.data
        self.OnTextChange(event)



class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True



#####################



if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(r'chromedriver.exe', options=options)
    except SessionNotCreatedException as err:
        tmb.showinfo('chromedriver错误','chromedriver版本不对，请到http://npm.taobao.org/mirrors/chromedriver/ 下载对应版本（Chrome版本信息如下）\n{}'.format(err))
        #print('\nchromedriver版本不对，请到http://npm.taobao.org/mirrors/chromedriver/ 下载对应版本（Chrome版本信息如下）\n', err)
        quit()
        
        
    browser.get('https://fanyi.youdao.com')
    app = MainApp(0)
    app.MainLoop()
    browser.quit()
    browser.stop_client()
    #print("exiting")
    if app.frame.worker2 != None:
        app.frame.worker2.appClose = True
        app.frame.worker2.join(0.1)
        #print("worker2 stopped?")
    if app.frame.worker3 != None:
        app.frame.worker3.appClose = True
        app.frame.worker3.join(0.1)
        #print("worker3 stopped?")


    quit()
    '''
    @atexit.register
    def closeBrowser():
        browser.quit()
        browser.stop_client()
        print('exiting')
        quit()
    '''
### todos: save config; more key support; time select; changing engine then change translation; more engines; word translation; using request
