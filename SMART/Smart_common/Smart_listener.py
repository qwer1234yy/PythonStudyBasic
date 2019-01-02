from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class SMART_Listener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print(url)
        pass

    def after_navigate_to(self, url, driver):
        pass

    def before_navigate_back(self, driver):
        pass

    def after_navigate_back(self, driver):
        pass

    def before_navigate_forward(self, driver):
        pass

    def after_navigate_forward(self, driver):
        pass

    def before_find(self, by, value, driver):
        print(value)
        pass

    def after_find(self, by, value, driver):
        pass

    def before_click(self, element, driver):
        print('-------------SMART_Listener-----------')
        pass

    def after_click(self, element, driver):
        pass

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        pass

    def before_execute_script(self, script, driver):
        pass

    def after_execute_script(self, script, driver):
        pass

    def before_close(self, driver):
        pass

    def after_close(self, driver):
        pass

    def before_quit(self, driver):
        pass

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        # <class 'selenium.common.exceptions.NoSuchWindowException'>
        print('Unable to locate element: ' in exception)
        print(type(exception))
        pass
