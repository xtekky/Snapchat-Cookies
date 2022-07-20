import requests, urllib.parse, json


class SnapCookies:
    def __init__(self, session: requests.Session) -> None:
        self.headers = {'host': 'accounts.snapchat.com', 'connection': 'keep-alive', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36', 'accept': '*/*', 'sec-gpc': '1', 'origin': 'https://web.snapchat.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://web.snapchat.com/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
        self.session = session
        
    def client_id(self) -> None:
        self.session.options(
            url = (
                'https://'
                    +'accounts.snapchat.com'
                    + '/accounts/sso?'
                    + urllib.parse.urlencode(
                        {
                            "client_id": "web-calling-corp--prod"
                    }
                )
            )
        )
        
    def xcrsf_token(self) -> None:
        x = self.session.post(
            url = (
                'https://'
                    +'accounts.snapchat.com'
                    + '/accounts/sso?'
                    + urllib.parse.urlencode(
                        {
                            "client_id": "web-calling-corp--prod"
                    }
                )
            )
        )
    
    def header_cookies(self) -> str:
        cookies = ""
        for item in self.session.cookies.items(): 
            cookies += (
                "=".join(
                    item
                ) 
                + '; '
            )
        
        return cookies
        
    def get_cookies(self) -> str:
        self.client_id()
        self.xcrsf_token()
        
        headers = {
            "cookie": self.header_cookies()
        }
        
        return headers

if __name__ == "__main__":
    session = requests.Session()
    headers = SnapCookies(session).get_cookies()

    # print(session.cookies)
    print(json.dumps(headers, indent=4))
