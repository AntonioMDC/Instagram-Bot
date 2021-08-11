from InstagramBot import * 

def main():
    bot = InstagramBot()
    bot.login()
    bot.upload_photo("/test_images/test.jpg")

if __name__ == "__main__":
    main()