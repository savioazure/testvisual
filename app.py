from screen_manager import ScreenManager

def run():
    while True:
        coordinates = ScreenManager.get_all_matches_by_image(image_to_search="./Screenshot_2023-12-12_03_05_48.png")
        for coordinate in coordinates:
            print(coordinate)

            
run()