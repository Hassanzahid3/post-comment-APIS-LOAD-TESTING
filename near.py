from locust import HttpUser, task, between

class Nearby(HttpUser):
    host = "https://staging.imlink.network"

    wait_time = between(1, 5)  # Set the wait time between requests

    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def update_user_location(self):
        if self.flag == 1:
            endpoint = "/v1/nearby/private/nearby-range?min-latitude=28.611962&max-latitude=35.914025&min-longitude=68.047595&max-longitude=75.413915"
            url = f"{self.host}{endpoint}"
            payload = {
                "latitude": 31.7091758473,
                "longitude": 73.9848945803
            }
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(2)
    def enable_disable_nearby_device(self):
        if self.flag == 1:
            url = f"{self.host}/v1/users/private/switch-nearby"
            payload = {
                "nearby": False
            }
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.put(url, json=payload, headers=headers)

            if response.status_code == 200:
                self.environment.events.request_success.fire(
                    request_type="PUT",
                    name="Update User Nearby",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    response=response,
                )
            else:
                self.environment.events.request_failure.fire(
                    request_type="PUT",
                    name="Update User Nearby",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    exception=None,
                )

    @task(3)
    def get_nearby_user(self):
        if self.flag == 1:
            endpoint = "/v1/nearby/private/nearby"
            url = f"{self.host}{endpoint}"
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get(url, headers=headers)

            if response.status_code == 200:
                self.environment.events.request_success.fire(
                    request_type="GET",
                    name="Get Nearby User",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    response=response,
                )
            else:
                self.environment.events.request_failure.fire(
                    request_type="GET",
                    name="Get Nearby User",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    exception=None,
                )

    @task(4)
    def get_nearby_user_range(self):
        if self.flag == 1:
            endpoint = "/v1/nearby/private/nearby-range?min-latitude=28.611962&max-latitude=35.914025&min-longitude=68.047595&max-longitude=75.413915"
            url = f"{self.host}{endpoint}"
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get(url, headers=headers)

            if response.status_code == 200:
                self.environment.events.request_success.fire(
                    request_type="GET",
                    name="Get Nearby User Range",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    response=response,
                )
            else:
                self.environment.events.request_failure.fire(
                    request_type="GET",
                    name="Get Nearby User Range",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    exception=None,
                )


