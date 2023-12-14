import random
import time
import keyboard


from screen_manager import ScreenManager


def run():
    
    total_follows_count = 0
    
    while True:
        if ScreenManager.is_app_focused(app_title_name="linkedin"):
            coordinates = ScreenManager.search_image_on_screen(image_to_search="./testingcut3.png")
            
            for coordinate in coordinates:
#                print(coordinate)
                total_follows_count = total_follows_count + 1
                ScreenManager.click_on_screen(coordinate_to_click=coordinate)
                keyboard.press_and_release('TAB, TAB, TAB, Enter')

                time.sleep(random.randint(1, 2))
            
            
                
            ScreenManager.scroll_on_screen(value_to_scroll=-400)
            time.sleep(random.randint(1, 2))
            print(f"Total de unfollows hasta el momento {str(total_follows_count)}" )
            if keyboard.is_pressed("ESC"):
                print("saliendo del programa Lnkbot")
                break
        
        
run()

"""    dondeclicares = ScreenManager.search_image_on_screen(image_to_search="./unfollow.png")
            for dondeclicar in dondeclicares:
                ScreenManager.click_on_screen(coordinate_to_click=dondeclicar) """
