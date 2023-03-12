import time

import pytest
import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageobjects.Home_Page import Homepage


@pytest.mark.usefixtures("setup")
class Testcase1:

    def test_case1(self):
        pc = Homepage(self.driver)
        pc.enter_colour_catalogue()
        pc.click_search()
        pc.click_colour_catalogue()

        time.sleep(5)

    def test_case2(self):
        pc = Homepage(self.driver)
        pc.hovering_on_paints_and_colours_tab()
        pc.click_interior_textures()

        time.sleep(5)

    def test_case3(self):
        pc = Homepage(self.driver)
        pc.hovering_on_paints_and_colours_tab()
        pc.click_exterior_textures()
        pc.if_filters_displayed_in_exterior_textures()

        time.sleep(5)

    def test_case4(self):
        pc = Homepage(self.driver)
        pc.hovering_on_paints_and_colours_tab()
        pc.click_exterior_paints()
        pc.if_various_paints_displayed_in_exterior_paints()
        time.sleep(5)

    def test_case5(self):
        pc = Homepage(self.driver)
        pc.hovering_on_paints_and_colours_tab()
        pc.click_on_metal_paints()
        pc.if_user_is_navigated_to_metal_paints_page()
        time.sleep(5)
