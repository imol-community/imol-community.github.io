import pandas as pd

path_to_tsv_file = '~/Downloads/tsv_file.tsv'
cutoff_date = '27/10/2024'  #day/month/year
# last update on march 29 2024

def tsv_to_member_list(path_to_tsv_file, cutoff_date):
    """
    Function to review new applications since a cutoff_date using the output of the form google sheet
    from https://docs.google.com/spreadsheets/d/14ZuCujk7Qql0vsAglO-ErgpBAsxo_VNm2uel6jTz2q4/edit?resourcekey#gid=25377730
    The cutoff date must be in the format: day/month/year.
    The function gives you the name, affiliation and papers/scholar links for you to decide whether to accept or reject.
    It saves accepted or rejected decisions made so far in the tsv_file.
    At the end, it returns the list of new members to be copied / pasted on the community.md page of the website.
    If no cutoff date is provided it reviews all answers to the form since the beginning.
    """
    # load tsv
    df = pd.read_csv(path_to_tsv_file, delimiter='\t')

    # define key names in case they change later
    date_key = 'Horodateur'
    name_added = "I want my name to be added to the list of members at https://www.imol-community.org/community/"
    papers = "Link to 1-3 of your papers relevant to IMOL (e.g. ArXiv)"
    scholar = "Link to google scholar page or equivalent (if any)"
    accept_reject = 'accept/reject'
    first_name = 'First name'
    middle_name = 'Middle name (optional)'
    last_name = 'Last name'
    position = 'Position'
    affiliation = 'Affiliation'
    research_description = 'Short description of your research in areas of interest to the IMOL community'
    accept = 'Accept'
    reject = "Reject"

    # format dates of each entry
    try:
        date_format = '%d/%m/%Y %H:%M:%S'
        dates = pd.to_datetime(df[date_key], format=date_format)
    except:
        date_format = '%Y-%m-%d %H:%M:%S'
        dates = pd.to_datetime(df[date_key], format=date_format)

    if accept_reject not in df:
        df[accept_reject] = [None] * len(df[date_key])

    # if a cutoff_date is provided, filter the indexes based on that
    if cutoff_date is not None:
        try:
            cutoff_date = pd.to_datetime(cutoff_date, format='%d/%m/%Y')
        except:
            print("ERROR: the cutoff data as the wrong format, should be '%d/%m/%Y'")
            assert False

        filtered_df = df[dates >= cutoff_date]
    else:
        filtered_df = df

    markdown_code = []
    accept_reject_data = []
    counter = 0
    total = len(filtered_df)
    first_index = None
    for index, entry in filtered_df.iterrows():
        counter += 1
        if first_index is None:
            first_index = index
        date = str(pd.to_datetime(entry[date_key], format=date_format).strftime('%m/%Y'))

        # test if application is valid (str for first, last name, position and affiliation)
        is_valid = True
        is_valid = is_valid and isinstance(entry[first_name], str)
        is_valid = is_valid and isinstance(entry[last_name], str)
        is_valid = is_valid and isinstance(entry[position], str)
        is_valid = is_valid and isinstance(entry[affiliation], str)

        if not is_valid:
            # should not happen, I think the form enforces a string
            format_str = f"{entry[first_name]} {entry[middle_name]} {entry[last_name]}, {entry[position]} ({entry[affiliation]}), added on {date}."
            print(f'Application invalid (please update tsv file manually) and restart:'
                  f'\n{format_str}')
            assert False
        else:
            if isinstance(entry[middle_name], str):
                format_str = f"<b>{entry[first_name]} {entry[middle_name]} {entry[last_name]}</b>, {entry[position]} ({entry[affiliation]}), added on {date}."
            else:
                format_str = f"<b>{entry[first_name]} {entry[last_name]}</b>, {entry[position]} ({entry[affiliation]}), added on {date}."

        if entry[accept_reject] == accept:
            accept_reject_data.append(accept)
            print(f'Already accepted: {format_str}')
            if entry[name_added] == 'Yes':
                markdown_code.append(format_str)
        elif entry[accept_reject] == reject:
            accept_reject_data.append(reject)
            print(f'Already rejected: {format_str}')
        else:
            # review the application
            print(f'Application review: {counter} / {total}')
            print(format_str)
            print(f'Research description: {entry[research_description]}\n')
            print(f'Papers: {entry[papers]}\n')
            print(f'Scholar: {entry[scholar]}')
            decision = None
            while decision not in ['a', 'r']:
                decision = input('Press "a" to accept, "r" to reject.')

            if decision == 'a':
                df.at[index, accept_reject] = accept
                df.to_csv(path_to_tsv_file, sep='\t', index=False)  # save in case of bug during the review process
                print('ACCEPTED')
                if entry[name_added] == 'Yes':
                    # only add names of people who agreed to
                    markdown_code.append(format_str)
                accept_reject_data.append(accept)
            elif decision == 'r':
                print('REJECTED')
                accept_reject_data.append(reject)
            else: raise ValueError
    assert len(accept_reject_data) == total
    format_everything = ""
    for code in markdown_code:
        format_everything += f'<li> {code} </li> \n'
    decisions = '\n'.join(accept_reject_data)
    instructions = ("Instructions:\n"
                    "Two things need to be done:\n\n"
                    "1) update the list of accepted members on the website by copy/paste:\n\n"
                    f"{format_everything}\n\n"
                    f"2) update the form sheet with decisions (starting with index {first_index + 2}, last column):\n"
                    f"https://docs.google.com/spreadsheets/d/14ZuCujk7Qql0vsAglO-ErgpBAsxo_VNm2uel6jTz2q4/edit?resourcekey#gid=25377730\n\n"
                    f"{decisions}")
    print(instructions)
    return instructions

if __name__ == '__main__':
    tsv_to_member_list(path_to_tsv_file=path_to_tsv_file, cutoff_date=cutoff_date)
