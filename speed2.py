import gradio as gr

def pace_calculator(distance = 1, hours = 0, minutes = 0, seconds = 0):
  distance *= 1000
  total_seconds = hours * 3600 + minutes * 60 + seconds
  pace_100m_s = (total_seconds / (distance / 100) ) % 60
  pace_100m_m = (total_seconds / (distance / 100)) // 60  
  pace_200m_s = (total_seconds / (distance / 200) ) % 60
  pace_200m_m = (total_seconds / (distance / 200) ) // 60
  pace_400m_s = (total_seconds / (distance / 400) ) % 60
  pace_400m_m = (total_seconds / (distance / 400) ) // 60
  pacce_mkm_m = (total_seconds / distance* 1000 ) // 60
  pace_mkm_s = (total_seconds / distance * 1000) % 60
  speed_kmh = (1000 / total_seconds) * 3.6  
  speed_ms = 1000 / total_seconds  

  return round(pace_100m_m, 0), round(pace_100m_s, 0), round(pace_200m_m, 0), round(pace_200m_s, 0), round(pace_400m_m, 0), round(pace_400m_s, 0), round(pacce_mkm_m, 0), round(pace_mkm_s, 0) ,round(speed_kmh, 0), round(speed_ms, 0)

def demo(pace_calculator):
  # Add CSS style to make the button orange
  css = """
  .submit-btn {
    background-color: orange !important;
    color: white !important;
  }
  """
  with gr.Blocks(title="Pace changer",css=css) as demo:
    with gr.Row():
      gr.Markdown('<h1><center>Pace changer</center></h1>')
    with gr.Row():
      with gr.Column(scale=0.3):
        with gr.Row():
          distance = gr.Slider(0, 42, step=1, label="Distance (km)")
        with gr.Row():
          hours_slider = gr.Slider(0, 60, step=1, label="Hours")
        with gr.Row():
          minutes_slider = gr.Slider(0, 100, step=1, label="Minutes")
          seconds_slider = gr.Slider(0, 59, step=1, label="Seconds")
        with gr.Row():
          submit = gr.Button('Submit', elem_classes="submit-btn")
          
      with gr.Column(scale=0.7):
        with gr.Row():
          gr.Markdown("### Results")
        with gr.Row():
          pace_100m_m = gr.Textbox(label="100m Average Time (min):")
          pace_100m_s = gr.Textbox(label="100m Average Time (s):")
        with gr.Row():
          pace_200m_m = gr.Textbox(label="200m Average Time (min):")
          pace_200m_s = gr.Textbox(label="200m Average Time (s):")
        
        with gr.Row():
          pace_400m_m = gr.Textbox(label="400m Average Time (min):")
          pace_400m_s = gr.Textbox(label = "400m Average Time (s):")
        with gr.Row():
          speed_mkm_m = gr.Textbox(label = "Pace per kilometer (min/km) minutes:")
          speed_mkm_s = gr.Textbox(label = "Pace per kilometer (min/km) seconds:")
        with gr.Row():
          
          speed_kmh = gr.Textbox(label = "Speed (km/h):")
        with gr.Row():
          
          speed_ms = gr.Textbox(label = "Speed (m/s):")

    submit.click(pace_calculator,
                  [distance,hours_slider ,minutes_slider, seconds_slider],
                  [pace_100m_m, pace_100m_s, pace_200m_m, pace_200m_s, pace_400m_m, pace_400m_s, speed_mkm_m,speed_mkm_s , speed_kmh, speed_ms])


    demo.launch()  


if __name__ == '__main__':
  demo(pace_calculator)