from locust import HttpUser, task, between

class Places(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)
    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def check_in(self):
     if self.flag == 1:
        endpoint = "/v1/places/private/checkin/4b98ccf1f964a520235035e3/users?page-number=1&items-per-page=1"

        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "fsqId": "4b98ccf1f964a520235035e3",
            "latitude": 31.373669,
            "longitude": 74.181947,
            "name": "Food Court Bahria Test3",
            "category": "Cafe",
            "userCount": 1
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Check-In Successful")
        else:
            self.log.error("Check-In Failed")

    @task(2)
    def get_nearby_places(self):
     if self.flag == 1:
        endpoint = "/v1/places/private/places?lat=31.3695&long=74.1768&items-per-page=2"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Nearby Places Successful")
        else:
            self.log.error("GET Nearby Places Failed")

    @task(3)
    def search_places(self):
     if self.flag == 1:
        endpoint = "/v1/places/private/search-places?lat=31.5315&long=74.3679&search=stadium&items-per-page=2"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Search Places Successful")
        else:
            self.log.error("GET Search Places Failed")

    @task(4)
    def get_checkin_users(self):
     if self.flag == 1:
        endpoint = "/v1/places/private/checkin/4b98ccf1f964a520235035e3/users?page-number=1&items-per-page=1"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Check-In Users Successful")
        else:
            self.log.error("GET Check-In Users Failed")


