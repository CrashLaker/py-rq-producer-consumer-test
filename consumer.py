from redis import Redis
from rq import Queue, Worker
from foo import bar

def main():
    redis = Redis("172.17.0.7", 6379, "")
    queue = Queue("queue", connection=redis)
    worker = Worker([queue], connection=redis, name='foo')
    worker.work()


if __name__ == '__main__':
    main()
