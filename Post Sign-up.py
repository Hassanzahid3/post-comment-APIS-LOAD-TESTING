from locust import HttpUser, task, between

class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)
    flag = 1  # Set the flag here