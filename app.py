from screen_manager import ScreenManager

def run():
    while True:
        if ScreenManager.is_app_focused(app_title_name="linkedin"):
            coordinates = ScreenManager.search_image_on_screen(image_to_search="./testingcut3.png")
            for coordinate in coordinates:
                print()

            
run()