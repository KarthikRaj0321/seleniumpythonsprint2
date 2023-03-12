from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def enter_colour_catalogue(self):
        self.driver.find_element(By.NAME, "q").send_keys("colour catalogue")

    def click_search(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"headerSearch\"]/div[1]/form/div/button/span").click()

    def click_colour_catalogue(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/section/div/div/div[2]/div/div/div["
                                           "2]/div/div/a/div").click()

    def hovering_on_paints_and_colours_tab(self):
        element_to_hover_over = self.driver.find_element(By.XPATH, "//span[@class='iconTextLinks__text "
                                                                   "visible-in-Desktop'][normalize-space()='PAINTS & "
                                                                   "COLOURS']")
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()

    def click_interior_textures(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Interior Textures']").click()

    def click_exterior_textures(self):
        self.driver.find_element(By.XPATH, "//a[normalze-space()='Exterior Textures']").click()

    def if_filters_displayed_in_exterior_textures(self):
        self.driver.find_element(By.XPATH,
                                 "//section[@class='color-palettes-main-wrapper']//li[1]//a[1]//span[1]").is_displayed()

    def click_exterior_paints(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Exterior Paints']").click()

    def if_various_paints_displayed_in_exterior_paints(self):
        self.driver.find_element(By.XPATH, "//img[@title='Exterior Wall Paints - Asian Paints']").is_displayed()

    def click_on_metal_paints(self):
        self.driver.find_element(By.XPATH, "//a[@class='track_third_level'][normalize-space()='Metal Paints']").click()

    def if_user_is_navigated_to_metal_paints_page(self):
        self.driver.find_element(By.XPATH, "//a[@href='https://www.asianpaints.com/products/wood-and-metals"
                                           "/metal-enamels/apcolite-premium-gloss-enamel.html']").is_displayed()