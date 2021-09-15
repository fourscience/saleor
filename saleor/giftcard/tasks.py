from celery.utils.log import get_task_logger
from django.utils import timezone

from ..celeryconf import app
from .events import gift_cards_deactivated_event
from .models import GiftCard

task_logger = get_task_logger(__name__)


@app.task
def deactivate_expired_cards_task():
    today = timezone.now().date()
    gift_cards = GiftCard.objects.filter(expiry_date__lt=today)
    if not gift_cards:
        return
    count = gift_cards.update(is_active=False)
    gift_cards_deactivated_event(
        gift_cards.values_list("id", flat=True), user=None, app=None
    )
    task_logger.debug("Deactivate %s gift cards", count)
