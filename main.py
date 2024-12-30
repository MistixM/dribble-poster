import json
import time
import os

from DrissionPage import ChromiumPage

def main():
    url = "https://dribbble.com/uploads/new"

    driver = ChromiumPage()

    driver.get(url)

    with open("cookie.json", 'r') as file:
        cookies = json.load(file)

        for cookie in cookies:
            # do not delete this block of code. crucial for the cookie work
            if cookie.get('sameSite') not in ['None', 'Lax', 'Strict']:
                cookie['sameSite'] = 'Lax'

            driver.set.cookies(cookie)

    time.sleep(1)

    driver.refresh()

    time.sleep(1)


    posts = os.path.join(os.path.dirname(__file__), 'posts')
    
    for post in os.listdir(posts):
        uploader = driver.ele('.drag-drop-container media-drop-zone')

        post_path = os.path.join(posts, post)
        
        items = []

        for item in os.listdir(post_path):
            item_path = os.path.join(post_path, item)
            items.append(item_path)

        uploader.click.to_upload(items)


        time.sleep(1)

        title = driver.ele('.textarea transparent-textarea-heading1')
        title.input(post)

        time.sleep(15)

        draft_button = driver.ele('.save-btn form-btn')
        draft_button.click()

        items.clear()

        time.sleep(5)

        print("Post was saved as draft")
        driver.refresh()

    print("All posts were loaded!")

if __name__ == '__main__':
    main()