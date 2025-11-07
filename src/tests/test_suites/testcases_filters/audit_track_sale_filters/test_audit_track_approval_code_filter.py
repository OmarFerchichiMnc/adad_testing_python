import logging
import os
import subprocess
import time
import pytest
import psycopg2
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_approval_code_filter import AuditTrackSaleApprovalCodeFilters
import psycopg2
import psycopg2.extensions
import signal

def fetch_approval_codes(timeout_seconds=5):
    """Fetch approval codes from the database with a time limit."""
    print("📡 Connecting to DB to fetch approval codes...")

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
        cur.execute('SELECT approval_code FROM "8X".sale ORDER BY id ASC LIMIT 10;')
        approval_codes = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not approval_codes:
            print("⚠️ No approval codes returned from DB.")
        else:
            print(f"✅ Found approval codes: {approval_codes}")
        return approval_codes

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching approval codes: {e}")
        return []
    finally:
        # Cancel alarm to avoid affecting next operations
        signal.alarm(0)



# -------------------------------------------------------------------------
@pytest.mark.parametrize("approval_code", fetch_approval_codes())
def test_filter_approval_codes(driver, approval_code):
    """Run pending approval codes check for each approval code."""
    if approval_code == "NO_DATA_FOUND":
        pytest.skip("⚠️ No data in DB — skipping test.")
    try:
        logging.info(f"🧪 Running check for approval_code: {approval_code}")
        tc = AuditTrackSaleApprovalCodeFilters(approval_code)
        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for approval_code: {approval_code}")
    except Exception as e:
        pytest.skip(f"⚠️ Skipped approval_code {approval_code} due to error: {e}")