from locust import HttpUser, task, between


class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)
    flag = 2  # Set the flag here

    @task(1)
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
            "/v1/users/public/register",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            pass
        else:
            pass

    @task(2)
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

    @task(3)
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

    @task(4)
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

    @task(5)
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

    @task(6)
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

    @task(7)
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

    @task(8)
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

    @task(9)
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

    @task(10)
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

    @task(11)
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

    @task(12)
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

    @task(13)
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
