from selenium import webdriver
import unittest
import time

MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_link_text(self, link_text, link):
        start_time = time.time()
        while True:
            try:
                web_link = self.browser.find_element_by_link_text(link_text)
                self.assertEqual(web_link.get_attribute('href'), link)
                web_link.click()
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for_text_in_tag_name_p(self, text):
        start_time = time.time()
        while True:
            try:
                web_text = self.browser.find_element_by_tag_name('p')
                self.assertIn(text, web_text.text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_add_and_answer_a_quiz_for_visitor(self):
        # ตั้นได้ยินเพื่อนคุยกันเกี่ยวกับ web app ตอบคำถาม True False
        # ตั้นสนใจจึงทดลองเข้าไปตามลิ้งที่เพื่อนให้มา
        self.browser.get('http://localhost:8000/')

        # ตั้นเห็นว่าสามารถเลือกเพิ่มคำถามให้กับ web app นี้ ตั้นเลือกเพิ่มคำถาม
        self.wait_for_link_text('Add quiz', 'http://localhost:8000/addquiz')

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
        self.wait_for_text_in_tag_name_p('Your quiz has been added')

        # หลังจากตั้งคำถามเสร็จตั้นกดลิงค์ home กลับไปที่หน้าแรก
        self.wait_for_link_text('Home', 'http://localhost:8000/')

        # ตั้นทดลองไปตอบคำถาม
        self.wait_for_link_text('Answer', 'http://localhost:8000/answer')

        # ตั้นพบคำถามที่พึ่งสร้างอยู่บนสุดและตอบคำถามนั้น
        self.wait_for_text_in_tag_name_p('1+1=2')

        ans = self.browser.find_element_by_tag_name('input')
        self.assertEqual(ans.get_attribute('name'), 'ans1')
        ans.click()

        time.sleep(3)
        ans_button = self.browser.find_element_by_id('id_ans_button')
        self.assertEqual(ans_button.get_attribute('value'), 'Answer')
        ans_button.click()

        # ตั้นพบหน้าบอกว่าคุณตอบถูก 1 ข้อ
        self.wait_for_text_in_tag_name_p('You answered 1 question correctly')

        # ตั้นพอใจแล้วจึงปิดเว็บไป

if __name__ == '__main__':
    unittest.main(warnings='ignore')
