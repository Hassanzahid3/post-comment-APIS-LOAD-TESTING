from locust import HttpUser, task, between


class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def block_user(self):
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
            payload = {
                "userId": "32321b04-ff15-4143-8309-d1d901c965c4"
            }

            response = self.client.post(
                "/v1/users/private/block",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(2)
    def unblock_user(self):
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
            payload = {
                "userId": "32321b04-ff15-4143-8309-d1d901c965c4"
            }

            response = self.client.delete(
                "/v1/users/private/unblock",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(3)
    def get_blocked_users(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/block-users?page-number=1&items-per-page=10",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass
