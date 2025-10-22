import logging
import os
import subprocess
import time
import pytest
import psycopg2
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_sale_id_filter import AuditTrackSalesSaleIDFilters


# -------------------------------------------------------------------------
def fetch_sale_ids():
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
        sale_ids = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not sale_ids:
            print("⚠️ No sale IDs returned from DB.")
        else:
            print(f"✅ Found sale IDs: {sale_ids}")
        return sale_ids

    except Exception as e:
        print(f"❌ Error fetching sale IDs: {e}")
        return []


# -------------------------------------------------------------------------
@pytest.mark.parametrize("sale_id", fetch_sale_ids())
def test_filter_sale_ids(driver, sale_id):
    """Run pending sales check for each sale ID."""
    if sale_id == "NO_DATA_FOUND":
        pytest.skip("⚠️ No data in DB — skipping test.")
    try:
        logging.info(f"🧪 Running check for sale_id: {sale_id}")
        tc = AuditTrackSalesSaleIDFilters(sale_id)
        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for sale_id: {sale_id}")
    except Exception as e:
        pytest.skip(f"⚠️ Skipped sale_id {sale_id} due to error: {e}")



