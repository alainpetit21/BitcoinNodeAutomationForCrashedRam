from Src.CrossCuttingConcerns.App import App
import pyautogui as pk_py_auto_gui
import time


class AppBitCoinNodeAutomationForCrashedRam(App):
    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. I does not do a lot but, overload the BaseClass
            construction call and initialization the class attributes for this instance.
        """
        super().__init__("AppBitCoinNodeAutomationForCrashedRam")


    def load(self):
        """ load Description : (public visibility) :
            Method that is called directly after the creation of the object. Its purpose is to do all loading that is
            beside initial initialization.
        """
        pk_py_auto_gui.PAUSE = 1
        pk_py_auto_gui.FAILSAFE = True


    def main(self, param1= None):
        """ main Description : (public visibility) :
            The main function of this Applicaiton objet.
        """

        # pyautogui.position()

        try:
            while True:
                pk_py_auto_gui.moveTo(100, 100, duration=2)
                # pk_py_auto_gui.typewrite('bitcoin-qt -datadir=/home/pi/SSD_1Tb/bitcoinData')
                # pk_py_auto_gui.typewrite(['enter']
                pk_py_auto_gui.moveTo(600, 200, duration=2)
                # time.sleep(2*60*60)
                time.sleep(2*60)
                # pk_py_auto_gui.click(600, 200)

        except KeyboardInterrupt:
            print('\nDone.')