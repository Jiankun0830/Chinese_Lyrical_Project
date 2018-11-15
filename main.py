from config import *
import data
import model

def defineArgs():
    """define args"""
    parser = argparse.ArgumentParser(description = "Chinese_poem_generator.")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test", "head"], default = "test")
    return parser.parse_args()

if __name__ == "__main__":
    args = defineArgs()
    trainData = data.POEMS(trainPoems)
    SmartWriter = model.MODEL(trainData)
    if args.mode == "train":
        SmartWriter.train()
    else:
        if args.mode == "test":
            poems = SmartWriter.test()
        else:
            characters = input("please input chinese character:")
            poems = SmartWriter.testHead(characters)
