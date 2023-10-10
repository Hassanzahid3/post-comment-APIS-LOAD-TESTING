from locust import HttpUser, task, between


class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Define a class-level flag with a default value of 1
    flag = 2

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

    @task(2)
    def unfollow_user(self):
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
                "userId": "4a8185bd-a0c3-426f-99df-233f5af19557"
            }
            response = self.client.delete(
                "/v1/users/private/unfollow",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(3)
    def accept_follow_request(self):
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
                "followRequestId": "cb136675-36d6-44e1-a613-f2566dc6bf1d"
            }
            response = self.client.post(
                "/v1/users/private/accept-follow-request",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(4)
    @task
    def remove_follow_request(self):
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
                "follow_request_id": "9b484be0-2257-43c3-8ff2-aa942806d29e"
            }
            response = self.client.delete(
                "/v1/users/private/remove-follow-request",
                json=payload,
                headers=headers
            )

            if response.status_code == 204:
                pass
            else:
                pass

    @task(5)
    def reject_follow_request(self):
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
                "followRequestId": "9b484be0-2257-43c3-8ff2-aa942806d29e"
            }
            response = self.client.put(
                "/v1/users/private/reject-follow-request",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(6)
    def get_followers(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get("/v1/users/private/follower?page-number=1&items-per-page=20", headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(7)
    def get_following(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get("/v1/users/private/following?page-number=1&items-per-page=5", headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(8)
    def get_following_ids_internal(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get("/v1/users/private/following-ids", headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(9)
    def get_recieved_follow_requests(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.get("/v1/users/private/follow-requests?page-number=1&items-per-page=5",
                                       headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass
