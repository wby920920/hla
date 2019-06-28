from data_provider import *
from eval import *

entries = all_weekly_data_filter_NEW_NONREDUNT(
        [allele], [9], f_name=test_file)

print(entries)
print(type())

def test_weekly_data_on_allele(allele, test_file=None):
    # get test entryies
    entries = all_weekly_data_filter_NEW_NONREDUNT(
        [allele], [9], f_name=test_file)

    if len(entries) > 0:
        print("="*20)
        print("Test [{}] weekly data entries on allele [{}], length [9]".format(
            len(entries), allele))
        print("="*20)
    else:
        print("="*20)
        print("No weekly data entries on allele [{}], length [9]. Continue".format(
            len(entries), allele))
        print("="*20)
        return

    # get hla encoded vector
    hla_encoded = hla_encode_ONE_HOT(allele)

    # group by iedb id
    ref_ids = list(map(lambda x: x[1], entries))
    ref_ids = set(ref_ids)

    # for each date, generate separate file
    for ref_id in ref_ids:
        # out file
        title, _ = all_weekly_data_NEW_NONREDUNT()
        out_file_name = '{}_{}_weekly.txt'.format(
            allele.replace(':', '-'), ref_id)
        RESULT_FILE_LIST.append(out_file_name)
        out_file = open(os.path.join(TEST_RESULT_DIR, out_file_name), 'w')
        out_str = '{}'.format('\t'.join(title[:7]))
        out_str += '\t{}\t{}\t{}'.format('ConvLogIC50',
                                         'ConvIC50', 'ConvBinding')
        out_str += '\t{}'.format('\t'.join(title[7:]))
        out_file.write(out_str + '\n')

        # filter entries by date
        filtered_entries = list(filter(lambda x: x[1] == ref_id, entries))

        for entry in filtered_entries:
            logic50, bind_prob = predict_on_entry(entry, hla_encoded)
            out_str = '{}'.format('\t'.join(entry[:7]))
            out_str += '\t{}\t{}\t{}'.format(logic50,
                                             math.exp(logic50), bind_prob)
            out_str += '\t{}'.format('\t'.join(entry[7:]))
            out_file.write(out_str + '\n')
        out_file.close()
