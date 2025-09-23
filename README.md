*******# Team: MoMo Masters

## Team Members
- Saddam Daahir Adam
- Uwineza Shamilla
- Gahima Kuzo Divine
- Nicole Mbera Umurerwa

---

## Project Description
This project is about processing **Mobile Money (MoMo) SMS data**.  
We plan to:
- Read MoMo transaction data from XML files.
- Clean and organize the data.
- Save it into a database.
- Build a dashboard to visualize transactions.

This README is for Week 1, where we focus on setting up the repository, folder structure, and planning.

---

<img width="661" height="529" alt="image" src="https://github.com/user-attachments/assets/cd3f5159-9913-417e-aadd-7b3c845c9a93" />



## Week 2 Contributions – JSON Modeling
## ENTITY RELATIONSHIP DIAGRAM ERD
While parsing the sample XML MOMO file provided to design our Entity Relationship Diagram (ERD), the following key entities: Transaction, User, TransactionCategory, TransactionUser, SystemLog, and SMS, were identified.
• Transaction: Core entity containing attributes like transaction date, amount, currency, category (foreign key), transaction fee, balance, and timestamp.
User: Includes id, first and last names, phone number, and usertype (e.g., MTN agents, merchants).
TransactionCategory: Categorizes transactions into deposit, withdrawal, payment, or transfer; consists of id, category name, and description.
TransactionUser: Addresses many-to-many relationships between users and transactions, identifying user roles (sender or receiver).
SystemLog: Tracks events related to transactions, with attributes including event type, transaction_id, date, and message for auditing complaints.
 SMS: Entity for SMS messages related to transactions, capturing metadata such as protocol, address, date, and service center.
Relationships:
Transaction ↔ User: Many-to-Many via TransactionUser.
TransactionCategory → Transaction: One-to-Many (one category can be involved in many transactions).
Transaction → SystemLog: One-to-Many (one transaction can have multiple log events such as parsed, validated, flagged, completed, etc.).
User → TransactionUser: One-to-Many (one user can be involved in many transactions as either sender or receiver).
SMS → Transaction: Can be One-to-Many or One-to-One, depending on SMS content and transaction communication. Especially, if the SMS is a summary of all the transactions made or a single sms can be linked to a single transaction.

<img width="905" height="605" alt="image" src="https://github.com/user-attachments/assets/0d0b4dee-885b-48fb-a658-2b71b63b30ae" />

### JSON Schemas
We designed JSON schemas for each main entity:

- Users: `user_schema.json`
- Transaction Categories: `transaction_category_schema.json`
- Transactions: `transaction_schema.json`
- System Logs: `system_log_schema.json`

### Complex Transaction Example
`transaction_example.json` demonstrates a full transaction with:

- Sender & receiver user info
- Transaction details
- Category info
- System logs

### SQL → JSON Mapping
`sql_to_json_mapping.md` documents:

- Mapping of SQL tables to JSON fields
- Example SQL `INSERT` statements
- Corresponding JSON examples
- Full nested transaction object

<img width="473" height="186" alt="image" src="https://github.com/user-attachments/assets/03758146-4f9d-4d6a-a3eb-1d93f5139f2f" />

---

## Architecture Diagram
![MoMo ETL Dashboard Architecture](./docs/system-architecture.drawio.png)

---

## Scrum Board
[https://github.com/orgs/ALUdevops7/projects/2/views/1]

  
<img width="1171" height="406" alt="image" src="https://github.com/user-attachments/assets/ec662e35-fbb4-436c-ab8e-65121a624348" />

<img width="994" height="540" alt="image" src="https://github.com/user-attachments/assets/2a69c95b-2211-4190-a352-674f7ab3cb39" />





---

## Notes
- Week 1 focus: repository setup, folder organization, team collaboration, and task planning.


