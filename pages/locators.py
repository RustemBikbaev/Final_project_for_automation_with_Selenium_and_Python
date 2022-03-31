from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    
    #EMAIL_FOR_LOGIN = (By.CSS_SELECTOR, "#id_login-username")   
    #PASSWORD_FOR_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    
    #REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_login-password")   
    #PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_login-password")   
    #PASSWORD_FOR_REGISTRATION_AGAINE = (By.CSS_SELECTOR, "#id_login-password")
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")