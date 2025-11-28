from models import User, Trainer, Slot, Booking
from datetime import datetime
from typing import List, Optional

trainers_db: dict = {}
slots_db: dict = {}
bookings_db: dict = {}
users_db: dict = {}

next_trainer_id = 1
next_slot_id = 1
next_booking_id = 1

def create_trainer(user_id: int, specialization: str, experience_years: int) -> Trainer:
    global next_trainer_id
    trainer = Trainer(
        trainer_id=next_trainer_id,
        user_id=user_id,
        specialization=specialization,
        experience_years=experience_years
    )
    trainers_db[next_trainer_id] = trainer
    next_trainer_id += 1
    return trainer

def create_slot(trainer_id: int, start_time: datetime, end_time: datetime, capacity: int = 1) -> Slot:
    global next_slot_id
    slot = Slot(
        slot_id=next_slot_id,
        trainer_id=trainer_id,
        start_time=start_time,
        end_time=end_time,
        capacity=capacity
    )
    slots_db[next_slot_id] = slot
    next_slot_id += 1
    return slot

def list_slots(trainer_id: Optional[int] = None) -> List[Slot]:
    slots = list(slots_db.values())
    if trainer_id:
        slots = [s for s in slots if s.trainer_id == trainer_id]
    return slots

def book_slot(user_id: int, slot_id: int) -> Optional[Booking]:
    global next_booking_id
    if slot_id not in slots_db:
        return None
    
    slot = slots_db[slot_id]
    if not slot.is_available():
        return None
    
    booking = Booking(
        booking_id=next_booking_id,
        user_id=user_id,
        slot_id=slot_id
    )
    bookings_db[next_booking_id] = booking
    slot.booked_count += 1
    next_booking_id += 1
    return booking
