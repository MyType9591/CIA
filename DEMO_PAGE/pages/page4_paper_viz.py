import gradio as gr
import matplotlib.pyplot as plt

def draw_results():
    fig, ax = plt.subplots()
    models = ['Baseline', 'CIA', 'CIA+']
    hr = [0.25, 0.32, 0.35]
    ndcg = [0.18, 0.24, 0.27]
    x = range(len(models))

    ax.bar(x, hr, width=0.4, label='HR@20')
    ax.bar([i + 0.4 for i in x], ndcg, width=0.4, label='NDCG@20')
    ax.set_xticks([i + 0.2 for i in x])
    ax.set_xticklabels(models)
    ax.legend()
    ax.set_title("실험 결과 비교")

    return fig

def page4_ui():
    with gr.Blocks() as demo:
    with gr.Row():
        # 오버라이드된 profile_box() 호출 → 내 소개만 보임
        profile_box()

        with gr.Column(scale=8):
            gr.Markdown("""
            # SW.Kim's page
            """)

            with gr.Tab("1번 논문"):
                page1_ui()
            with gr.Tab("2번 논문"):
                page2_ui()
            with gr.Tab("3번 논문"):
                page3_ui()

