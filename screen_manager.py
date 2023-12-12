import logging
import pyautogui                                        
import cv2
import win32gui




class ScreenManager:

    @staticmethod
    def is_app_focused(app_title_name: str):
        active_window_title = win32gui.GetWindownText(win32gui.GetForegroundWindow()).lower()
        return app_title_name in active_window_title

    @staticmethod
    def search_image_on_screen(image_to_search: str):
        try:
           return pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)        
        except Exception as ex:
            logging.info(f"No se ha encontrado la imagen. Error: {ex}")