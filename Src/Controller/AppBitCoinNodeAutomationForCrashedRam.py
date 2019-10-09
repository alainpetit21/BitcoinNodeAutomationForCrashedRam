from Src.CrossCuttingConcerns.App import App
import pyautogui as pk_py_auto_gui
import time as pk_time


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
        pk_py_auto_gui.FAILSAFE = False

    def main(self, param1=None):
        """ main Description : (public visibility) :
            The main function of this Applicaiton objet.
        """

        # pyautogui.position()

        try:
            while True:
                print("\nRestarting Time now" + str(pk_time.time()))

                print("\nPerforming moveTo(150, 150, duration=2)")
                pk_py_auto_gui.moveTo(150, 150, duration=2)

                print("\nPerforming click(150, 150");
                pk_py_auto_gui.click(150, 150)

                print("\nPerforming typewrite('bitcoin-qt -datadir=/home/pi/SSD_1Tb/bitcoinData')");
                pk_py_auto_gui.typewrite('bitcoin-qt -datadir=/home/pi/SSD_1Tb/bitcoinData')

                print("\nPerforming press('enter')");
                pk_py_auto_gui.press('enter')

                print("\nPerforming sleep(3 * 60)");
                # pk_time.sleep(2)
                pk_time.sleep(3 * 60)
                # pk_time.sleep(2*60*60)

                print("\nPerforming click(150, 150)");
                pk_py_auto_gui.click(150, 150)

                print("\nPerforming hotkey('ctrl', 'c')");
                pk_py_auto_gui.hotkey('ctrl', 'c')

                print("\nPerforming sleep(10 * 60)");
                pk_time.sleep(10 * 60)

        except KeyboardInterrupt:
            print('\nDone.')