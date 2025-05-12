import flet as ft
import random

def main(page):
    jokes = [
        "Why dont skeletons fight each other? because they dont have the guts!",
        "What do you call a fake noodle? an impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How do you organize a space party? You planet!",
        "Why did the math book look sad? Because it had too many problems.",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why can't your nose be 12 inches long? Because then it would be a foot!",
        "What is brown and sticky? A stick!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "How do you make a tissue dance? Put a little boogie in it!"
    ]
    
    joke_sheet = ft.BottomSheet(
        ft.Container(
            ft.Column([
                ft.Text("Here's your joke:", size=20),
                ft.Text("", size=16, weight="bold"),
                ft.ElevatedButton("Close", on_click=lambda _: joke_sheet.dismiss())
            ], tight=True),
            padding=20
        ),
        open=False
    )
    
    page.overlay.append(joke_sheet)
    
    def tell_joke(e):
        random_joke = random.choice(jokes)
        joke_sheet.content.controls[1].value = random_joke
        joke_sheet.open = True
        page.update()
    
    page.add(
        ft.Column([
            ft.Text("Bad Joke Generator", size=24),
            ft.ElevatedButton("Tell me a joke!", 
                            on_click=tell_joke,
                            icon=ft.icons.EMOJI_EMOTIONS)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)