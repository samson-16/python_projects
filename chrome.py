import webbrowser as web

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    URLS=(
        "stackoverflow.com",
        "github.com/samson-16",
        "gmail.com"
    )

    for url in URLS:
        print("opening: "+url)
        web.get(chrome_path).open(url)
webauto()