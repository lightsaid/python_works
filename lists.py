# 定义 列表
bicycles = ["永久", "凤凰", "美利达", "喜德盛", "飞鸽"]
print(bicycles)

# 访问列表元素
print(bicycles[0])
# print(bicycles[5])  下表越界： list index out of range
print(bicycles[-1].title()) # 飞鸽

message = f"我家有一辆古老的{bicycles[1]}牌自行车。"
print(message)


# 修改、添加和删除元素

# TODO: 3.2 修改、添加和删除元素