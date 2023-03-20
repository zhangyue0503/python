# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cs = "GUID=af645c2c-8313-4e56-85e7-18d3026db787; Hm_lvt_9793f42b498361373512340937deb2a0=1674977725; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F08%252F28%252F22%252F99942228.jpg-88x88%253Fv%253D1674977850000%26id%3D99942228%26nickname%3Dzyblog%26e%3D1690529998%26s%3D090843ecf4d5290a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299942228%22%2C%22%24device_id%22%3A%22185fc73c669b85-03573f78622cea-16525635-2073600-185fc73c66a207%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22af645c2c-8313-4e56-85e7-18d3026db787%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1675386019"

    cookies = {data.split('=')[0]: data.split('=')[-1] for data in cs.split('; ')}
    print(cookies)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
