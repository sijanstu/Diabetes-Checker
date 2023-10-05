from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# load image from the IAM database (actually this model is meant to be used on printed text)
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')


def get_captcha():
    id_url = "https://tms16.nepsetms.com.np/tmsapi/authApi/captcha/id"-
    captcha_id = requests.get(id_url).json()["data"]["id"]
    print(captcha_id)
    captcha_url = f"https://tms16.nepsetms.com.np/tmsapi/authApi/captcha/image/{captcha_id}"
    captcha1 = requests.get(captcha_url).content
    with open(captcha_id + ".png", "wb") as f:
        f.write(captcha1)
    return Image.open(captcha_id + ".png").convert("RGB")


def solve_captcha(image):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values, max_new_tokens=1000)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]


if __name__ == '__main__':
    for i in range(20):
        captcha = get_captcha()
        captcha_text = solve_captcha(captcha)
        print(captcha_text)
        captcha.close()
