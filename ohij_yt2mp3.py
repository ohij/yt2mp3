import gradio as gr
from pytubefix import YouTube 
import os

def yt2mp3(url):
    
    # url input from user 
    yt = YouTube(url)

    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 

    # download the file 
    out_file = video.download(output_path='.') 

    unique_out_file = uniquify(out_file)
  
    # save the file as mp3
    base, ext = os.path.splitext(unique_out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    # Get file name and retrun it 
    basename = os.path.basename(new_file)

    return basename

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path

demo = gr.Interface(
    fn=yt2mp3,
    inputs=["text"],
    outputs=["audio"],
    allow_flagging="never"
)

demo.launch()