from redis import Redis
from rq import Queue, use_connection
from foo import bar

host = "172.17.0.7"
port = 6379
pwd = ""
import time
def main():
    redis = Redis(host, port, pwd)
    #use_connection(redis)
    q = Queue('queue', connection=redis)
    job = q.enqueue(bar, 2)
    rs = job.result
    print(rs)
    time.sleep(3)
    rs = job.result
    print(rs)

    jobs = [q.enqueue(bar, i) for i in range(100)]
    for i, job in enumerate(jobs):
        print(i, rs)
        rs = job.result
        while rs is None:
            rs = job.result
            time.sleep(1)
        print(rs)
    #redis.set("a", "hello")
    #msg = redis.get("a")
    #print(msg)


if __name__ == '__main__': 
    main()

