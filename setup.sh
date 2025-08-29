set -e

# kalau belum ada venv, bikin
if [ ! -d "venv" ]; then
    echo "🔧 Membuat virtualenv dengan Python 3.11..."
    pyenv install -s 3.10.14
    pyenv local 3.10.14
    python -m venv venv
fi

# aktifkan venv (path relatif ke core)
. venv/bin/activate

# install dependency
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup selesai. Gunakan ./start.sh untuk menjalankan app."
