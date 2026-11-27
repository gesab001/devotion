from playwright.sync_api import sync_playwright


def getParagraph(topic):
    target_div_id = "egw_paragraph"

    with sync_playwright() as p:
      browser = p.chromium.launch(headless=True)
      page = browser.new_page()
      page.goto("https://gesab001.github.io/egw/?topic="+topic)

      # Wait for the JS-loaded div to appear in the DOM
      div_locator = page.locator(f"#{target_div_id}")
      div_locator.wait_for(state="visible", timeout=10000)

      # Extract text or raw HTML
      text_content = div_locator.inner_text()
      html_content = div_locator.inner_html()

      print(text_content)
      browser.close()
      
getParagraph("angel")      