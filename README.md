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

#### Create a custom field value
```
response = activecampaign_client.contacts.create_a_custom_field_value(data)
```

#### Retrieve a custom field value
```
response = activecampaign_client.contacts.retrieve_a_custom_field_value(field_value_id="some-id")
```

#### Update a custom field value for contact
```
response = activecampaign_client.contacts.update_a_custom_field_value_for_contact(data, field_value_id="some-id")
```

#### Delete a custom field value
```
response = activecampaign_client.contacts.delete_a_custom_field_value(field_value_id="some-id")
```

#### List all custom field values
```
response = activecampaign_client.contacts.list_all_custom_field_values()
```

#### Retrieve a contact's field values
```
response = activecampaign_client.contacts.retrieve_a_contacts_field_values(contact_id="some-id")
```

#### Retrieve a contact's tracking logs
```
response = activecampaign_client.contacts.retrieve_a_contacts_tracking_logs(contact_id="some-id")
```

#### Retrieve a contact's data
```
response = activecampaign_client.contacts.retrieve_a_contacts_data(contact_id="some-id")
```

#### Retrieve a contact's bounce logs
```
response = activecampaign_client.contacts.retrieve_a_contacts_bounce_logs(contact_id="some-id")
```

#### Retrieve a contact's geo ips
```
response = activecampaign_client.contacts.retrieve_a_contacts_geo_ips(contact_id="some-id")
```

#### Retrieve a contact's organization
```
response = activecampaign_client.contacts.retrieve_a_contacts_organization(contact_id="some-id")
```

#### Retrieve a contact's account contacts
```
response = activecampaign_client.contacts.retrieve_a_contacts_account_contacts(contact_id="some-id")
```

#### Retrieve a contact's automation entry counts
```
response = activecampaign_client.contacts.retrieve_a_contacts_automation_entry_counts(contact_id="some-id")
```

#### Add a tag to a contact
```
data = {
    "contactTag": {
        "contact": "1",
        "tag": "20"
    }
}
response = client.contacts.add_a_tag_to_contact(data)
```

#### Remove a tag from a contact
```
response = client.contacts.remove_a_tag_from_a_contact("contact_tag_id")
```

#### Retrieve contact tags
```
response = client.contacts.retrieve_contact_tags("contact_id")
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

### Tags
#### Create a tag
```
data = {
    "tag":{
        "tag": "My Tag",
        "tagType": "contact",
        "description": "Description"
    }
}
response = client.tags.create_a_tag(data)
```

#### Retrieve a tag
```
response = client.tags.retrieve_a_tag("tag_id")
```

#### Update a tag
```
data = {
    "tag":{
        "tag": "My Tag",
        "tagType": "contact",
        "description": "Description"
    }
}
response = client.tags.update_a_tag("tag_id", data)
```

#### Delete a tag
```
response = client.tags.delete_a_tag("tag_id")
```

#### List all tags
```
response = client.tags.list_all_tags(search='Tag Name')
```

### Custom Objects
#### Create a schema
```
data = {
  "schema": {
    "slug": "object-name",
    "labels": {
      "singular": "ObjectName",
      "plural": "ObjectNames"
    },
    "description": "Some Description",
    "fields": [
      {
        "id": "some-field-id",
        "labels": {
          "singular": "ID",
          "plural": "IDs"
        },
        "type": "text",
        "required": True,
      },
    ],
    "relationships": [
      {
        "id": "primary-contact",
        "labels": {
          "singular": "Primary Contact",
          "plural": "Primary Contacts"
        },
        "description": "Primary contact to this object",
        "namespace": "contacts",
        "hasMany": False
      }
    ]
  }
}
response = client.customobjects.create_a_schema(data=data)
```

#### Retrieve a schema
```
response = client.customobjects.retrieve_a_schema(schema_id="some-id", show_all_fields=False)
```

#### Update a schema
```
data = {
  "schema": {
    "slug": "object-name",
    "labels": {
      "singular": "ObjectName",
      "plural": "ObjectNames"
    },
    "description": "Some Description",
    "fields": [
      {
        "id": "some-field-id",
        "labels": {
          "singular": "ID",
          "plural": "IDs"
        },
        "type": "text",
        "required": True,
      },
      {
        "id": "some-other-field-id",
        "labels": {
          "singular": "OtherID",
          "plural": "OtherIDs"
        },
        "type": "text",
        "required": True,
      },
    ],
    "relationships": [
      {
        "id": "primary-contact",
        "labels": {
          "singular": "Primary Contact",
          "plural": "Primary Contacts"
        },
        "description": "Primary contact to this object",
        "namespace": "contacts",
        "hasMany": False
      }
    ]
  }
}
response = client.customobjects.update_a_schema(schema_id="some-schema-id", data=data, show_all_fields=False)
```

#### Delete a schema
```
response = client.customobjects.delete_a_schema(schema_id="some-id")
```
WARNING: This deletes all associated records

#### List all schemas
```
response = client.customobjects.list_all_schemas(schema_relationship="contact", limit=20, offset=0, ordering=None, show_all_fields=False)
```

#### Delete field in schema
```
response = client.customobjects.delete_a_field(schema_id="some-id", field_id="some-field-id", show_all_fields=False)
```

#### Create a public schema
```
data = {

}
response = client.customobjects.create_a_public_schema(data=data)
```

#### Create a child schema
```
response = client.customobjects.create_a_child_schema(parent_id="some-parent-schema-id")
```

#### Upsert custom object record
```
data = {
  "record": {
    "fields": [
      {
        "id": "some-field-id",
        "value": "asdf-1234"
      },
      {
        "id": "some-other-field-id",
        "value": "asdf-5678"
      },
    ]
  }
}
response = client.customobjects.create_or_update_record(schema_id="some-id", data=data)
```

#### Retrieve a record
```
response = client.customobjects.retrieve_a_record(schema_id="some-id", record_id="some-record-id")
```

#### Retrieve a record by external id
```
response = client.customobjects.retrieve_a_record_by_external_id(schema_id="some-id", external_id="some-record-id")
```

#### Delete a record
```
response = client.customobjects.delete_a_record(schema_id="some-id", record_id="some-record-id")
```

#### Delete a record by external id
```
response = client.customobjects.delete_a_record_by_external_id(schema_id="some-id", external_id="some-record-id")
```

#### List all records
```
response = client.customobjects.list_all_records(
        schema_id="some-id", contact_id="some-contact-id", deal_id=None, account_id=None,
        limit=20, offset=0)
```

### Addresses
#### Create an address
```
response = activecampaign_client.addresses.create_an_address(data)
```

#### Retrieve an address
```
response = activecampaign_client.addresses.retrieve_address(address_id="some-id")
```

#### Update an address
```
response = activecampaign_client.addresses.update_address(data, address_id="some-id")
```

#### Delete an address
```
response = activecampaign_client.addresses.delete_address(address_id="some-id")
```

#### Delete an address associated with a user group
```
response = activecampaign_client.addresses.delete_address_associated_with_user_group(group_id="some-id")
```

#### Delete an address associated with a list
```
response = activecampaign_client.addresses.delete_address_associated_with_list(list_id="some-id")
```

#### Retrieve all addresses
```
response = activecampaign_client.addresses.retrieve_all_addresses()
```

### Campaigns
#### List all campaigns
```
response = activecampaign_client.campaigns.list_all_campaigns()
```

#### Retrieve a link associated campaign
```
response = activecampaign_client.campaigns.retrieve_a_link_associated_campaign(campaign_id="some-id")
```

#### Retrieve a campaign
```
response = activecampaign_client.campaigns.retrieve_a_campaign(campaign_id="some-id")
```

### Brandings
#### Retrieve a branding
```
response = activecampaign_client.brandings.retrieve_a_branding(branding_id="some-id")
```

#### Update a branding
```
response = activecampaign_client.brandings.update_a_branding(data, branding_id="some-id")
```

#### List all brandings
```
response = activecampaign_client.brandings.list_all_brandings()
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
