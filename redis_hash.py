# _*_ coding=utf-8 _*_

import redis
from Interview.Redis.RedisPool.redis_pool import pool

r = redis.Redis(connection_pool=pool)

# hset(key,field,value) 为设置field指定值，若key不存在，则创建
r.hset('dic', 'a', 1)
# hmset(key,{field1:value1,field2:value2....}),设置多个字段的值
r.hmset('dic', {'b': 1, 'c': 2})
# hgetall(key),获取key内所有字段的值
print(r.hgetall('dic'))
