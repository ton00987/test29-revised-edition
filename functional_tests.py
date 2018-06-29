from selenium import webdriver
import unittest
import time

MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_and_answer_a_quiz_for_visitor(self):
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
        home_link = self.browser.find_element_by_link_text('Home')
        self.assertEqual(home_link.get_attribute('href'), 'http://localhost:8000/')
        home_link.click()

        # ตั้นทดลองไปตอบคำถาม
        ans_link = self.browser.find_element_by_link_text('Answer')
        self.assertEqual(ans_link.get_attribute('href'), 'http://localhost:8000/answer')
        ans_link.click()

        # ตั้นพบคำถามที่พึ่งสร้างอยู่บนสุดและตอบคำถามนั้น
        question = self.browser.find_element_by_tag_name('p')
        self.assertIn('1+1=2', question.text)

        ans = self.browser.find_element_by_tag_name('input')
        self.assertEqual(ans.get_attribute('name'), 'ans1')
        ans.click()

        time.sleep(3)
        ans_button = self.browser.find_element_by_id('id_ans_button')
        self.assertEqual(ans_button.get_attribute('value'), 'Answer')
        ans_button.click()

        # ตั้นพบหน้าบอกว่าคุณตอบถูก 1 ข้อ
        congrat_text = self.browser.find_element_by_tag_name('p')
        self.assertIn('You answered 1 question correctly', congrat_text.text)

        # ตั้นพอใจแล้วจึงปิดเว็บไป

if __name__ == '__main__':
    unittest.main(warnings='ignore')
