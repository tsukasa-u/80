from PIL import Image

filename = "nisshouki.png"
imgPIL = Image.open(filename)  # 画像読み込み

imgPIL.show()  # 画像表示