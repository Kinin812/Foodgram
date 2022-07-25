import io

from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

FILENAME = 'shoppingcart.pdf'


def draw_pdf(shopping_cart):
    buffer = io.BytesIO()
    page = canvas.Canvas(buffer)
    pdfmetrics.registerFont(TTFont(
        'YakumoPreschoolHand',
        'YakumoPreschoolHand.ttf', 'UTF-8'
    ))
    x_position, y_position = 50, 800
    page.setFillColorRGB(255, 0, 0)
    page.setFont('YakumoPreschoolHand', 14)
    if shopping_cart:
        indent = 20
        page.drawString(x_position, y_position, 'Артем, привет!')
        y_position -= 25
        page.drawString(
            x_position, y_position,
            'Очистка списка покупок после скачивания файла не соответствует'
        )
        y_position -= 15
        page.drawString(
            x_position, y_position,
            'методологии HTTP, определенной протоколом RFC 2616, а именно:'
        )
        y_position -= 15
        page.drawString(
            x_position, y_position,
            'GET (метод указан в ТЗ) — применяется, чтобы получить ресурс.'
        )
        y_position -= 40
        page.setFillColorRGB(0, 0, 0)
        page.setFont('YakumoPreschoolHand', 14)
        page.drawString(x_position, y_position, 'Cписок покупок:')
        for index, recipe in enumerate(shopping_cart, start=1):
            page.drawString(
                x_position, y_position - indent,
                f'{index}. {recipe["ingredients__name"]} - '
                f'{recipe["amount"]} '
                f'{recipe["ingredients__measurement_unit"]}.')
            y_position -= 15
            if y_position <= 50:
                page.showPage()
                y_position = 800
        page.save()
        buffer.seek(0)
        return FileResponse(
            buffer, as_attachment=True, filename=FILENAME)
    page.setFont('YakumoPreschoolHand', 24)
    page.drawString(
        x_position,
        y_position,
        'Cписок покупок пуст!')
    page.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=FILENAME)
