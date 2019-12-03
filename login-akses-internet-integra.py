from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":
    
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get("https://id.its.ac.id/I/index.php?p=http://www.msftconnecttest.com/redirect")
    print('opened chrome webdriver')

    driver.find_element_by_xpath("//a[@href='https://integra.its.ac.id/index.php?n=internet&p=http://www.msftconnecttest.com/redirect']").click()
    print('clicked akses internet personal')

    driver.find_element_by_id('userid').send_keys('05111840000094')
    print('typing nrp')

    driver.find_element_by_id('password').send_keys('password')
    print('typing password')
    
    driver.find_element_by_class_name('btn').click()

    try:
        my = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'btn'), 'Logout'))
        print ("Found - quit")
        driver.quit()
    except TimeoutException:
        print ("Page took to much time - quit")
        driver.quit()
        
    
    
    
    
    