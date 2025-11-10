import logging
import pytest
from src.testcase.testcases_filters.audit_track_sale_filter.testcase_audit_track_advanced_filters import AuditTrackSalesAdvancedFilters





import logging
import pytest
import psycopg2


import logging
import pytest

import psycopg2
import signal

def fetch_payment_dates(timeout_seconds=5):
    """Fetch payment dates from the database with a time limit."""
    print("📡 Connecting to DB to fetch payment dates...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT payment_date FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        payment_dates = [f"{row[0]} to {row[0]}" if row[0] else "" for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not payment_dates:
            print("⚠️ No payment dates returned from DB.")
        else:
            print(f"✅ Found payment dates: {payment_dates}")
        return payment_dates

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching payment dates: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_channel_types(timeout_seconds=5):
    """Fetch channel types from the database with a time limit."""
    print("📡 Connecting to DB to fetch channel types...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT sale_channel_type FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        channels = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not channels:
            print("⚠️ No channel types returned from DB.")
        else:
            print(f"✅ Found channel types: {channels}")
        return channels

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching channel types: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_countries(timeout_seconds=5):
    """Fetch countries from the database with a time limit."""
    print("📡 Connecting to DB to fetch countries...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT country FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        countries = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not countries:
            print("⚠️ No countries returned from DB.")
        else:
            print(f"✅ Found countries: {countries}")
        return countries

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching countries: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_file_ids(timeout_seconds=5):
    """Fetch file IDs from the database with a time limit."""
    print("📡 Connecting to DB to fetch file IDs...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT operation_id FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        file_ids = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not file_ids:
            print("⚠️ No file IDs returned from DB.")
        else:
            print(f"✅ Found file IDs: {file_ids}")
        return file_ids

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching file IDs: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_fop_codes(timeout_seconds=5):
    """Fetch FOP codes from the database with a time limit."""
    print("📡 Connecting to DB to fetch FOP codes...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT form_of_payment_code FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        fop_codes = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not fop_codes:
            print("⚠️ No FOP codes returned from DB.")
        else:
            print(f"✅ Found FOP codes: {fop_codes}")
        return fop_codes

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching FOP codes: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_fop_sub_codes(timeout_seconds=5):
    """Fetch FOP sub codes from the database with a time limit."""
    print("📡 Connecting to DB to fetch FOP sub codes...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT fop_sub_code FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        fop_sub_codes = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not fop_sub_codes:
            print("⚠️ No FOP sub codes returned from DB.")
        else:
            print(f"✅ Found FOP sub codes: {fop_sub_codes}")
        return fop_sub_codes

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching FOP sub codes: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_settled_statuses(timeout_seconds=5):
    """Fetch settled statuses from the database with a time limit."""
    print("📡 Connecting to DB to fetch settled statuses...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT settled_status FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        settled_statuses = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not settled_statuses:
            print("⚠️ No settled statuses returned from DB.")
        else:
            print(f"✅ Found settled statuses: {settled_statuses}")
        return settled_statuses

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching settled statuses: {e}")
        return []
    finally:
        signal.alarm(0)


def fetch_transaction_type(timeout_seconds=5):
    """Fetch channel types from the database with a time limit."""
    print("📡 Connecting to DB to fetch channel types...")

    def timeout_handler(signum, frame):
        raise TimeoutError("⏰ Database operation timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="adad",
            user="staging_dbuser8x",
            password="Ad@d8X!St0dU$eR2024",
            port=5555,
            connect_timeout=3
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute('SELECT transaction_type FROM "8X".sale ORDER BY id ASC LIMIT 3;')
        channels = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        if not channels:
            print("⚠️ No channel types returned from DB.")
        else:
            print(f"✅ Found channel types: {channels}")
        return channels

    except TimeoutError as te:
        print(f"⏰ Operation timed out after {timeout_seconds}s: {te}")
        return []
    except Exception as e:
        print(f"❌ Error fetching channel types: {e}")
        return []
    finally:
        signal.alarm(0)



channels = ([i+' - ' +'Sale' for i in fetch_channel_types()]) or [""]
countries = fetch_countries() or [""]
file_ids = fetch_file_ids() or [""]
fop_codes = fetch_fop_codes() or [""]
fop_sub_codes = fetch_fop_sub_codes() or [""]
settled_statuses = fetch_settled_statuses() or [""]

payment_date_range = '09/11/2025 - 10/11/2025'  # fixed tuple problem





@pytest.mark.parametrize("channel_type", channels)
@pytest.mark.parametrize("country", countries)
@pytest.mark.parametrize("file_id", file_ids)
@pytest.mark.parametrize("fop_code", fop_codes)
@pytest.mark.parametrize("fop_sub_code", fop_sub_codes)
@pytest.mark.parametrize("settled_status", settled_statuses)
def test_filter_advanced_filters(driver, channel_type, country, file_id, fop_code, fop_sub_code, settled_status):
    """Run pending sales check for each sale ID."""

    try:
        logging.info(f"🧪 Running check for sale_id: ")
        tc = AuditTrackSalesAdvancedFilters(payment_date_range='09/11/2025 - 10/11/2025',
        channel_type=channel_type ,
        country=country ,
        file_id=file_id ,
        fop_code=fop_code ,
        fop_sub_code =fop_sub_code,
        settled_status=settled_status )


        tc.run(driver)
        tc.export_to_json()
        logging.info(f"✅ Test passed for sale_id: ")
    except Exception as e:
        pytest.fail(f"⚠️ Skipped sale_id  due to error: {e}")