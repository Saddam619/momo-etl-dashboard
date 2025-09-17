# SQL → JSON Mapping

This document shows how each SQL table/column from the ERD maps to the JSON schemas.

---

## 1. User Table → user_schema.json
| SQL Column       | JSON Field     |
|------------------|---------------|
| user_id          | user_id       |
| phone_number     | phone_number  |
| full_name        | full_name     |
| user_type        | user_type     |
| account_number   | account_number|
| created_at       | created_at    |

---

## 2. Transaction Table → transaction_schema.json
| SQL Column        | JSON Field       |
|-------------------|-----------------|
| transaction_id    | transaction_id  |
| transaction_date  | transaction_date|
| amount            | amount          |
| currency          | currency        |
| category_id       | category_id     |
| fee               | fee             |
| balance_after     | balance_after   |
| service_center    | service_center  |
| sms_date_long     | sms_date_long   |
| raw_message       | raw_message     |
| created_at        | created_at      |

---

## 3. TransactionCategory Table → transaction_category_schema.json
| SQL Column     | JSON Field     |
|----------------|---------------|
| category_id    | category_id   |
| category_name  | category_name |
| description    | description   |

---

## 4. TransactionUser Table → transaction_user_schema.json
| SQL Column     | JSON Field     |
|----------------|---------------|
| txn_user_id    | txn_user_id   |
| transaction_id | transaction_id|
| user_id        | user_id       |
| role           | role          |

---

## 5. SMS Table → sms_schema.json
| SQL Column     | JSON Field     |
|----------------|---------------|
| sms_id         | sms_id        |
| protocol       | protocol      |
| address        | address       |
| date           | date          |
| readable_date  | readable_date |
| body           | body          |
| service_center | service_center|

---

## 6. SystemLog Table → system_log_schema.json
| SQL Column     | JSON Field     |
|----------------|---------------|
| log_id         | log_id        |
| transaction_id | transaction_id|
| event_date     | event_date    |
| event_type     | event_type    |
| message        | message       |
| service_center | service_center|
| created_at     | created_at    |
