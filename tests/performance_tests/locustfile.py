from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def show_summary(self):
        self.client.post('/show_summary', {"email": "TESTLOCUSTclubwith1000points@1000points.com"})

    @task
    def show_booking(self):
        self.client.get('/show_booking/LOCUST Competition with 1000 places/TEST LOCUST club with 1000 points')

    @task
    def booking(self):
        request_form = {
        "club": "TEST LOCUST club with 1000 points",
        "competition": "LOCUST Competition with 1000 places",
        "places": "1"
        }
        self.client.post('/booking', data=request_form)
