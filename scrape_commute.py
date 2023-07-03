from lattice_governor.driver_setup import DriverSetup
from subprocess import Popen

def scrape_commute():

    driver = DriverSetup()
    breakpoint()
    goog_dict = driver.get_site_db("google")
    search_id = goog_dict.get("search_box")
    driver.search_site(goog_dict.get("url"), "how long is my commute to work")
    breakpoint()

if __name__ == "__main__":
    scrape_commute()