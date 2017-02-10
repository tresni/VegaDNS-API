import redis
import threading
import time
import subprocess


class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    def work(self, item):
        print subprocess.check_output(
            ["/etc/update-data.sh"],
            stderr=subprocess.STDOUT
        )

    def run(self):
        for item in self.pubsub.listen():
            self.work(item)

if __name__ == "__main__":
    r = redis.Redis(host="10.112.0.82")
    client = Listener(r, ['VEGADNS-CHANGES'])
    client.start()
