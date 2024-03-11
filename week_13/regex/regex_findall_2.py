import re


def main():
    """
    Drive the program. Demonstrate how to find all.
    """
    phone_number_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    fake_input = 'Office: 604-555-1234 Cell: 604-555-5678'

    match_object = phone_number_regex.search(fake_input)
    if match_object:
        print("I found this number:", match_object.group())
    else:
        print("No numbers found.")

    match_object_list = phone_number_regex.findall(fake_input)
    if match_object_list:
        print('\nI found this many phone numbers:', len(match_object_list))
        print(match_object_list)

    phone_number_grouped_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    match_object_list = phone_number_grouped_regex.findall(fake_input)
    if match_object_list:
        print('\nI found this many phone numbers:', len(match_object_list))
        print(match_object_list)


if __name__ == "__main__":
    main()
