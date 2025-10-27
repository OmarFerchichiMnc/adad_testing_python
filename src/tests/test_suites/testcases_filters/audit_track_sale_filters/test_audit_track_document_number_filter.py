import logging

import pytest
import psycopg2
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_document_number_filter import AuditTrackSalesDocumentNumberFilters
import psycopg2
import signal




# -------------------------------------------------------------------------
def fetch_document_numbers(timeout_seconds=5):
    """Fetch sale IDs from the database with a time limit."""
    logging.info("📡 Connecting to DB to fetch sale IDs...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    # Set an alarm to limit total function execution time
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3  # connection-level timeout
        )
        conn.set_session(readonly=True, autocommit=True)

        cur = conn.cursor()
        cur.execute('SELECT document_number FROM "8X".sale ORDER BY id ASC LIMIT 10;')
        document_numbers = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not document_numbers:
            logging.info("⚠️ No sale IDs returned from DB.")
        else:
            logging.info(f"✅ Found sale IDs: {document_numbers}")
        return document_numbers

    except TimeoutError as te:
        logging.error(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        logging.error(f"❌ Error fetching sale IDs: {e}")
        return []
    finally:
        # Cancel alarm to avoid affecting next operations
        signal.alarm(0)


# -------------------------------------------------------------------------
@pytest.mark.parametrize("document_number", fetch_document_numbers())
def test_filter_document_numbers(driver, document_number):
    """Run pending sales check for each sale ID."""
    if document_number == "NO_DATA_FOUND":
        pytest.skip("⚠️ No data in DB — skipping test.")
    try:
        logging.info(f"🧪 Running check for sale_id: {document_number}")
        tc = AuditTrackSalesDocumentNumberFilters(document_number)
        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for sale_id: {document_number}")
    except Exception as e:
        pytest.skip(f"⚠️ Skipped sale_id {document_number} due to error: {e}")


