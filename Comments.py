from locust import HttpUser, task, between

class Comments(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)
    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def create_comment(self):
     if self.flag == 1:
        endpoint = "/v1/comments/private/comment"

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
            "contentId": "8f947174-bc3e-4dd8-ab22-e44d41a9bd90",
            "comment": "dont rush now",
            "contentType": "post"
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Create Comment Successful")
        else:
            self.log.error("Create Comment Failed")

    @task(2)
    def update_comment(self):
     if self.flag == 1:
        endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"

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
            "comment": "good job v good",
            "commentType": "gif"
        }

        response = self.client.put(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Update Comment Successful")
        else:
            self.log.error("Update Comment Failed")

    @task(3)
    def delete_comment(self):
      if self.flag == 1:
        endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.delete(endpoint, headers=headers)

        if response.status_code == 204:
            self.log.info("Delete Comment Successful")
        else:
            self.log.error("Delete Comment Failed")

    @task(4)
    def get_comment_details(self):
      if self.flag == 1:
        endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Comment Details Successful")
        else:
            self.log.error("GET Comment Details Failed")

    @task(5)

    def get_all_comment(self):
      if self.flag == 1:
        endpoint = "/v1/comments/private/comments?contentId=0b1fb129-2737-469c-90ec-f999fdc6dc57"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET All Comments Successful")
        else:
            self.log.error("GET All Comments Failed")


