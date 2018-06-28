from selenium import webdriver
import unittest
import time

MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_quiz_for_visitor(self):
        # ตั้นได้ยินเพื่อนคุยกันเกี่ยวกับ web app ตอบคำถาม True False
        # ตั้นสนใจจึงทดลองเข้าไปตามลิ้งที่เพื่อนให้มา
        self.browser.get('http://localhost:8000/')

        # ตั้นเห็นว่าสามารถเลือกเพิ่มคำถามให้กับ web app นี้ ตั้นเลือกเพิ่มคำถาม
        quiz_link = self.browser.find_element_by_link_text('Add quiz')
        self.assertEqual(quiz_link.get_attribute('href'), 'http://localhost:8000/addquiz')
        quiz_link.click()


        # ตั้นใส่คำถามว่า "1+1=2" และเลือกคำตอบเป็น True จากนั้นกด submit
        inputbox = self.browser.find_elements_by_tag_name('input')
        self.assertEqual(inputbox[0].get_attribute('name'), 'quiz')
        self.assertEqual(inputbox[1].get_attribute('value'), 'True')
        self.assertEqual(inputbox[2].get_attribute('value'), 'False')
        self.assertEqual(inputbox[3].get_attribute('value'), 'Add quiz')
        inputbox[0].send_keys('1+1=2')
        inputbox[1].click()
        inputbox[3].click()

        # ตั้นพบหน้าบอกว่า "Your quiz has been added"
        add_text = self.browser.find_element_by_tag_name('p')
        self.assertEqual('Your quiz has been added', add_text.text)

        # หลังจากตั้งคำถามเสร็จตั้นกดลิงค์ home กลับไปที่หน้าแรก
        self.wait_for_link_text('Home', 'http://localhost:8000/')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
