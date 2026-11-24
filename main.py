import os
import shutil
if not os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"): os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/")
def main():
    shutil.copy2(os.path.dirname(__file__) + "/entry.png", os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.png")
    print("Created output directory and copied entry.png")
if __name__ == "__main__":
    main()
