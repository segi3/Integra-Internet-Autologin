# Integra Autologin Akses Internet

Untuk login akses internet karena aku males&&mager

![demo](https://media.giphy.com/media/cjiFG82TysNVqkt3Km/giphy.gif)

## Requirement

1. Punya akun integra
2. Udah install [Python 3](https://www.python.org/downloads/)
3. Punya Python [pip](https://pip.pypa.io/en/stable/), cara install [ini](https://www.liquidweb.com/kb/install-pip-windows/)
4. Download [Webdriver untuk chrome](https://chromedriver.chromium.org/downloads) sesuai versi Google Chrome mu


## Installation

`chromedriver.exe` pindah ke `C:\chromedriver.exe`

kalau mau pake path sendiri, nanti ganti path dalem file py nya
```python
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
```

Buka Command Prompt, install [Selenium](https://pypi.org/project/selenium/)

```bash
pip install -U selenium
```
Dalem file py ganti nrp sama passwordnya
```python
driver.find_element_by_id('userid').send_keys('05111840000094') #buat nrp
driver.find_element_by_id('password').send_keys('password') #buar password
```

## Usage

Buka Command Prompt di path file nya
```bash
python login-akses-internet-integra.py
```
misalnya ku simpen di download berarti:
```bash
C:\Users\Rafi Nizar\Downloads>python login-akses-internet-integra.py
```

## AutoHotKey

Karena aku lebih mager lagi, bisa di tambahin shortcut pake [ahk](https://www.autohotkey.com/)

Di file `script.ahk` tinggal ganti path file py nya
```ahk
Send cd D:\file\path{Enter}
```

Default nya Windows+O buat run script, bisa di ganti jadi yang lain
```html
#o::
```

[yaboi](https://steamcommunity.com/id/nizar15/)
