"""令牌桶：补充、放行与重试：待实现的核心模块。"""


def refill(bucket, now, rate, capacity):
    """补充令牌。"""
    raise NotImplementedError

def allow(bucket, cost, now, rate, capacity):
    """放行判断。"""
    raise NotImplementedError

def retry_after(bucket, cost, rate):
    """重试等待。"""
    raise NotImplementedError

def consume(bucket, cost):
    """扣令牌。"""
    raise NotImplementedError

def bucket_key(user, route):
    """限流键。"""
    raise NotImplementedError
