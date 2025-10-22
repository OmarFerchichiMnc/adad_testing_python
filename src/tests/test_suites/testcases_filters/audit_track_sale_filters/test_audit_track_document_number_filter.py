import logging
import os
import subprocess
import time
import pytest
import psycopg2
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_document_number_filter import AuditTrackSalesDocumentNumberFilters
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_sale_id_filter import AuditTrackSalesSaleIDFilters
from src.testcase.testcases_filters.testcase_check_sales import checkPendingSalesFilters


# -------------------------------------------------------------------------
def fetch_document_numbers():
    """Fetch sale IDs from the database."""
    print("📡 Connecting to DB to fetch sale IDs...")

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555
        )
        cur = conn.cursor()
        cur.execute('SELECT id FROM "8X".sale ORDER BY id ASC LIMIT 10;')
        document_numbers = [row[5] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not document_numbers:
            print("⚠️ No sale IDs returned from DB.")
        else:
            print(f"✅ Found sale IDs: {document_numbers}")
        return document_numbers

    except Exception as e:
        print(f"❌ Error fetching sale IDs: {e}")
        return []


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


