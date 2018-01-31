def compare(manual_result_file):
    manual = open(manual_result_file)
    automated = open('./result/log_latest.txt', 'r')


    manual_dic = {}
    #automated_dic = {}
    cmp_file = open('./result/cmp.txt', 'w')
    ratio_file = open('./result/ratio.txt', 'w')
    cmp_file.write('duns\tcontentItemId\tmanual_result\tautomated_result\n')
    count = 0
    manual_created_count = 0
    for manual_record in manual:
        fields = manual_record.strip('\n').split(',')
        if len(fields) != 2:
            continue
        final_dec = fields[1]
        if final_dec == 'y' or final_dec == "Y" or final_dec == "Yes":
            final_dec = "Yes"
            manual_created_count = manual_created_count + 1
        if final_dec == 'n' or final_dec == "N":
            final_dec = "No"
        duns = fields[0]
        manual_dic[duns] = final_dec

    automated_lines = 0
    created_count = 0
    for automated_record in automated:
        fields = automated_record.strip('\n').split('\t')
        if len(fields) != 3:
            continue
        automated_lines = automated_lines + 1
        duns = fields[1]
        final_dec = fields[2]
        if final_dec == "Yes":
            created_count = created_count + 1
        content_item_id = fields[0]
        cmp_file.write(duns + "\t" + content_item_id + "\t" + manual_dic[duns] + "\t" + final_dec + "\n")

    manual_lines = len(manual_dic)

    error_count = manual_lines - automated_lines
    invalid_ratio = error_count / (manual_lines+0.0) * 100
    invalid_ratio_intro = "(" + str(error_count) + "/" + str(manual_lines) + " Useless in matcher automation since we dont use Reader to input the source data)"
    automated_created_ratio = created_count / (automated_lines+0.0) * 100
    automated_created_ratio_intro = "(" + str(created_count)+ "/" + str(automated_lines) + ")"
    manual_created_ratio = manual_created_count/(manual_lines+0.0) * 100
    manual_created_ratio_intro = "("+str(manual_created_count)+"/"+str(manual_lines)+")"

    ratio_file.write("Invalid Record Ratio: "+str("%.2f%%" % invalid_ratio)+ invalid_ratio_intro + "\n")
    ratio_file.write("Manual Create Ratio: " + str("%.2f%%" % manual_created_ratio) + manual_created_ratio_intro +"\n")
    ratio_file.write("BCO Create Ratio: " + str("%.2f%%" % automated_created_ratio)+ automated_created_ratio_intro +"\n")

    cmp_file.close()
