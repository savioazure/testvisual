import logging
import pyautogui                                        
import cv2
import win32gui




class ScreenManager:

    @staticmethod
    def is_app_focused(app_title_name: str):
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
        #print("\n\n" + active_window_title)
        return app_title_name in active_window_title
    
    @staticmethod
    def click_on_screen(coordinate_to_click: int):
        pyautogui.click(coordinate_to_click)
        
    @staticmethod
    def scroll_on_screen(value_to_scroll: int):
        pyautogui.scroll(value_to_scroll)

    @staticmethod
    def search_image_on_screen(image_to_search: str):
        try:
           return pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)        
        except Exception as ex:
            logging.info(f"No se ha encontrado la imagen. Error: {ex}")