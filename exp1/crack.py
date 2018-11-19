from string import ascii_lowercase
#from Crypto import AES
from binascii import b2a_hex, a2b_hex
def insert_letter(text, i, l):
    return text[:i] + l + text[i:]

def get_blank_record(text):
    text = text.lower()
    blank_record = []
    for i in range(len(text)):
        l = text[i]
        item = []
        if lowercase.find(l) < 0:
            item.append(i)
            item.append(l)
            blank_record.append(item)
    return blank_record

def restore_blank_record(text, blank_record):
    for i in blank_record:
        text = insert_letter(text, i[0], i[1])
    return text

def get_vigener_key_table(text, key):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += l

    total_length = len(trim_text)
    key_length = len(key)
    quotient = total_length // key_length
    reminder = total_length % key_length
    key_table = quotient * key + key[:reminder]

    return trim_text, key_table

def vigener_cypher_encrypt(text, key, is_encrypt=True):
    blank_record = get_blank_record(text)
    trim_text, key_table = get_vigener_key_table(text, key)

    result = ''
    for i in range(len(trim_text)):
        l = trim_text[i]
        index_lowercase = lowercase.find(l)
        index_key_table = lowercase.find(key_table[i])
        if not is_encrypt:
            index_key_table = -index_key_table
        result += lowercase[(index_lowercase + index_key_table) % 26]

    return restore_blank_record(result, blank_record)

def vigener_cypher_decrypt(text, key):
    return vigener_cypher_encrypt(text, key, False)




def get_coincidence_index(text):
    trim_text = get_trim_text(text)
    length = len(trim_text)
    letter_stats = []
    for l in lowercase:
        lt = {}
        count = trim_text.count(l)
        lt[l] = count
        letter_stats.append(lt)

    index = 0
    for d in letter_stats:
        v = list(d.values())[0]
        index += (v/length) ** 2

    return index

def get_var(data, mean=0.067):
    if not data:
        return 0
    var_sum = 0
    for d in data:
        var_sum += (d - mean) ** 2

    return var_sum / len(data)

def get_trim_text(text):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += l
    return trim_text

def get_key_length(text):
    trim_text = get_trim_text(text)
    # assume text length less than 26
    group = []
    for n in range(1, 26):
        group_str = ['' for i in range(n)]
        for i in range(len(trim_text)):
            l = trim_text[i]
            for j in range(n):
                if i % n == j:
                    group_str[j] += l
        group.append(group_str)

    var_list = []
    length = 1
    for text in group:
        data = []
        for t in text:
            index = get_coincidence_index(t)
            data.append(index)
        var_list.append([length, get_var(data)])
        length += 1
    var_list = sorted(var_list, key=lambda x: x[1])
    return [v[0] for v in var_list[:12]]



def crack_vigener_cypher(text, key_length):
    blank_record = get_blank_record(text)
    trim_text = get_trim_text(text)
    group = ['' for i in range(key_length)]
    for i in range(len(trim_text)):
        l = trim_text[i]
        for j in range(key_length):
            if i % key_length == j:
                group[j] += l

    key = ''
    letter_stats_group = []
    for j in range(key_length):
        letter_stats = []
        for l in lowercase:
            lt = {}
            count = group[j].count(l)
            lt[l] = count
            letter_stats.append(lt)

        letter_stats = sorted(letter_stats, key=lambda x: list(x.values())[0], reverse=True)
        letter_stats_group.append(letter_stats)
        # print('group', j, ':', letter_stats[:8])

        # gvctxs
        score_list = []
        for i in range(3):
            current_letter = list(letter_stats[i].keys())[0]
            index = lowercase.find(current_letter)
            key_letter = lowercase[index - lowercase.find('e')]
            item = []
            item.append(key_letter)
            score = 0
            for k in range(3):
                vl = list(letter_stats[k].keys())[0]
                for fl in ['t', 'a']:
                    #if i == 1 and (k == 1 or k == 2) and j == 1:
                    if (lowercase.find(key_letter) + lowercase.find(fl)) % 26 == lowercase.find(vl):
                        score += 1
            item.append(score)
            score_list.append(item)
        score_list = sorted(score_list, key=lambda x: x[1], reverse=True)
        key += score_list[0][0]

    plain_text = vigener_cypher_decrypt(trim_text, key)
    return restore_blank_record(plain_text, blank_record)

text = 'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'
crack_vigener_cypher(text,7)