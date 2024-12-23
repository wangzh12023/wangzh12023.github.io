import gradio as gr

def pace_calculator(minutes, seconds):
    # 将分钟和秒转换为总秒数
    total_seconds = minutes * 60 + seconds
    
    # 计算每200米和400米的平均时间
    pace_200m = total_seconds / (1000 / 200)
    pace_400m = total_seconds / (1000 / 400)
    
    # 计算速度（km/h和m/s）
    speed_kmh = (1000 / total_seconds) * 3.6  # km/h
    speed_ms = 1000 / total_seconds  # m/s
    
    # 返回结果
    return round(pace_200m, 2), round(pace_400m, 2), round(speed_kmh, 2), round(speed_ms, 2)

# 创建 Gradio 界面
demo = gr.Interface(
    fn=pace_calculator,  # 绑定函数
    inputs=[
        gr.Number(label="Minutes", precision=0),  # 输入分钟
        gr.Number(label="Seconds", precision=0)    # 输入秒
    ],
    outputs=[
        gr.Number(label="200m Average Time (s)"),  # 输出每200米配速
        gr.Number(label="400m Average Time (s)"),  # 输出每400米配速
        gr.Number(label="Speed (km/h)"),           # 输出速度 (km/h)
        gr.Number(label="Speed (m/s)")             # 输出速度 (m/s)
    ],
    title="Pace Calculator",
    description="输入你的1000米成绩（分钟和秒），计算每200米和400米的平均时间，以及速度（km/h和m/s）。"
)

# 启动 Gradio
demo.launch()
