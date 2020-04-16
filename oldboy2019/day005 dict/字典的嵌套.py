wf = {
    "name":"汪峰",
    "age":"48",
    "成名求":"春天里",
    "wife": {
        "name":"章子怡",
        "age":39,
        "工作":"演员"
    },
    "children": [
        {"num":"001","name":"汪一","hobby":"唱歌"},
        {"num":"002","name":"汪二","hobby":"演戏"}
    ]
}

print(wf["children"][1]["hobby"])
print(wf["wife"]["工作"])

wf["wife"]["age"] = wf["wife"]["age"] + 10
print(wf)

