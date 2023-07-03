from subprocess import Popen

if __name__ == "__main__":
    Popen("conda run -n web-scraper python scrape_commute.py")