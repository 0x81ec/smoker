
import redis
import json
if __name__ == "__main__":
    keyword = input("input keywords")

    red = redis.Redis(host="127.0.0.1", port=6379, db=0)

    red.lpush("movies", "")
    red.hset("123")
   #  list = red.lrange("smoke:items",0,-1)
   #
   # # print(len(list))
   #  result  = []
   #
   #  for li in list:
   #     data = json.loads(li.decode())
   #     if keyword in data["name"]:
   #         print(data)
   #         result.append(data)
   #     else:
   #         pass
   #  for r in result:
   #      print(r)

    