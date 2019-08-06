# activecampaign-python
ActiveCampaign API wrapper written in python.

This library supports the latest API version 3. If you are looking for API version 1 which is also supported by ActiveCampaign then check below.

## Installing (API v3)

```
pip install activecampaign-python
```

## Requirements

```
- requests
```

## Usage

#### Client instantiation
```
from activecampaign.client import Client
client = Client(URL, API_KEY)
```

### Automations
#### List all automations
```
response = client.automations.list_all_automations()
```

### Contacts
#### Create a contact
```
data = {
	"contact": {
		"email": "johndoe@example.com",
		"firstName": "John",
		"lastName": "Doe",
		"phone": "7223224241"
	}
}
response = client.contacts.create_a_contact(data)
```

#### Create or update contact
```
data = {
	"contact": {
		"email": "johndoe@example.com",
		"firstName": "John",
		"lastName": "Doe",
		"phone": "7223224241"
	}
}
response = client.contacts.create_or_update_contact(data)
```

#### Retrieve a contact
```
response = client.contacts.retrieve_a_contact("contact_id")
```

#### Update list status for a contact
```
data = {
    "contactList": {
        "list": 2,
        "contact": 1,
        "status": 1
    }
}
response = client.contacts.update_list_status_for_a_contact(data)
```

#### Update a contact
```
data = {
	"contact": {
		"email": "johndoe@example.com",
		"firstName": "John",
		"lastName": "Doe"
	}
}
response = client.contacts.update_a_contact("contact_id", data)
```

#### Delete a contact
```
response = client.contacts.delete_a_contact("contact_id")
```

#### List all contacts
```
response = client.contacts.list_all_contacts()

Additionally, you can filter a contact:
response = client.contacts.list_all_contacts(email="johndoe@example.com")

For more query params: https://developers.activecampaign.com/reference#list-all-contacts
```

#### List all automations the contact is in
```
response = client.contacts.list_all_automations_the_contacts_is_in("contact_id")
```

#### Retrieve a contacts score value
```
response = client.contacts.retrieve_a_contacts_score_value("contact_id")
```

#### Add a contact to an automation
```
data = {
    "contactAutomation": {
        "contact": 1,
        "automation": 1
    }
}
response = client.contacts.add_a_contact_to_an_automation(data)
```

#### Retrieve an automation a contact is in
```
response = client.contacts.retrieve_an_automation_a_contact_is_in("contact_automation_id")
```

#### Remove a contact from an automation
```
response = client.contacts.remove_a_contact_from_an_automation("contact_automation_id")
```

#### List all automations a contact is in
```
response = client.contacts.list_all_automations_a_contact_is_in()
```

#### Create a custom field
```
data = {
	"field": {
		"type": "textarea",
		"title": "Field Title",
		"descript": "Field description",
		"isrequired": 1,
		"perstag": "Personalized Tag",
		"defval": "Defaut Value",
		"visible": 1,
		"ordernum": 1
    }
}
response = client.contacts.create_a_custom_field(data)
```

#### Retrieve a custom field
```
response = client.contacts.retrieve_a_custom_field("field_id")
```

#### Update a custom field
```
data = {
	"field": {
		"type": "textarea",
		"title": "Field Title",
		"descript": "Field description",
		"isrequired": 1,
		"perstag": "Personalized Tag",
		"defval": "Defaut Value",
		"visible": 1,
		"ordernum": 1
    }
}
response = client.contacts.create_a_custom_field("field_id", data)
```

#### Delete a custom field
```
response = client.contacts.delete_a_custom_field("field_id")
```

#### List all custom fields
```
response = client.contacts.list_all_custom_fields()
```

#### Create a custom field relationship to list(s)
```
data = {
	"fieldRel": {
		"field": 8,
		"relid": 2
	}
}
response = client.contacts.create_a_custom_field_relationship_to_list(data)
```

#### Create custom field options
```
data = {
    "field": 1,
    "label": "my custom label",
    "value": 1,
    "orderid": 1,
    "isdefault": True
}
response = client.contacts.create_custom_field_options(data)
```

#### Retrieve field options
```
response = client.contacts.retrieve_field_options("field_id")
```

### Deals
#### Create a deal
```
data = {
  "deal": {
    "contact": "51",
    "description": "This deal is an important deal",
    "currency": "usd",
    "group": "1",
    "owner": "1",
    "percent": None,
    "stage": "1",
    "status": 0,
    "title": "AC Deal",
    "value": 45600
  }
}
response = client.deals.create_a_deal(data)
```

#### Retrieve a deal
```
response = client.deals.retrieve_a_deal("deal_id")
```

#### Update a deal
```
data = {
  "deal": {
    "contact": "51",
    "description": "This deal is an important deal",
    "currency": "usd",
    "group": "1",
    "owner": "1",
    "percent": None,
    "stage": "1",
    "status": 0,
    "title": "AC Deal",
    "value": 45600
  }
}
response = client.deals.update_a_deal(data)
```

#### Delete a deal
```
response = client.deals.delete_a_deal("deal_id")
```

#### List all deals
```
response = client.deals.list_all_deals()

Additionally, you can filter a deal:
query = {
    "filters[stage]": 1
}
response = client.deals.list_all_deals(**query)

For more query params: https://developers.activecampaign.com/reference#list-all-deals
```

#### Create a deal note
```
data = {
  "note": {
    "note": "Note for the deal"
  }
}
response = client.deals.create_a_deal_note("deal_id", data)
```

#### Update a deal note
```
data = {
  "note": {
    "note": "Update with more info"
  }
}
response = client.deals.update_a_deal_note("deal_id", "note_id", data)
```

#### List all pipelines
```
response = client.deals.list_all_pipelines()

Additionally, you can filter a pipeline:
query = {
    "filters[title]": "My pipeline"
}
response = client.deals.list_all_pipelines(**query)

For more query params: https://developers.activecampaign.com/reference#list-all-pipelines
```

#### List all stages
```
response = client.deals.list_all_stages()

Additionally, you can filter a stage:
query = {
    "filters[d_groupid]": 1
}
response = client.deals.list_all_stages(**query)

For more query params: https://developers.activecampaign.com/reference#list-all-deal-stages
```

### Lists
#### Create a list
```
data = {
	"list": {
		"name": "Name of List",
		"stringid": "Name-of-list",
		"sender_url": "http://activecampaign.com",
		"sender_reminder": "You are receiving this email as you subscribed to a newsletter when making an order on our site.",
		"send_last_broadcast": 0,
		"carboncopy": "",
		"subscription_notify": "",
		"unsubscription_notify": "",
		"user": 1
	}
}
response = client.lists.create_a_list(data)
```

#### Retrieve a list
```
response = client.lists.retrieve_a_list("list_id")
```

#### Delete a list
```
response = client.lists.delete_a_list("list_id")
```

#### Retrieve all lists
```
response = client.lists.retrieve_all_lists()
```

#### Create a list group permission
```
data = {
	"listGroup": {
		"listid": 19,
		"groupid": 1
	}
}
response = client.lists.create_a_list_group_permission(data)
```

### Notes
#### Create a note
```
data = {
	"note": {
		"note": "This is the text of the note",
		"relid": 2,
		"reltype": "Subscriber"
	}
}
response = client.notes.create_a_note(data)
```

#### Retrieve a note
```
response = client.notes.retrieve_a_note("note_id")
```

#### Update a note
```
data = {
	"note": {
		"note": "This is the text of the note",
		"relid": 2,
		"reltype": "Subscriber"
	}
}
response = client.notes.update_a_note("note_id", data)
```

#### Delete a note
```
response = client.notes.delete_a_note("note_id")
```

### Tasks
#### Create a task
```
data = {
  "dealTask": {
    "title":null,
    "ownerType":"contact",
    "relid":"7",
    "status":0,
    "note":"Testing Task",
    "duedate":"2017-02-25T12:00:00-06:00",
    "edate":"2017-02-25T12:15:00-06:00",
    "dealTasktype":"1"
  }
}
response = client.tasks.create_a_task(data)
```

#### Retrieve a task
```
response = client.tasks.retrieve_a_task("task_id")
```

#### Update a task
```
data = {
  "dealTask": {
    "title":null,
    "ownerType":"contact",
    "relid":"7",
    "status":0,
    "note":"Testing Task",
    "duedate":"2017-02-25T12:00:00-06:00",
    "edate":"2017-02-25T12:15:00-06:00",
    "dealTasktype":"1"
  }
}
response = client.tasks.update_a_task("task_id", data)
```

#### Delete a task
```
response = client.tasks.delete_a_task("task_id")
```

#### List all tasks
```
response = client.tasks.list_all_tasks()

Additionally, you can filter a task:
query = {
    "filters[title]": "My task"
}
response = client.deals.list_all_tasks(**query)

For more query params: https://developers.activecampaign.com/reference#list-all-tasks
```

### Users
#### Create a user
```
response = client.users.create_a_user(data)
```

#### Retrieve a user
```
response = client.users.retrieve_a_user("user_id")
```

#### Retrieve a user by email
```
response = client.users.retrieve_a_user_by_email("email")
```

#### Retrieve a user by username
```
response = client.users.retrieve_a_user_by_username("username")
```

#### Retrieve logged-in user
```
response = client.users.retrieve_logged_in_user()
```

#### Update a user
```
response = client.users.update_a_user("user_id", data)
```

#### Delete a user
```
response = client.users.delete_a_user("user_id")
```

#### List all users
```
response = client.users.list_all_users()
```

### Webhooks
#### Create a webhook
```
data = {
    "webhook": {
        "name": "My Hook",
        "url": "http://example.com/my-hook",
        "events": [
            "subscribe",
            "unsubscribe",
            "sent"
        ],
        "sources": [
            "public",
            "system"
        ]
    }
}
response = client.webhooks.create_a_webhook(data)
```

#### Retrieve a webhook
```
response = client.webhooks.retrieve_a_webhook("webhook_id")
```

#### Delete a webhook
```
response = client.webhooks.delete_a_webhook("webhook_id")
```

#### List all webhooks
```
response = client.webhooks.list_all_webhooks()

Additionally, you can filter a webhook:
query = {
    "filters[name]": "My webhook"
}
response = client.deals.list_all_webhooks(**query)

For more query params: https://developers.activecampaign.com/reference#get-a-list-of-webhooks
```

#### List all webhook events
```
response = client.webhooks.list_all_webhook_events()
```

## About API v1

You can clone and checkout our tag v0.1.1.

```
$ git clone https://github.com/GearPlug/activecampaign-python.git
$ git checkout tags/v0.1.1 -b <branch_name>
```

Also you can install this version in pip
```
$ pip install activecampaign-python=0.1.1
```
