import gradio as gr

def input_whitepaper(whitepaper_url):
    # print(whitepaper_url)
    # call summarize function and return summary
    summary = ""
    return f"These are the keypoints: \n {summary}"

def compare_whitepapers(*args):
    pass

demo = gr.Interface(fn=input_whitepaper,
                    inputs="text",  
                    outputs="text")

# print(demo)

demo.launch()
