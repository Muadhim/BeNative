import sys
import json

def handle_message(message):
    action = message.get("action")
    if action == "echo":
        return {"action": "echo", "result": f"Echo: {message.get('payload')}"}
    elif action == "speech_to_text":
        # Dummy response (nanti bisa diganti Whisper)
        return {"action": "speech_to_text", "result": "Hello, how are you?"}
    else:
        return {"error": "Unknown action"}

def main():
    for line in sys.stdin:  # baca dari Electron (stdin)
        try:
            message = json.loads(line.strip())
            response = handle_message(message)
            print(json.dumps(response))
            sys.stdout.flush()  # penting biar langsung terkirim ke Electron
        except Exception as e:
            error_msg = {"error": str(e)}
            print(json.dumps(error_msg))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
