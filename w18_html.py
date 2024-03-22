def make_link(url, anchor):
    ans = '<a href="' + url + '">' + anchor + '</a>'
    return ans

print(make_link('http://xkcd.com', 'xkcd'))
# -> <a href="http://xkcd.com">xkcd</a>


def html_list(g):
    num = 0
    ans = '<ul> \n'
    while num < len(g):
        ans += '<li>' + str(g[num]) + '</li>' +'\n'
        num += 1
    ans += '</ul>'
    return ans

print (html_list(['cat', 'dog', 47]))

def link_list(links, anchors):
    num = 0
    ans = '<ul> \n'
    while num < len(links):
        ans += '<li>'
        ans += make_link(links[num], anchors[num])
        ans += '</li>'
        ans += '\n'
        num += 1
    ans = ans + '</ul>'
    return ans

us = ['https://www.stuycs.org/fcs00-dw/', 'https://github.com/mks21-dw/solutions', 'https://www.stuycs.org/dwlessons/fcs/selector.html']
ts = ['class site', 'source code', 'slides']
print(link_list(us, ts))

def make_table(data):
    num = 0
    ans = '<table> \n'
    while num < len(data):
        ans += '<tr>'
        newnum = 0
        while newnum < len(data[num]):
            ans += '<td>'
            ans += str(data[num][newnum])
            ans += '</td>'
            newnum +=1
        num+=1
        ans += '</tr> \n'
    ans += '</table>'
    return ans

d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(make_table(d))

