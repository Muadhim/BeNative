set -e

# Jalankan AI core
. venv/bin/activate
python main.py &
CORE_PID=$!

# Tunggu exit
wait $CORE_PID
