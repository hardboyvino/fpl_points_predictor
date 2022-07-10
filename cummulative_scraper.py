import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from seasonal_scrape import gk_perapp_6gws, gk_perstart_2gws, def_perapp_5gws, mid_perapp_5gws, fwd_perapp_6gws
from add_prediction_to_csv import all_predictions


def main():
    # Page is preopened with OPTA Page loaded
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    slider_1 = driver.find_element(By.XPATH, "(//span)[18]")
    slider_2 = driver.find_element(By.XPATH, "(//span)[22]")
    which_gw_are_we_on = (int(slider_2.text) - 1)

    def_pickles = ["Linear DEF PerApp 5GWs.pkl", "Incomplete Forest DEF PerApp 5GWs.pkl"]
    mid_pickles = ["Linear MID PerApp 5GWs.pkl", "Incomplete Forest MID PerApp 5GWs.pkl"]
    fwd_pickles = ["Linear FWD PerApp 6GWs.pkl", "Incomplete Forest FWD PerApp 6GWs.pkl"]

    # gk_perstart_2gws(driver, wait, slider_1,slider_2, which_gw_are_we_on)

    # gk_perapp_6gws(driver, wait, slider_1,slider_2, which_gw_are_we_on)

    # def_perapp_5gws(driver, wait, slider_1,slider_2, which_gw_are_we_on)

    # mid_perapp_5gws(driver, wait, slider_1,slider_2, which_gw_are_we_on)

    fwd_perapp_6gws(driver, wait, slider_1,slider_2, which_gw_are_we_on)

    all_predictions(def_pickles, mid_pickles, fwd_pickles)

if __name__ == "__main__":
    main()