import time
from DrissionPage import ChromiumPage, ChromiumOptions

page = ChromiumPage(ChromiumOptions().set_browser_path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))

#page.get("https://cn.bing.com/search?pglt=2339&q=%E5%88%98%E4%BA%A6%E8%8F%B2&cvid=acbfac59e42b412e9a8b95ca36afa020&gs_lcrp=EgRlZGdlKgYIABAAGEAyBggAEAAYQDIGCAEQLhhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEAyBggJEAAYQNIBCDI0MzJqMGo3qAIIsAIB&FORM=ANSPA1&PC=U531")
#这个网址是直接搜的刘亦菲

page.get("https://www.baidu.com")

textarea = page.ele("#chat-submit-button")

textarea.input('章若楠')

bouuton = page.ele('#chat-submit-button')
bouuton.click()

time.sleep(2)

page.ele('xpath://div[@id="s_tab_inner"]/a[2]').click()

for i in range(1):
    time.sleep(2)
    page.scroll.to_bottom()

imgs = page.eles('xpath://div[@class="image-m9T9I img-hFPj_"]//img')
for img in imgs:
    img.save('章若楠')
