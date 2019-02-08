from selenium import webdriver

globBrowser = None


def before_scenario(context, scenario):
    global globBrowser
    if globBrowser is None:

        context.browser = webdriver.Chrome("features/chromedriver")
        globBrowser = context.browser
        if 'User signup with valid data' in scenario.name:
            globBrowser.get("https://demo-biq.dev.tradecore.io/#/")
        else:
            globBrowser.get("https://demo-biq.dev.tradecore.io/#/portal/accounts")
    else:
        context.browser = globBrowser
