# cmd command to open localhost chrome
# start chrome.exe --remote-debugging-port=1991 --user-data-dir="C:\Users\Adeniyi Babalola\Desktop\PythonPrograms\chromedata"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from final_scrapper import (click_perapp, random_sleeps, medium_sleep, scrape_players, short_sleep, load_all_players, click_per_start, stat_type_custom, unclick_positions
)


def main():
    # Page is preopened with OPTA Page loaded
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    slider_1 = driver.find_element(By.XPATH, "(//span)[18]")
    slider_2 = driver.find_element(By.XPATH, "(//span)[22]")
    which_gw_are_we_on = (int(slider_2.text) - 1)
    print(which_gw_are_we_on)

def gk_perstart_2gws(driver, wait, slider_1, slider_2, which_gw_are_we_on):
    # Goalkeeper Scrape (Per Start)
    position = "GK"
    gws_to_consider = 2

    # For All The Goalkeepers
    stat_type_custom(driver, wait)

    # Click on GK position alone by unclicked all other positions
    for i in range(1, 4):
        unclick_positions(driver, i)
    
    short_sleep()

    load_all_players(driver, wait)

    click_per_start(driver)

    move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerStart {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

    # Click all the positions earlier unclicked back
    short_sleep()
    for i in range(1, 4):
        unclick_positions(driver, i)
    
    short_sleep()

def gk_perapp_6gws(driver, wait, slider_1, slider_2, which_gw_are_we_on):
    # Goalkeeper Scrape (Per App)
    position = "GK"
    gws_to_consider = 6

    # Click on GK position alone by unclicked all other positions
    for i in range(1, 4):
        unclick_positions(driver, i)

    short_sleep()

    click_perapp(driver)

    move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

    # Click all the positions earlier unclicked back
    short_sleep()

    for i in range(1, 4):
        unclick_positions(driver, i)

    short_sleep()

def def_perapp_5gws(driver, wait, slider_1, slider_2, which_gw_are_we_on):
    # Defender Scrape (Per App)
    position = "DEF"
    gws_to_consider = 5

    # Click on DEFs position alone by unclicked all other positions
    for i in {0, 2, 3}:
        unclick_positions(driver, i)

    short_sleep()

    click_perapp(driver)

    move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

    # Click all the positions earlier unclicked back
    short_sleep()

    for i in {0, 2, 3}:
        unclick_positions(driver, i)

    short_sleep()

def mid_perapp_5gws(driver, wait, slider_1, slider_2, which_gw_are_we_on):
    # Midfielder Scrape (Per App)
    position = "MID"
    gws_to_consider = 5

    # Click on MIDs position alone by unclicked all other positions
    for i in {0, 1, 3}:
        unclick_positions(driver, i)

    short_sleep()

    click_perapp(driver)

    move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

    # Click all the positions earlier unclicked back
    short_sleep()

    for i in {0, 1, 3}:
        unclick_positions(driver, i)

    short_sleep()

def fwd_perapp_6gws(driver, wait, slider_1, slider_2, which_gw_are_we_on):
    # Forwards Scrape (Per App)
    position = "FWD"
    gws_to_consider = 6

    # Click on FWDs position alone by unclicked all other positions
    for i in {0, 1, 2}:
        unclick_positions(driver, i)

    short_sleep()

    click_perapp(driver)

    move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

    # Click all the positions earlier unclicked back
    short_sleep()

    for i in {0, 1, 2}:
        unclick_positions(driver, i)

    medium_sleep()

def move_sliders_and_scrape_new_season(driver, slider_1, slider_2, which_gw_are_we_on, filename, gws_to_consider):
    SLIDER_WIDTH = 569

    # Enter this by dividing 569 by how ever many GWs we are considering
    pixels_per_gw = f"{SLIDER_WIDTH / which_gw_are_we_on:.14f}"
    print(pixels_per_gw)

    # Reset the sliders. Lower slider and Upper slider to last GW
    ActionChains(driver).drag_and_drop_by_offset(slider_2, SLIDER_WIDTH, 0).perform()
    medium_sleep()
    ActionChains(driver).drag_and_drop_by_offset(slider_1, -SLIDER_WIDTH, 0).perform() 
    medium_sleep()

    # # Move upper slider to prediction GW
    # ActionChains(driver).drag_and_drop_by_offset(slider_1, -((gws_to_consider - 1) * float(pixels_per_gw)), 0).perform() # Then move the upper limit to GW3
    # random_sleeps()

    data = scrape_players(driver)
    print("Getting the main player data...")
    
    short_sleep()

    data.to_csv(filename, mode="a", index=False, header=True)


if __name__ == "__main__":
    main()