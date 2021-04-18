from fastapi import FastAPI, BackgroundTasks
from datetime import datetime

app = FastAPI()


def write_notification(card_id: str):
    with open("/var/log/cards.csv", mode="a") as logfile:
        content = f"{datetime.now()},{card_id}\n"
        logfile.write(content)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/cards/{card_id}")
async def write_card(card_id: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, card_id)
    return {"card_id": card_id}