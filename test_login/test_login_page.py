import time
import allure



def test_open_login_page(app, credentials):
   with allure.step ('Открываем страницу логина и вводим данные учетной записи'):
      app.forms.form_login.sign_in(credentials['login'], credentials['password'])
      assert app.forms.form_main.current_user_login() == credentials['username']
      app.forms.form_main.logout()

def test_incorrect_login(app, credentials):
   with allure.step('Проверяем невозможность входа с некорректным логином'):
      app.forms.form_login.sign_in(credentials['login'] + 'Qwe123', credentials['password'])
      assert app.forms.form_login.get_alert_text() == 'Incorrect username or password.'

def test_incorrect_password(app, credentials):
   with allure.step('Проверяем невозможность входа с некорректным паролем'):
      app.forms.form_login.sign_in(credentials['login'] , credentials['password'] + 'Qwe123')
      assert app.forms.form_login.get_alert_text() == 'Incorrect username or password.'
