import typer

app = typer.Typer()

@app.command()
def start():
    print("Judgement started!")

if __name__ == "__main__":
    app()