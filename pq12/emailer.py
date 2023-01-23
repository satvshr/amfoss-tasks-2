import sys, time
def mailsend():
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get('https://www.mail.com/#.23140-header-navlogin2-1')
    userElem = browser.find_element_by_name('username')
    userElem.send_keys(email)
    passwordElem = browser.find_element_by_name('password')
    passwordElem.send_keys(password)
    passwordElem.submit()
    time.sleep(10)
    compose = browser.find_element_by_partial_link_text('E-mail')
    compose.click()
    time.sleep(5)
    composefinal = browser.find_element_by_id('id5')
    composefinal.click()
    time.sleep(10)
    messageElem = browser.find_element_by_id('cke_editor')
    messageElem.send_keys(message)

if len(sys.argv) > 4:
    email = sys.argv[1]
    password = sys.argv[2]
    message = sys.argv[3:]
    print(sys.argv)
    print(message)
    mailsend()
else:
    print("Error! Wrong usage of the command line (<email> <password> <message>")











