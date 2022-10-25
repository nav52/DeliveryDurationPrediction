echo [$(date)]: "START"
echo [$(date)]: "Creating environment with Python 3.8"
conda create -p venv python=3.8 -y
echo [$(date)]: "Activate the environment"
conda activate venv/
echo [$(date)]: "Installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"