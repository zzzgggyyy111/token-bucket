# 令牌桶：补充、放行与重试

限流在突发流量下把请求全放过去、限流后重试时间算错：补充没有按时间差，容量没有封顶，放行没有扣令牌，拒绝后没有保留余量，重试时间除零，空桶崩，批量限流只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
net/__init__.py
net/token_bucket.py
tests/test_token_bucket.py
```

## 当前状态

`net/token_bucket.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_token_bucket.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 按时间差补充
2. 容量封顶
3. 放行扣令牌
4. 拒绝保留余量
5. 重试时间除零
6. 空桶兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `net/token_bucket.py`
后 15 条用例应全部通过。
