from selenium import webdriver
# Create a new instance of the Chrome driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get('https://example.com')

# Perform actions to interact with the page and obtain the ticket information
# (These actions will depend on the structure of the website)

# Example: Find an element by its ID
ticket_element = driver.find_element_by_id('ticket_id')

# Get the text content of the ticket element
ticket_text = ticket_element.text

# Print the ticket information
print(f'Ticket Information: {ticket_text}')

# Close the browser window
driver.quit()
