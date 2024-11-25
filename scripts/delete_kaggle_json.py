import os

def main():
    # delete kaggle json file that was created during the build

    if os.path.exists("kaggle-storage-manager/kaggle.json"):
        os.remove("kaggle-storage-manager/kaggle.json")



if __name__ == "__main__":
    main()
