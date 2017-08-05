# test_task
Another test task to demonstrate Django skills

# Requirements
Build and deploy a web application representing Dogs and Cats.

- Each dog and cat must have a name and birthday, and be linked to an Owner
- Owners should be able to access dogs and cats via an API and carry out CRUD operations on their Dog and Cat
- Owners should also be able to access dogs and cats via an admin interface

# Implementation
- User model is a great candidate for the "Owner" role - let's use it
- For this task, I decided not to create any Form and View for managing pets in userspace, but rather create a second, restricted admin ("owners' admin") which will do all the job for me. I just need to make some modifications:
    - Allow logging-in not-staff users (owners)
    - Restrict Pets to only owner's ones (owner cannot edit someone else's pets)
- For CRUD, use django rest framework
