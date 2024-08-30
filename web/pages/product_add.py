import logging
import os
import base64
from typing import List, Optional
import flet as ft
from web.ui.elements import UIConstants
from web.ui import error_image
from web.database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_new_product(
    name: str,
    price: int,
    currency: str,
    description: str,
    category: str,
    encoded_image: str,
    page
) -> None:
    """
    Adds a new product to the database.

    :param name: Product name.
    :param price: Product price.
    :param description: Product description.
    :param category: Product category.
    :param encoded_image: Encoded image data.
    """

    dlg_modal_name = ft.AlertDialog(
        content=ft.Text("Название не может быть пустым!"),
        actions=[ft.TextButton(
            "ОК", on_click=lambda e: page.close(dlg_modal_name))],
    )
    dlg_modal_category = ft.AlertDialog(
        content=ft.Text("Категория не может быть пустой!"),
        actions=[ft.TextButton(
            "ОК", on_click=lambda e: page.close(dlg_modal_category))],
    )
    dlg_modal_add_product = ft.AlertDialog(
        content=ft.Text("Продукт успешно добавлен!"),
        actions=[ft.TextButton(
            "ОК", on_click=lambda e: page.close(dlg_modal_add_product))],
    )

    if UIConstants.NAME_PRODUCT.value == '':
        page.open(dlg_modal_name)
    elif UIConstants.CATEGORY_NAME.value == None:
        page.open(dlg_modal_category)
    else:
        if UIConstants.PRICE_PRODUCT.value == "":
            price = "Не указана!"
            currency = ''
        
        category = engine.read_link_of_name_category(category)[0]
        engine.add_product(name, price, currency, description, category, encoded_image)
        logger.info(f"Product added: {name}, Category: {category}")
        UIConstants.NAME_PRODUCT.value = ''
        UIConstants.PRICE_PRODUCT.value = ''
        UIConstants.DESCRIPTION_PRODUCT.value = ''
        UIConstants.CATEGORY_NAME.value = ''
        UIConstants.ENCODED_IMAGE_PRODUCT.value = error_image.image_scr
        page.open(dlg_modal_add_product)
        if UIConstants.CHEKBOX.value:
            page.go('/adminhome')
    page.update()


def encode_image_to_base64(
    update: ft.FilePickerUploadEvent,
) -> str:
    """
    Encodes the image at the given file path to Base64 format and deletes the
    file.

    :param file_picker: The FilePicker instance that triggered the upload.
    :param page: The current Flet page instance.
    :return: The encoded image data.
    """
    if update.progress == 1:
        file_path = os.path.join("uploads", update.file_name)

        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()
            ).decode('utf-8')
        os.remove(file_path)
        UIConstants.ENCODED_IMAGE_PRODUCT.value = encoded_string

        logger.info(f"File uploaded and encoded: {update.file_name}")


def generate_upload_list(
    page: ft.Page,
    files: Optional[List[ft.FilePickerFileType]]
) -> List[ft.FilePickerUploadFile]:
    """
    Generates a list of files to be uploaded with their corresponding upload
    URLs.

    :param page: The current Flet page instance.
    :param files: List of files selected by the user through FilePicker.
    :return: List of FilePickerUploadFile objects ready for uploading.
    """
    upload_list = []
    if files:
        for file in files:
            upload_url = page.get_upload_url(file.name, 600)
            upload_list.append(ft.FilePickerUploadFile(
                file.name, upload_url=upload_url)
            )
    return upload_list


def upload_files(file_picker: ft.FilePicker, page: ft.Page) -> None:
    """
    Handles the uploading of files selected through the FilePicker.

    :param file_picker: The FilePicker instance that triggered the upload.
    :param page: The current Flet page instance.
    """
    if file_picker.result and file_picker.result.files:
        upload_list = generate_upload_list(page, file_picker.result.files)
        file_picker.upload(upload_list)


def setup_file_picker(page: ft.Page) -> ft.FilePicker:
    """
    Sets up the file picker for the page.

    :param page: The Flet page object.
    """
    file_picker = ft.FilePicker(
        on_result=lambda _: upload_files(file_picker, page),
        on_upload=encode_image_to_base64,
    )
    page.overlay.append(file_picker)
    logger.info("File picker setup completed")
    return file_picker


def create_page(page: ft.Page) -> ft.Container:
    """
    Create the product add page view with fields to add a new product.

    :param page: An instance of ft.Page to create the product add page for.
    :return: A Flet Container with controls for adding a product.
    """
    page.clean
    file_picker = setup_file_picker(page)
    UIConstants.CATEGORY_NAME.options = [
        ft.dropdown.Option(category[0]) for category in engine.read_categories()
    ]

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[                   
                ]),
                UIConstants.NAME_PRODUCT,
        ft.Row(controls=[
                UIConstants.PRICE_PRODUCT,
                UIConstants.CURRENCY_FIELD
            ]),
                UIConstants.DESCRIPTION_PRODUCT,
                UIConstants.CATEGORY_NAME,
                UIConstants.CHEKBOX,
                ft.Row(
                    controls=[
                        ft.FloatingActionButton(
                            text="Добавить продукт",
                            width=259,
                            on_click=lambda e: add_new_product(
                                UIConstants.NAME_PRODUCT.value,
                                UIConstants.PRICE_PRODUCT.value,
                                UIConstants.CURRENCY_FIELD.value,
                                UIConstants.DESCRIPTION_PRODUCT.value,
                                UIConstants.CATEGORY_NAME.value,
                                UIConstants.ENCODED_IMAGE_PRODUCT.value,
                                page
                            )
                        ),
                        ft.FloatingActionButton(
                            icon=ft.icons.IMAGE,
                            width=94,
                            on_click=lambda _: file_picker.pick_files(),
                        )
                    ],
                ),
                UIConstants.ENCODED_IMAGE_PRODUCT,
            ]
        )
    )
