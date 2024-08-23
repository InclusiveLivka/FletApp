import logging
import os
import base64
from typing import List, Optional
import flet as ft
from web.ui.elements import UIConstants
from web.database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_new_product(
    name: str,
    price: str,
    description: str,
    category: str,
    encoded_image: str
) -> None:
    """
    Adds a new product to the database.

    :param name: Product name.
    :param price: Product price.
    :param description: Product description.
    :param category: Product category.
    :param encoded_image: Encoded image data.
    """
    engine.add_product(name, price, description, category, encoded_image)
    logger.info(f"Product added: {name}, Category: {category}")


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
        UIConstants.ENCODED_IMAGE.value = encoded_string

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
    file_picker = setup_file_picker(page)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Product add"),
                UIConstants.NAME_PRODUCT,
                UIConstants.PRICE_PRODUCT,
                UIConstants.DESCRIPTION_PRODUCT,
                UIConstants.get_category_dropdown_options(),
                ft.Row(
                    controls=[
                        ft.FloatingActionButton(
                            text="Добавить продукт",
                            width=150,
                            on_click=lambda e: add_new_product(
                                UIConstants.NAME_PRODUCT.value,
                                UIConstants.PRICE_PRODUCT.value,
                                UIConstants.DESCRIPTION_PRODUCT.value,
                                UIConstants.CATEGORY_NAME_FIELD.value,
                                UIConstants.ENCODED_IMAGE.value
                            )
                        ),
                        ft.FloatingActionButton(
                            icon=ft.icons.IMAGE,
                            on_click=lambda _: file_picker.pick_files(),
                        )
                    ],
                ),
                UIConstants.ENCODED_IMAGE,
            ]
        )
    )
