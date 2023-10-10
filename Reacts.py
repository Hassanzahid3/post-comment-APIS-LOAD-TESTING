from locust import HttpUser, task, between


class Reacts(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Define a class-level flag with a default value of 1
    flag = 1

    @task(1)
    def post_reaction(self):
     if self.flag == 1:
        payload = {
            "contentType": "post",
            "contentId": "8f947174-bc3e-4dd8-ab22-e44d41a9bd90",
            "reaction": "2110001"
        }

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
        }

        response = self.client.post("/v1/reacts/private/like", json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Post Reaction Successful")
        else:
            self.log.error("Post Reaction Failed")

    @task(2)
    def get_reaction_count(self):
     if self.flag == 1:
        endpoint = "/v1/reacts/private/likes?contentId=949f3146-3dc3-4e15-aff5-ea92decc8210"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("Get Reaction Count Successful")
        else:
            self.log.error("Get Reaction Count Failed")

    @task(3)
    def update_reaction(self):
     if self.flag == 1:
        endpoint = "/v1/reacts/private/like"

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
        }

        payload = {
            "contentId": "ce1ac61a-c2e0-4ff8-82fe-2a35973b0d41",
            "reaction": "2210002"
        }

        response = self.client.put(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Update Reaction Successful")
        else:
            self.log.error("Update Reaction Failed")

    @task(4)

    def get_reaction_detail(self):
     if self.flag == 1:
        endpoint = "/v1/reacts/private/likes-detail?contentId=ce1ac61a-c2e0-4ff8-82fe-2a35973b0d41"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("Get Reaction Detail Successful")
        else:
            self.log.error("Get Reaction Detail Failed")

    @task(5)
    def delete_reaction(self):
     if self.flag == 1:
        endpoint = "/v1/reacts/private/like"

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
        }

        payload = {
            "contentId": "ce1ac61a-c2e0-4ff8-82fe-2a35973b0d41"
        }

        response = self.client.delete(endpoint, json=payload, headers=headers)

        if response.status_code == 204:  # Assuming 204 indicates successful deletion
            self.log.info("Delete Reaction Successful")
        else:
            self.log.error("Delete Reaction Failed")
