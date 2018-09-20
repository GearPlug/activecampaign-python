# activecampaign-python
ActiveCampaign API wrapper written in python.

## Installing

```
pip install activecampaign-python
```

## Requirements

```
- Requests
```

## Usage

```
from activecampaign.client import Client
client = Client(URL, APIKEY)

View a contact:

Client.contacts.view_contact(ID)

Get Deals:

Client.deals.get_deals()
```
## TODO

### Address
### Automation
### Branding
### Campaign
### Contact

- Contact_automation_list
- Contact_delete_list
- Contact_list
- Contact_note_add
- Contact_note_delete
- Contact_note_edit
- Contact_paginator
- Contact_sync
- Contact_tag_add
- Contact_tag_remove
- Contact_view_hash

### Deal

- Deal_edit
- Deal_note_add
- Deal_note_edit
- Deal_pipeline_add
- Deal_pipeline_edit
- Deal_pipeline_list
- Deal_stage_add
- Deal_stage_edit
- Deal_task_edit
- Deal_tasktype_add
- Deal_tasktype_delete
- Deal_tasktype_edit

### Form

### Group

### List

- List_edit
- List_field_add
- List_field_delete
- List_field_edit
- List_field_view
- List_paginator

### Message

### Organization

### Segment

### Settings

### Single Sin On

### Tags

### Site & Event Tracking

### User

- User_add
- User_delete
- User_delete_list
- User_edit
- User_list
- User_me
- User_view_email
- User_view_username

### Webhook

- Webhook_edit
- Webhook_events
- Webhook_list
