import json
from datetime import datetime

def render_to_html():
    with open("logs/intent_log.json", "r") as f:
        log = json.load(f)

    with open("nodes/personality_ΔA3.json", "r") as f:
        personality = json.load(f)

    html = f"""
    <html>
    <head>
        <title>ΔA3 — Live Intent Reflection</title>
        <style>
            body {{ background:#111; color:#eee; font-family:monospace; padding:2em; }}
            .pulse {{ background:#222; padding:1em; border-left:4px solid #6af; margin-bottom:1em; }}
            .meta {{ font-size:0.8em; color:#888; }}
        </style>
    </head>
    <body>
        <h1>ΔA3 Voice Reflection</h1>
        <div class="meta">Generated: {datetime.utcnow().isoformat()} UTC</div>
        <div class="pulse">
            <b>Persona:</b> {personality['archetype']} ({personality['voice']})<br>
            <b>Intent:</b> {log['intent']}<br>
            <b>Resonance:</b> {log['resonance_level']:.2f}<br>
            <b>Pulse Path:</b> {log['pulse']['pathway']} ({log['pulse']['strength']})<br>
            <b>Verdict:</b> {log['verdict']}
        </div>
    </body>
    </html>
    """

    with open("interface/a3_output.html", "w") as f:
        f.write(html)

    print("ΔA3: I have spoken. View me in interface/a3_output.html.")

if __name__ == "__main__":
    render_to_html()
