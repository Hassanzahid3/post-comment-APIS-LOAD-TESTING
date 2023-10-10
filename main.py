from locust import HttpUser, task, between


class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def follow_user(self):
        if self.flag == 1:
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "200",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            payload = {
                "userId": "079c81d5-2705-4c99-8683-03dbed0b83ff"
            }
            response = self.client.post(
                "/v1/users/private/follow",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass