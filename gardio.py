import gradio as gr
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Initialize the agent
multimodal_Agent = Agent(
    name="Video AI Summarizer",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo()],
    markdown=True,
)

def process_video(video_path, user_query):
    if not user_query:
        return "Please enter a question or insight to analyze the video."
    
    try:
        # Upload and process video file
        processed_video = upload_file(video_path)
        while processed_video.state.name == "PROCESSING":
            time.sleep(1)
            processed_video = get_file(processed_video.name)

        # Prompt generation for analysis
        analysis_prompt = f"""
        Analyze the uploaded video for content and context.
        Respond to the following query using video insights and supplementary web research:
        {user_query}

        Provide a detailed, user-friendly, and actionable response.
        """

        # AI agent processing
        response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])
        return response.content

    except Exception as error:
        return f"An error occurred during analysis: {error}"
    finally:
        # Clean up temporary video file
        if video_path:
            Path(video_path).unlink(missing_ok=True)

# Create Gradio interface
with gr.Blocks(title="Multimodal AI Agent- Video Summarizer") as demo:
    gr.Markdown("# Phidata Video AI Summarizer Agent 🎥🎤🖬")
    gr.Markdown("## Powered by Gemini 2.0 Flash Exp")
    
    with gr.Row():
        video_input = gr.Video(label="Upload a video file")
        
    with gr.Row():
        query_input = gr.Textbox(
            label="What insights are you seeking from the video?",
            placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
            lines=3
        )
    
    with gr.Row():
        analyze_button = gr.Button("🔍 Analyze Video")
    
    with gr.Row():
        output = gr.Markdown(label="Analysis Result")

    analyze_button.click(
        fn=process_video,
        inputs=[video_input, query_input],
        outputs=output
    )

# Launch the application
if __name__ == "__main__":
    demo.launch()
