from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
from locator import Locator
from constants import Constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from pathlib import Path


class DeepsetAnnotationUserFlow(unittest.TestCase):

    def setUp(self, browser='Chrome'):

        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(Locator.deepset_url)

        time.sleep(1)

        email_element = self.driver.find_element_by_id(Locator.email_id)
        email_element.send_keys(Constants.email)

        password_element = self.driver.find_element_by_id(Locator.password_id)
        password_element.send_keys(Constants.password)

        login_button = self.driver.find_element_by_xpath(Locator.login_button_path)
        login_button.click()

        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.projects_heading_path))
        )
        assert elem.text == Constants.project_heading

    def test_a_create_project(self):

        create_pjt_button = self.driver.find_element_by_xpath(Locator.create_project_button_path)
        create_pjt_button.click()

        project_name_element = self.driver.find_element_by_id(Locator.project_name_placeholder_id)
        project_name_element.send_keys(Constants.project_name)

        final_create_pjt_button = self.driver.find_element_by_xpath(Locator.final_create_project_button)
        final_create_pjt_button.click()

        time.sleep(3)

        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.project_created_row_path))
        )
        assert Constants.project_name in elem.text

    def test_c_delete_project(self):

        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.projects_table))

        )

        line = elem.text.split("\n")
        for i in range(len(line)):
            if Constants.project_name in line[i]:
                row = i

        delete_pjt_icon = self.driver.find_element_by_xpath(
            "(" + Locator.delete_project_icon + ")[" + str(row + 1) + "]")

        self.driver.execute_script("arguments[0].click();", delete_pjt_icon)
        yes_span = self.driver.find_element_by_xpath(Locator.yes_span_to_delete_pjt)
        self.driver.execute_script("arguments[0].click();", yes_span)

    def test_b_upload_document(self):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.projects_table))

        )

        line = elem.text.split("\n")
        for i in range(len(line)):
            if Constants.project_name in line[i]:
                row = i
        icon_arrow_right = self.driver.find_element_by_xpath(
            "(" + Locator.icon_arrow_right + ")[" + str(row + 1) + "]")
        self.driver.execute_script("arguments[0].click();", icon_arrow_right)
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.documents_heading))

        )

        hover_import_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.import_menu))

        )
        hover_import_menu.click()

        click_documents_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.import_xpath))

        )
        click_documents_button.click()
        time.sleep(3)

        upload_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.input_icon))

        )
        base_path = Path(__file__).parent
        file_path = (base_path / Constants.file_to_be_uploaded).resolve()

        upload_icon.send_keys(str(file_path))

        documents_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.documents_tab))

        )
        documents_tab.click()
        time.sleep(3)

        assert Constants.contents_of_file in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
