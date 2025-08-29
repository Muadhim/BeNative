set -e

# Jalankan AI core
cd core
. venv/bin/activate
python main.py &
CORE_PID=$!

# Jalankan Electron UI
cd ../ui
npm install &
npm start &

# Tunggu exit
wait $CORE_PID
