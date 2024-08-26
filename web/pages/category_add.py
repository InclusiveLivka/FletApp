import logging
import flet as ft
import os
import base64
from web.database import engine
from web.ui.elements import UIConstants
from typing import List,Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_new_category(category_name: str , encoded_image: str, page):
    """
    Adds a new category to the database.

    :param category_name: Name of the new category.
    """
    engine.add_category(category_name,encoded_image)
    logger.info(f"New category added: {category_name}")
    UIConstants.CATEGORY_NAME_FIELD.value = ""
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
        UIConstants.ENCODED_IMAGE_CATEGORY.value = encoded_string
        
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
    Create the category add page view with a field to add a new category.

    :param page: An instance of ft.Page to create the category add page for.
    :return: A Flet Container with controls for adding a category.
    """

    file_picker = setup_file_picker(page)

    return ft.Container(
        content=ft.Column(
            controls=[
                UIConstants.CATEGORY_NAME_FIELD,
                ft.Row(
                    controls=[
                        ft.FloatingActionButton(
                            text="Добавить категорию",
                            width=300,
                            on_click=lambda e: add_new_category(
                                UIConstants.CATEGORY_NAME_FIELD.value,
                                UIConstants.ENCODED_IMAGE_CATEGORY.value,
                                page,
                                )
                        ),
                            ft.FloatingActionButton(
                                icon=ft.icons.IMAGE,
                                width=89,
                                on_click=lambda e: file_picker.pick_files(),
                        ),
                    ],
                        
                ),
                ft.FloatingActionButton(
                            text="Далее",
                            on_click=lambda _: page.go('/productadd'),
                            width=399,
                            
                            
                            ),
                UIConstants.ENCODED_IMAGE_CATEGORY
            ]
        )
    )
