from locust import HttpUser, task, between

class GetFollowersAndFollowing(HttpUser):
    host = "https://staging.imlink.network"
    followers_endpoint = "/v1/users/private/follower?page-number=1&items-per-page=20"
    following_endpoint = "/v1/users/private/following?page-number=1&items-per-page=5"
    wait_time = between(1, 3)

    def get_flag_input(self):
        flag = input("Enter flag (1 to execute, 2 to skip): ")
        return int(flag) if flag.isdigit() else None

    def on_start(self):
        # Prompt the user to enter the flag
        self.flag = self.get_flag_input()

    @task
    def get_followers(self):
        if self.flag == 1:
            followers_response = self.client.get(f"{self.host}{self.followers_endpoint}")
            if followers_response.status_code == 200:
                # Successful response handling for followers here
                pass
            else:
                # Handle other responses for followers here
                pass

    @task
    def get_following(self):
        if self.flag == 1:
            following_response = self.client.get(f"{self.host}{self.following_endpoint}")
            if following_response.status_code == 200:
                # Successful response handling for following here
                pass
            else:
                # Handle other responses for following here
                pass
