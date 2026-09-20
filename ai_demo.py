# 简易文本情感分析Demo
def sentiment_analysis(text):
    positive = {"开心", "好", "很棒", "满意", "喜欢"}
    negative = {"难过", "差", "糟糕", "讨厌", "失望"}
    score = 0
    for word in positive:
        if word in text:
            score += 1
    for word in negative:
        if word in text:
            score -= 1
    if score > 0:
        return "积极情感"
    elif score < 0:
        return "消极情感"
    else:
        return "中性情感"

if __name__ == "__main__":
    print("===简易情感分析AI Demo===")
    while True:
        content = input("请输入文本（输入exit退出）：")
        if content == "exit":
            print("程序结束")
            break
        result = sentiment_analysis(content)
        print(f"分析结果：{result}\n")
