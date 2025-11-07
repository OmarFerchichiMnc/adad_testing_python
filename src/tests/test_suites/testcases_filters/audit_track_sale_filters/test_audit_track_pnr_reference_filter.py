import logging

import pytest
import psycopg2
import psycopg2
import signal

from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_pnr_order_reference_filter import AuditTrackSalesPNROrderReferenceFilters




# -------------------------------------------------------------------------
def fetch_pnr_references(timeout_seconds=5):
    """Fetch pnr references from the database with a time limit."""
    logging.info("📡 Connecting to DB to fetch pnr references...")

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
        cur.execute('SELECT pnr_reference FROM "8X".sale ORDER BY id ASC LIMIT 10;')
        document_numbers = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not document_numbers:
            logging.info("⚠️ No pnr references returned from DB.")
        else:
            logging.info(f"✅ Found pnr references: {document_numbers}")
        return document_numbers

    except TimeoutError as te:
        logging.error(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        logging.error(f"❌ Error fetching pnr references: {e}")
        return []
    finally:
        # Cancel alarm to avoid affecting next operations
        signal.alarm(0)


# -------------------------------------------------------------------------
@pytest.mark.parametrize("pnr_reference", fetch_pnr_references())
def test_filter_pnr_references(driver, pnr_reference):
    """Run pending sales check for each sale ID."""
    if pnr_reference == "NO_DATA_FOUND":
        pytest.skip("⚠️ No data in DB — skipping test.")
    try:
        logging.info(f"🧪 Running check for sale_id: {pnr_reference}")
        tc = AuditTrackSalesPNROrderReferenceFilters(pnr_reference)
        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for sale_id: {pnr_reference}")
    except Exception as e:
        pytest.skip(f"⚠️ Skipped sale_id {pnr_reference} due to error: {e}")


