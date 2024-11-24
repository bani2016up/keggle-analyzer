import os

def main():
    # delete kaggle json file that was created during the build

    if os.path.exists("kaggle-api/kaggle.json"):
        os.remove("kaggle-api/kaggle.json")



if __name__ == "__main__":
    main()
