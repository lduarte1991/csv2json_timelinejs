import json
import csv
from pprint import pprint
import sys
from datetime import datetime
try:
    from sets import Set
except:
    pass

def main():
    with open(sys.argv[1]) as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=',', quotechar='"')
        index = 0
        json_data = []
        # each row is an object
        headers = []
        final_object = {
            "events": []
        }
        try:
            for index, column in enumerate(csv_reader.next()):
                headers.append((index, column))
        except:
            for index, column in enumerate(next(csv_reader)):
                headers.append((index, column))
        for row in csv_reader:
            new_object = {
                'start_date': {
                },
                'end_date': {
                },
                'text': {
                    'headline': '',
                    'text': ''
                },
                'media': {
                    'url': '',
                    'caption': '',
                    'credit': '',
                    'thumbnail': ''
                },
                'type': '',
                'group': '',
                'display_date': '',
                'background': '',
                'autolink': True,
            }
            for index, header in headers:
                new_header = header.lower().strip()
                date_type = 'start_date'
                if 'end' in new_header:
                    date_type = 'end_date'
                if new_header == 'year' or new_header == 'end year':
                    if row[index].strip() != '':
                        new_object[date_type]['year'] = int(row[index])
                elif new_header == 'month' or new_header == 'end month':
                    if row[index].strip() != '':
                        new_object[date_type]['month'] = int(row[index])
                elif new_header == 'day' or new_header == 'end day':
                    if row[index].strip() != '':
                        new_object[date_type]['day'] = int(row[index])
                elif new_header == 'time' or new_header == 'end time':
                    if row[index].strip() != '':
                        split_time = row[index].split(':')
                        if len(split_time) == 1:
                            if 'am' in split_time[0].lower():
                                hour = int(split_time[0])
                                if hour != 12:
                                    new_object[date_type]['hour'] = hour
                            elif 'pm' in split_time[0].lower():
                                hour = int(split_time[0])
                                if hour != 12:
                                    hour = hour + 12
                                new_object[date_type]['hour'] = hour
                        elif len(split_time) == 2:
                            hour = int(split_time[0])
                            minute = int(split_time[1])
                            if 'am' in split_time[1].lower():
                                if hour != 12:
                                    new_object[date_type]['hour'] = hour
                            elif 'pm' in split_time[1].lower():
                                if hour != 12:
                                    hour = hour + 12
                                new_object[date_type]['hour'] = hour
                            new_object[date_type]['minute'] = minute
                        elif len(split_time) == 3:
                            hour = int(split_time[0])
                            minute = int(split_time[1])
                            second = int(split_time[2])
                            if 'am' in split_time[2].lower():
                                if hour != 12:
                                    new_object[date_type]['hour'] = hour
                            elif 'pm' in split_time[2].lower():
                                if hour != 12:
                                    hour = hour + 12
                                new_object[date_type]['hour'] = hour
                            new_object[date_type]['minute'] = minute
                            if '.' in split_time[2]:
                                split_time_again = split_time[2].split('.')
                                millisecond = split_time_again[1]
                                new_object[date_type]['millisecond'] = millisecond
                            new_object[date_type]['second'] = second
                        elif len(split_time) == 4:
                            hour = int(split_time[0])
                            minute = int(split_time[1])
                            second = int(split_time[2])
                            millisecond = int(split_time[3])
                            if 'am' in split_time[3].lower():
                                if hour != 12:
                                    new_object[date_type]['hour'] = hour
                            elif 'pm' in split_time[3].lower():
                                if hour != 12:
                                    hour = hour + 12
                                new_object[date_type]['hour'] = hour
                            new_object[date_type]['minute'] = minute
                            new_object[date_type]['second'] = second
                            new_object[date_type]['millisecond'] = millisecond
                elif new_header == 'display date':
                    if row[index].strip() != '':
                        new_object['display_date'] = row[index].strip()
                elif new_header == 'headline':
                    if row[index].strip() != '':
                        new_object['text']['headline'] = row[index].strip()
                elif new_header == 'text':
                    if row[index].strip() != '':
                        new_object['text']['text'] = row[index].strip()
                elif new_header == 'media':
                    if row[index].strip() != '':
                        new_object['media']['url'] = row[index].strip()
                elif new_header == 'media credit':
                    if row[index].strip() != '':
                        new_object['media']['credit'] = row[index].strip()
                elif new_header == 'media caption':
                    if row[index].strip() != '':
                        new_object['media']['caption'] = row[index].strip()
                elif new_header == 'media thumbnail':
                    if row[index].strip() != '':
                        new_object['media']['thumbnail'] = row[index].strip()
                elif new_header == 'type':
                    if row[index].strip() != '':
                        new_object['type'] = row[index].strip()
                elif new_header == 'group':
                    if row[index].strip() != '':
                        new_object['group'] = row[index].strip()
                elif new_header == 'background':
                    if row[index].strip() != '':
                        new_object['background'] = row[index].strip()
            if new_object['end_date'] == {}:
                del new_object['end_date']
            final_object['events'].append(new_object)
        with open(sys.argv[1].replace('.csv', '.json'), 'w') as outfile:
            json.dump(final_object, outfile)

if __name__ == '__main__':
    main()
