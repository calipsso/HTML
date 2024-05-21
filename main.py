from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recept: Špagety Carbonara</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header, footer {
            background-color: #f8b400;
            color: white;
            text-align: center;
            padding: 1em 0;
        }
        main {
            padding: 20px;
        }
        h1 {
            margin-bottom: 0.5em;
        }
        section {
            margin-bottom: 1em;
        }
        ul, ol {
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Špagety Carbonara</h1>
    </header>
    <main>
        <section>
            <h2>Ingrediencie</h2>
            <ul>
                <li>200 g špagiet</li>
                <li>100 g slaniny</li>
                <li>2 vajcia</li>
                <li>50 g strúhaného parmezánu</li>
                <li>2 strúčiky cesnaku</li>
                <li>Soľ a čierne korenie</li>
            </ul>
        </section>
        <section>
            <h2>Postup</h2>
            <ol>
                <li>Špagety uvaríme podľa návodu na obale.</li>
                <li>Slaninu nakrájame na malé kúsky a opečieme na panvici.</li>
                <li>Vajcia rozšľaháme a zmiešame so strúhaným parmezánom.</li>
                <li>Uvarené špagety pridáme na panvicu k slanine a premiešame.</li>
                <li>Panvicu odstavíme z ohňa, pridáme vaječnú zmes a dobre premiešame.</li>
                <li>Dochutíme soľou a čiernym korením podľa chuti.</li>
                <li>Servírujeme ihneď.</li>
            </ol>
        </section>
    </main>
    <footer>
        <p>Vytvorené: 20. máj 2024</p>
        <p>&copy; 2024 Tvoje Meno</p>
    </footer>
</body>
</html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
