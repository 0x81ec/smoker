
from requests_html import HTMLSession

def getips():
    session = HTMLSession()
    r = session.get("http://www.89ip.cn/")
    trs = r.html.xpath("//tr")
    ips = []
    for t in trs:
        # print(t)
        d1 = t.xpath(".//td[1]/text()")
        d2 = t.xpath(".//td[2]/text()")
        ipt = "".join(d1).strip()+":"+"".join(d2).strip()
        ips.append(ipt)
    return ips
if __name__=="__main__":
    
    ips = getips()

    for ip in ips:
        print(ip)
