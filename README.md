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
While designing our Entity relationship diagram, we started parsing the sample XML MOMO file provided to identify the entities and their attributes as well as their relationships. 
The first and core entity identified was a transaction which  stores the transaction date, amount, currency, transaction category (via a foreign key), transaction fee, and balance after the transaction, as well as the time stamp in regards to when the transaction was made.
User is the second entity consisting of  id, both the first and last names, phone number,  and usertype(MTN agents, merchants, etc).
Transactions are also categorized into deposit, withdrawal, payment, or transfer, which gives us the third entity: transaction-category. It has only three attributes: its id, categoryname, and description ( giving more details for instance, payment of airtime, electricity bill; person to person transfer; bank deposits made.)
We also opted to have another entity called transactionUser entity. Since many users can participate in  many transactions as either sender or receiver, it's essential to identify the user´s role in each transaction.  This solves the many to many ambiguities, allowing easy handling of transactions.
Finally, we have a system-log, which allows us to audit and track an event. For example, with users' complaints about how they sent money, but it wasn´t received. Systemlogs allows us to see if the event took place, pinpoint, and debug. It has the following attributes: event type, transaction_id, date(time stamp), and message related to the transaction, thus providing a historical record of system activities.
SMS: This entity represents the SMS messages received for transactions. It captures crucial metadata such as protocol, address, date, and the service center used. These attributes help in tracing the origin and context of each message.


Relationships: 
Transaction ↔ User (Many-to-Many Relationship via TransactionUser Table) A transaction can involve multiple users, and a user can participate in multiple transactions.
TransactionCategory →Transaction (One-to-Many Relationship)
One TransactionCategory can be linked to many transactions, but each transaction can only belong to one category.
Transaction → SystemLog (One-to-Many) A single transaction may have multiple log events.
SystemLog.transaction_id → Transaction.transaction_id (Foreign Key)
This is because a single  transaction may go through multiple stages: parsed, validated, flagged, completed, etc.
User → TransactionUser (One-to-Many)
Via transactionUser roles, a single user can participate in many transactions as either sender or receiver. TransactionUser.user_id → User.user_id (Foreign Key)


SMS → Transaction (One-to-Many) or (one to one)
In real world Momo services sometimes One SMS can result in one or more transactions. Especially, if the SMS is a summary of all the transactions made or a single sms can be linked to a single transaction.


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



