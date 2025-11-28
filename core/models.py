from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    user_id: int
    name: str
    is_trainer: bool = False
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

@dataclass
class Trainer:
    trainer_id: int
    user_id: int
    specialization: str
    experience_years: int
    rating: float = 0.0

@dataclass
class Slot:
    slot_id: int
    trainer_id: int
    start_time: datetime
    end_time: datetime
    capacity: int = 1
    booked_count: int = 0

    def is_available(self) -> bool:
        return self.booked_count < self.capacity

@dataclass
class Booking:
    booking_id: int
    user_id: int
    slot_id: int
    created_at: datetime = None
    status: str = 'active'

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
