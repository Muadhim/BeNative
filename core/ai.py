import subprocess

def ask_ollama(prompt: str, model="llama3.2"):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"(Error contacting Ollama: {e})"
