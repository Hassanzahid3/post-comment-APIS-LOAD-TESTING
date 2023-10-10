from locust import HttpUser, task, between

class Authentication(HttpUser):
    host = "https://staging.imlink.network"  # Set the host URL
    wait_time = between(1, 5)  # Define the time range between requests
    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def login(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for login task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the POST request
            payload = {
                "usernameOrEmail": "ram.2277@outlook.com",
                "password": "Rewaa12345",
                "deviceType": "IOS",
                "osVersion": "30.1",
                "deviceId": "123456"
            }

            # Send the POST request for login
            response = self.client.post("/v1/auth/public/login", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Login successful")
            else:
                print("Login failed")

    @task(2)
    def refresh_token(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for refresh token task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the POST request
            payload = {
                "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwOTc3MjMyLCJpYXQiOjE2ODgzODUyMzIsImp0aSI6ImI3NGFiODc4YWZmOTQwZTNhNmVkYWE3NGUwNmJhYTZlIiwidXNlcl9pZCI6IjNmZmI9N2I5LTNhNDMtNDlhNC05ZjlhLTVhY2ZmZWZjNjZiMyJ9.YcImMA3CAA0YOBspXnTAMdms6ddVUYdhYbLuHWtio8c"
            }

            # Send the POST request for refreshing token
            response = self.client.post("/v1/auth/public/refresh", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Token refresh successful")
            else:
                print("Token refresh failed")

    @task(3)
    def verify_user(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for verify user task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "200",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the POST request
            payload = {
                "email": "Rewaa@link.com",
                "otp": "7456"
            }

            # Send the POST request for verifying user
            response = self.client.post("/v1/auth/public/otp/verify", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("User verification successful")
            else:
                print("User verification failed")

    @task(4)
    def verify_update_email(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for verify and update email task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the POST request
            payload = {
                "email": "some@gmail.com",
                "otp": "2647"
            }

            # Send the POST request for verifying and updating email
            response = self.client.post("/v1/auth/private/otp/email-update", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Email verification and update successful")
            else:
                print("Email verification and update failed")

    @task(5)
    def resend_otp(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for resend OTP task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the PUT request
            payload = {
                "email": "hassanrajpoot6330@gmail.com"
            }

            # Send the PUT request for resending OTP
            response = self.client.put("/v1/auth/public/otp/resend", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("OTP resend successful")
            else:
                print("OTP resend failed")

    @task(6)
    def change_password(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for change password task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the PUT request
            payload = {
                "email": "hassanrajpoot6330@gmail.com",
                "otp": "9280",
                "password": "kamar1234",
                "confirmPassword": "kamar1234"
            }

            # Send the PUT request for changing password
            response = self.client.put("/v1/auth/public/create-new-password", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Password change successful")
            else:
                print("Password change failed")

    @task(7)
    def forget_password(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for forget password task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the PUT request
            payload = {
                "email": "hassanrajpoot6330@gmail.com"
            }

            # Send the PUT request for initiating password reset
            response = self.client.put("/v1/auth/public/forget-password", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Password reset initiated successfully")
            else:
                print("Password reset initiation failed")

    @task(8)
    def authentication_internal(self):
        if self.flag == 1:
            # Initialize the HTTP session with custom headers for authentication internal task
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "0",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "staging.imlink.network",
            }

            # Define the payload for the POST request
            payload = {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2OTE1NDM5LCJpYXQiOjE2ODQzMjM0MzksImp0aSI6Ijg4NTMxNjAzYmI1NzQ4Y2I5NDU3MjMwOWZmNWZlYTJhIiwidXNlcl9pZCI6IjNmZmI9N2I5LTNhNDMtNDlhNC05ZjlhLTVhY2ZmZWZjNjZiMyJ9.YcImMA3CAA0YOBspXnTAMdms6ddVUYdhYbLuHWtio8c"
            }

            # Send the POST request for internal authentication
            response = self.client.post("/v1/auth/public/authentication", json=payload, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("Authentication successful")
            else:
                print("Authentication failed")

    @task(9)
    def logout(self):
        if self.flag == 1:
            headers = {
                "Content-Length": "0",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            # Send the POST request for logout
            response = self.client.post("/v1/auth/private/logout", headers=headers)

            if response.status_code == 200:
                print("Logout successful")
            else:
                print("Logout failed")
