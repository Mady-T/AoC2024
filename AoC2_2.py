import pandas as pd

inp = pd.read_csv('inputs/day2inp1', sep='\s+', header=None, names = range(8))

safe_count = 0
for report_num in range(len(inp)):
    report_ = list(inp.iloc[report_num,:])
    reportlist = []
    for i in range(len(report_)):
        rep = report_.copy()
        rep.pop(i)
        reportlist.append(rep)
    anysafe = False
    for report in reportlist:
        n = 0
        asc = False
        desc = False
        safe = True
        while n < len(report) and report[n]:
            if n == 0:
                n+=1
                continue
            if abs(report[n] - report[n-1]) > 3:
                    safe = False
                    break
            if not asc and not desc:
                if report[n] > report[n-1]:
                    asc = True
                elif report[n] < report[n-1]:
                    desc= True
                else:
                    safe=False
                    break
            else:
                if asc:
                    if report[n] <= report[n-1]:
                        safe = False
                        break
                if desc:
                    if report[n] >= report[n-1]:
                        safe = False
                        break
            n+=1
        # print(report, safe)
        if safe:
            anysafe = True
            break
    # print(report, anysafe)
    if anysafe:
        safe_count+= 1

print(safe_count)