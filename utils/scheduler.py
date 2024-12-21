import schedule
import threading
import time
import logging
import os
from utils.scraping import scrape_airbnb_titles

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def safe_scrape():
    try:
        scrape_airbnb_titles()
        logger.info("Scraping completado exitosamente.")
    except Exception as e:
        logger.error(f"Error durante el scraping: {e}")

def start_scheduler():
    """Inicia el scheduler en un hilo en segundo plano con manejo de errores y configuración."""
    logger.info("Iniciando el scheduler...")

    schedule_times = os.environ.get("SCHEDULE_TIMES", "08:00,20:00").split(",")
    for time_str in schedule_times:
        try:
          schedule.every().day.at(time_str).do(safe_scrape)
          logger.info(f"Tarea programada para las {time_str}")
        except schedule.ScheduleError as e:
          logger.error(f"Error al programar la tarea {time_str}: {e}")

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()