from io import BytesIO

from pathlib import Path

from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image, ImageOps


def compress_image_to_webp(image_field, max_size=(800, 800), quality=85):
    if not image_field:
        return None

    img = Image.open(image_field)

    img = ImageOps.exif_transpose(img)

    if img.mode in ("RGBA", "P", "LA"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1] if "A" in img.mode else None)
        img = background
    elif img.mode != "RGB":
        img = img.convert("RGB")

    img.thumbnail(max_size, Image.Resampling.LANCZOS)

    output = BytesIO()

    img.save(output, format="WEBP", quality=quality, optimize=True)

    output.seek(0)

    new_name = f"{Path(image_field.name).stem}.webp"

    return InMemoryUploadedFile(
        file=output,
        field_name=image_field.field.name,
        name=new_name,
        content_type="image/webp",
        size=output.getbuffer().nbytes,
        charset=None,
    )
