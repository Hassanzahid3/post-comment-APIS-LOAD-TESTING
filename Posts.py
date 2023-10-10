from locust import HttpUser, task, between


class Posts(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def get_s3_presigned_url(self):
        if self.flag == 1:
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "20",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            payload = {
                "postType": "display",
                "fileExtension": "jpg"
            }

            response = self.client.post(
                "/v1/posts/private/s3/get-presigned-url",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass  # Handle a successful response if needed
            else:
                pass  # Handle an unsuccessful response if needed

    @task(2)
    def create_post(self):
        if self.flag == 1:
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "20",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            payload = {
                "postType": "text",
                "postContent": "my post for testing - abdo hahaha"
            }

            response = self.client.post(
                "/v1/posts/private/user-posts",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                pass  # Handle a successful response if needed
            else:
                pass  # Handle an unsuccessful response if needed

    @task(3)
    def get_all_posts(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            response = self.client.get(
                "/v1/posts/private/user-posts?page-number=1&items-per-page=20",
                headers=headers
            )

            if response.status_code == 200:
                pass  # Handle a successful response if needed
            else:
                pass  # Handle an unsuccessful response if needed

    @task(4)
    def get_single_post(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            # Replace {post_id} with the actual post ID you want to retrieve
            post_id = "5e337fae-26e6-49d5-b6b2-255f7f795f43"

            response = self.client.get(
                f"/v1/posts/private/post-detail/{post_id}",
                headers=headers
            )

            if response.status_code == 200:
                pass  # Handle a successful response if needed
            else:
                pass  # Handle an unsuccessful response if needed

    @task(5)
    def delete_single_post(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            # Replace {post_id} with the actual post ID you want to delete
            post_id = "0a05c76a-d7b5-4ac0-96ec-2323ea4d2572"

            response = self.client.delete(
                f"/v1/posts/private/post-detail/{post_id}",
                headers=headers
            )

            if response.status_code == 204:
                pass  # Handle a successful deletion (status code 204) if needed
            else:
                pass  # Handle an unsuccessful response if needed

    @task(6)
    def get_post_by_user_id(self):
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            user_id = "4a8185bd-a0c3-426f-99df-233f5af19557"  # Replace with the actual user ID

            response = self.client.get(
                f"/v1/posts/private/user-posts/{user_id}?page-number=1&items-per-page=10",
                headers=headers
            )

            if response.status_code == 200:
                pass  # Handle a successful response (status code 200) if needed
            else:
                pass  # Handle an unsuccessful response if needed
