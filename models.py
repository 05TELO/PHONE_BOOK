from typing import Optional

from pydantic import BaseModel


class Contact(BaseModel):
    Имя: str
    Фамилия: str
    Отчество: Optional[str] = None
    Организация: Optional[str] = None
    Рабочий_телефон: Optional[str] = None
    Личный_телефон: Optional[str] = None

    def view_contact(self) -> None:
        for key, value in self.model_dump().items():
            print(f"{key}: {value}")
