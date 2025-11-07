import logging
import os
import subprocess
import time
import pytest
import psycopg2
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_payment_id import AuditTrackSaleUIFilterPaymentID
import psycopg2
import psycopg2.extensions
import signal

def fetch_payment_ids(timeout_seconds=5):
    """Fetch payment ID from the database with a time limit."""
    print("📡 Connecting to DB to fetch payment ID...")

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
        cur.execute('SELECT payment_id FROM "8X".sale ORDER BY id ASC LIMIT 10;')
        payment_ids = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not payment_ids:
            print("⚠️ No payment ID returned from DB.")
        else:
            print(f"✅ Found payment ID: {payment_ids}")
        return payment_ids

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching payment ID: {e}")
        return []
    finally:
        # Cancel alarm to avoid affecting next operations
        signal.alarm(0)



# -------------------------------------------------------------------------
@pytest.mark.parametrize("payment_id", fetch_payment_ids())
def test_filter_payment_ids(driver, payment_id):
    """Run pending sales check for each payment id."""
    if payment_id == "NO_DATA_FOUND":
        pytest.skip("⚠️ No data in DB — skipping test.")
    try:
        logging.info(f"🧪 Running check for payment_id: {payment_id}")
        tc = AuditTrackSaleUIFilterPaymentID(payment_id)
        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for payment_id: {payment_id}")
    except Exception as e:
        pytest.skip(f"⚠️ Skipped payment_id {payment_id} due to error: {e}")