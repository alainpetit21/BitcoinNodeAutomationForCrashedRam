# ======================================================================================================================
# main.py : entry point script for this example

# ======================================================================================================================
# importing internal modules
from Src.Controller.AppBitCoinNodeAutomationForCrashedRam import AppBitCoinNodeAutomationForCrashedRam


if __name__ == "__main__":
    print("Hello AppBitCoinNodeAutomationForCrashedRam World")

    objApp = AppBitCoinNodeAutomationForCrashedRam()

    objApp.load()
    objApp.main()
