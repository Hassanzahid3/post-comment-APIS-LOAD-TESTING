from locust import HttpUser, task, between

class settings(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)
    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def get_user_settings(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            # Send a GET request to the /v1/users/private/settings endpoint
            response = self.client.get("/v1/users/private/settings", headers=headers)

            # Check the response status code
            if response.status_code == 200:
                # If the response is successful (status code 200), you can add your verification logic here
                pass
            else:
                # Handle the response when it's not 200 (e.g., logging or reporting)
                pass

    @task(2)
    def update_user_settings(self):
        if self.flag == 1:
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            # Define the payload
            payload = {
                "profileType": "private",
                "nearby": True,
                "pushNotification": False,
                "anonymousChat": True,
                "dmNotification": True,
                "emailNotification": True
            }

            # Send a PUT request to the /v1/users/private/settings endpoint with the payload
            response = self.client.put("/v1/users/private/settings", json=payload, headers=headers)

            # Check the response status code
            if response.status_code == 200:
                # If the response is successful (status code 200), you can add your verification logic here
                pass
            else:
                # Handle the response when it's not 200 (e.g., logging or reporting)
                pass
