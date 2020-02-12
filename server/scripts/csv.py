import csv
from apps.apply.models import ApplyForm


def run():
    f = open('tmp.cvs', 'w')
    wr = csv.writer(f)

    wr.writerow([
        "Name", "Given Name", "Additional Name", "Family Name", "Yomi Name", "Given Name Yomi", "Additional Name Yomi", "Family Name Yomi", "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name", "Maiden Name", "Birthday", "Gender", "Location", "Billing Information", "Directory Server", "Mileage", "Occupation", "Hobby", "Sensitivity", "Priority", "Subject", "Notes", "Language", "Photo", "Group Membership", "Phone 1 - Type", "Phone 1 - Value"
    ])

    items = ApplyForm.objects.all()
    for item in items:
        wr.writerow([
            f'큐시즘-{item.name}', f'큐시즘-{item.name}', "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "* myContacts ::: * kusitms-21기", "Mobile", f'{item.phone}'
        ])
