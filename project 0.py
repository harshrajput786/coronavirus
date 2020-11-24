class Coronavirus():
  def __init__(self):
    self.driver = webdriver.Chrome()
    bot = Coronavirus()
    bot.driver.get('https://www.worldometers.info/coronavirus/')
    self.driver.get('https://www.worldometers.info/coronavirus/')
    table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
    country_element = table.find_element_by_xpath("//td[contains(., 'India')]")
    row = country_element.find_element_by_xpath("./..")
    data = row.text.split(" ")
    total_cases = data[1]
    new_cases = data[2]
    total_deaths = data[3]
    new_deaths = data[4]
    active_cases = data[5]
    total_recovered = data[6]
    serious_critical = data[7]
    def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email', 'password')
    subject = 'Coronavirus stats in your country today!'
    body = 'Today in ' + country_element + '\
    \nThere is new data on coronavirus:\
    \nTotal cases: ' + total_cases +'\
    \nNew cases: ' + new_cases + '\
    \nTotal deaths: ' + total_deaths + '\
    \nNew deaths: ' + new_deaths + '\
    \nActive cases: ' + active_cases + '\
    \nTotal recovered: ' + total_recovered + '\
    \nSerious, critical cases: ' + serious_critical  + '\
    \nCheck the link: https://www.worldometers.info/coronavirus/'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
    'Coronavirus',
    'email',
    msg
    )
    print('Hey Email has been sent!')
    server.quit()
    
