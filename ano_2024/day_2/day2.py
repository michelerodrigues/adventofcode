import os


def load_file(file_path):
    reports = {}

    if not file_path:
        print(f"File: {file_path}")
        print("Error: File path empty or None")
        return reports
    
    try:
        with open(file_path, 'r', encoding='utf-8') as reports_file:
            for index, line in enumerate(reports_file):
                level =  line.strip().split()
                reports.update({index:{"levels": level}})

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error loading file: {e}")

    return reports


def update_data(reports):
    for index, report in reports.items():
        reports[index].update({'safe':False})
        reports[index].update({'order':None})
    
    return reports

def set_report_order(reports_updated):
    for index, reports in reports_updated.items():
        i = 0
        order = None
        new_order = None
        report = reports['levels']
        
        while (i < len(report)-1):
            if int(report[i]) == int(report[i+1]):
                new_order = None
            elif int(report[i]) > int(report[i+1]):
                new_order = 'decrease'
            else:
                new_order = 'increase'
            
            if order != new_order and i > 0:
                order = None
                break
            else:
                order = new_order
            i += 1
                
        reports_updated[index].update({'order': order})
    
    return reports_updated


def check_adjacent_levels(reports_ordered):
    for index, reports in reports_ordered.items():
        i = 0
        safe = None
        report = reports['levels']
        if reports['order'] != None:
            while(i < len(report)-1):
                if (abs(int(report[i]) - int(report[i+1])) <= 0 or abs(int(report[i]) - int(report[i+1])) > 3):
                    safe = False
                    break
                else:
                    safe = True
                i+=1
            reports_ordered[index].update({'safe': safe})
    
    return reports_ordered


def count_safe_reports(reports_checked):
    safe_reports = 0
    for reports in reports_checked.values():
        if reports['safe'] == True:
            safe_reports = safe_reports + 1
    
    return safe_reports



def main():
    file_path = os.path.abspath('day_2/input-day2.txt')
    reports = load_file(file_path)
    reports_updated = update_data(reports)
    reports_ordered = set_report_order(reports_updated)
    reports_checked = check_adjacent_levels(reports_ordered)
    count = count_safe_reports(reports_checked)
    print("How many reports are safe? = ", count)


if __name__ == '__main__':
    main()