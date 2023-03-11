import gradio as gr


def input_whitepaper(whitepaper_url):
    """
    This function receives the url for a blockchain's whitepaper,
    sends it to the backend which returns its summary.
    """
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
