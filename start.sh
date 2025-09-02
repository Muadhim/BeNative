set -e

# Jalankan AI core
. venv/bin/activate
python main.py &
CORE_PID=$!

# Pastikan Ctrl+C berhenti juga di child
trap "kill $CORE_PID 2>/dev/null" INT TERM

# Tunggu exit child
wait $CORE_PID
