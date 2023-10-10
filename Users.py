from locust import HttpUser, task, between


class Users(HttpUser):
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

    @task(10)
    def block_user(self):
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

    @task(11)
    def unblock_user(self):
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
                "userId": "32321b04-ff15-4143-8309-d1d901c965c4"
            }

            response = self.client.post(
                "/v1/users/private/unblock",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(12)
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

    @task(13)
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

    @task(14)
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

    @task(15)
    def register_user(self):
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
            "email": "mailto:abdullah.ahmed@imlink.network",
            "username": "abdullah.ahmad01",
            "fullName": "Abdullah Ahmad",
            "password": "Password1@#",
            "confirmPassword": "Password1@#",
            "gender": "2",
            "phone": "+923244545555",
            "dateOfBirth": "16-03-2000",
            "deviceId": "1234",
            "deviceType": "IOS",
            "osVersion": "30.1"
        }

        response = self.client.post(
            "/v1/users/public/register", headers=headers,
            json=payload
        )

        if response.status_code == 200:
            pass
        else:
            pass

    @task(16)
    def authenticate_internal(self):
        if self.flag == 1:
            endpoint = "/v1/auth/private/authenticate"
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(endpoint, headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(17)
    def profile_update(self):
        if self.flag == 1:
            endpoint = "/v1/users/private/profile"
            payload = {
                "fullName": "Linker Khan Ji"
            }

            headers = {
                "Content-Type": "application/json",
                "Content-Length": "172",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.put(endpoint, json=payload, headers=headers)

            if response.status_code == 200:
                pass
            else:
                pass

    @task(18)
    def user_followers(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/follower",
                headers=headers
            )

            if response.status_code == 200:

                pass
            else:

                pass

    @task(19)
    def user_following(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/following",
                headers=headers
            )

            if response.status_code == 200:

                pass
            else:

                pass

    @task(20)
    def get_user_profile(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/profile",
                headers=headers
            )

            if response.status_code == 200:

                pass
            else:
                # Handle the response when it's not 200 (e.g., logging or reporting)
                pass

    @task(21)
    def del_user_profile(self):
        if self.flag == 1:

            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.delete(
                "/v1/users/private/profile",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(22)
    def switch_user_profile(self):
        if self.flag == 1:
            headers = {
                "Content-Length": "0",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.put(
                "/v1/users/private/switch-profileType",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(23)
    def otp_user_verify(self):
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
                "email": "linker1",
                "otp": "8567"
            }

            response = self.client.patch(
                "/v1/auth/public/register/otp-verify",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(24)
    def get_all_user_internal(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/users?page-number=1&items-per-page=20",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(25)
    def get_other_user_detail(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/user/8d771c8b-0657-43df-8852-d8086bd496e1",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(26)
    def search_user_with_string(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/search-user?search=a&page-number=1&items-per-page=50",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    @task(27)
    def change_password(self):
        if self.flag == 1:
            # Define the headers
            headers = {
                "Host": "staging.imlink.network",
                "Content-Type": "application/json",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }
            # Define the payload (use lowercase "payload" consistently)
            payload = {
                "currentPassword": "test12345",
                "newPassword": "test12345678",
                "confirmNewPassword": "test12345678"
            }

            # Perform the PUT request to change the password
            response = self.client.put("/users/private/change-password", json=payload, headers=headers)

            if response.status_code == 200:
                print("Password changed successfully")
            else:
                print(f"Password change failed with status code: {response.status_code}")
                print(response.text)  # Print the response text for debugging
