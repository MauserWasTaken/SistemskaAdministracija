# Uporabi osnovno sliko z namestitvijo Pythona
FROM python:3.9

# Kopiraj celotno vsebino trenutnega direktorija v /app v Docker zabojniku
COPY . /app

# Nastavi delovni imenik na /app
WORKDIR /app

# Namesti potrebne pakete
RUN pip install --upgrade pip



# Ko se kontejner zažene, poženi program
CMD ["python", "main.py"]

