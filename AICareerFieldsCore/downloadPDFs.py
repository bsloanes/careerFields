#NEWEST
def downloadNscroll(webpage):
    import time 
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from bs4 import BeautifulSoup
    import requests
    import os

    # Initialize the Selenium web driver (you need to specify the path to your driver)
    
    driver = webdriver.Chrome(executable_path='/Users/bianca/Documents/AICareerFields/chromedriver')
    
    # URL of the page with search results
    url = webpage  
    
    # Open the page in the browser
    driver.get(url)
    num_pages = 22
    
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".epub-download")))
    
    # Specify a directory to save the downloaded PDFs
    download_dir = "pdfs/"

    # Loop through the desired number of pages
    for page in range(1, num_pages + 1):
        # Find the pagination element for the current page
        pagination_element = driver.find_element(By.CSS_SELECTOR, f"a.paginate_button[data-dt-idx='{page}']")
        
        # Introduce a small delay before clicking on the pagination element
        time.sleep(1)
        
        # Check if the pagination element is visible
        if pagination_element.is_displayed() and pagination_element.is_enabled():
        #if EC.element_to_be_clickable((By.CSS_SELECTOR, f"a.paginate_button[data-dt-idx='{page}']")):
        #if pagination_element.is_displayed():

            # Click on the pagination element to navigate to the next page
            pagination_element.click()

            # Wait for the next page to load
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".epub-download")))

            # Extract and download the PDFs from the current page
            pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")

            for link in pdf_links:
                pdf_url = link.get_attribute("href")
                pdf_filename = os.path.join(download_dir, pdf_url.split("/")[-1])

                # Download the PDF using the code from the previous solution
                response = requests.get(pdf_url)
                if response.status_code == 200:
                    with open(pdf_filename, "wb") as file:
                        file.write(response.content)
                    print(f"Downloaded: {pdf_filename}")
                else:
                    print(f"Failed to download: {pdf_url}")
                    
        else:
            print(f"Pagination element for page {page} is not visible. Skipping...")
                
    # Close the web driver
    driver.quit()