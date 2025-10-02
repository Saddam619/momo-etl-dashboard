

# **Transactions API Documentation**

The Transactions API provides endpoints to manage SMS transaction records.

Each transaction record follows this structure:

{
  "transaction_id": 10001,
  "transaction_date": "2024-09-15T14:45:30Z",
  "amount": 2500.75,
  "currency": "USD",
  "category_id": 3,
  "fee": 15.25,
  "balance_after": 10250.50,
  "service_center": "+250788110381",
  "sms_date_long": 1726401930000,
  "raw_message": "Payment of $2500.75 to John Doe completed successfully.",
  "created_at": "2024-09-15T14:46:00Z"
}

## **1\. List All Transactions**

Endpoint & Method

GET /transactions

Request Example

GET /transactions HTTP/1.1  
Host: api.example.com  
Accept: application/json

Response Example

{
  "transactions": [
    {
      "transaction_id": 10001,
      "transaction_date": "2024-09-15T14:45:30Z",
      "amount": 2500.75,
      "currency": "USD",
      "category_id": 3,
      "fee": 15.25,
      "balance_after": 10250.50,
      "service_center": "+250788110381",
      "sms_date_long": 1726401930000,
      "raw_message": "Payment of $2500.75 to John Doe completed successfully.",
      "created_at": "2024-09-15T14:46:00Z"
    },
    {
      "transaction_id": 10002,
      "transaction_date": "2024-09-20T09:10:12Z",
      "amount": 500.00,
      "currency": "USD",
      "category_id": 5,
      "fee": 5.00,
      "balance_after": 9750.50,
      "service_center": "+250788110382",
      "sms_date_long": 1726823412000,
      "raw_message": "Transfer of $500.00 received from Jane Smith.",
      "created_at": "2024-09-20T09:10:30Z"
    }
  ]
}

Error Codes

* `500` – Internal server error

## **2\. Get One Transaction**

**Endpoint & Method**

GET /transactions/{id}

Request Example

GET /transactions/76662021700 HTTP/1.1  
Host: api.example.com  
Accept: application/json

Response Example

{
  "transaction": {
    "transaction_id": 10001,
    "transaction_date": "2024-09-15T14:45:30Z",
    "amount": 2500.75,
    "currency": "USD",
    "category_id": 3,
    "fee": 15.25,
    "balance_after": 10250.50,
    "service_center": "+250788110381",
    "sms_date_long": 1726401930000,
    "raw_message": "Payment of $2500.75 to John Doe completed successfully.",
    "created_at": "2024-09-15T14:46:00Z"
  }
}

Error Codes

* `404` – Transaction not found

* `500` – Internal server error

## **3\. Create a New Transaction**

**Endpoint & Method**

POST /transactions

Request Example

POST /transactions HTTP/1.1  
Host: api.example.com  
Content-Type: application/json

{
  "transaction_date": "2024-09-25T11:30:00Z",
  "amount": 1000.00,
  "currency": "USD",
  "category_id": 2,
  "fee": 10.00,
  "balance_after": 8750.50,
  "service_center": "+250788110383",
  "sms_date_long": 1727250600000,
  "raw_message": "You paid $1000.00 for electricity bill.",
  "created_at": "2024-09-25T11:30:30Z"
}

Response Example


{  
  "message": "Transaction created successfully", 
  "transaction": {
  "transaction_date": "2024-09-25T11:30:00Z",
  "amount": 1000.00,
  "currency": "USD",
  "category_id": 2,
  "fee": 10.00,
  "balance_after": 8750.50,
  "service_center": "+250788110383",
  "sms_date_long": 1727250600000,
  "raw_message": "You paid $1000.00 for electricity bill.",
  "created_at": "2024-09-25T11:30:30Z"
}
 
}

Error Codes

* `400` – Invalid request body

* `500` – Internal server error

## **4\. Update an Existing Transaction**

**Endpoint & Method**

PUT /transactions/{id}

Request Example

PUT /transactions/76662021700 HTTP/1.1  
Host: api.example.com  
Content-Type: application/json

{  
  "amount": 2500.0,  
  "status": "PENDING"  
}

Response Example

{  
  "message": "Transaction updated successfully",  
  "transaction": {
  "amount": 2500.0,
  "fee": 12.00,
  "balance_after": 8740.50,
  "raw_message": "Corrected payment of $1100.00 for electricity bill."
}

}

Error Codes

* `400` – Invalid request body

* `404` – Transaction not found

* `500` – Internal server error

## **5\. Delete a Transaction**

**Endpoint & Method**

DELETE /transactions/{id}

Request Example

DELETE /transactions/76662021700 HTTP/1.1  
Host: api.example.com

Response Example

{  
  "message": "Transaction deleted successfully"  
}

Error Codes

* `404` – Transaction not found

* `500` – Internal server error.