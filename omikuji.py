import random
import gradio as gr  # type: ignore


def get_fortune(your_name: str):
    fortune_list = ["大吉", "中吉", "小吉", "凶", "大凶"]
    fortune_result = random.choice(fortune_list)
    return your_name + "さんの今日の運勢は" + fortune_result + "です！"


demo = gr.Interface(fn=get_fortune, inputs="text", outputs="text")
demo.launch()
