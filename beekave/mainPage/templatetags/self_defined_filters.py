from django import template
import re
register = template.Library()

@register.filter(name='getPercentage')
def getPercentage(score):
    if not score:
        return "0%"
    return str(int(score*10)) +"%"



@register.filter(name='getDT')
def getDT(dt):
    if dt == None:
        return "-"
    return str(dt.year)+"-"+str(dt.month)+"-"+ str(dt.day)

@register.filter(name='scoreSelect')
def scoreSelect(scoreTypeHan,option):
    if scoreTypeHan == option:
        return "selected"

@register.filter(name='getScoreType')
def getScoreType(scoreTypeHan):
    scoreTypeHanList = ["연기", "스토리", "감독", "OST", "영상미", "신선도"]
    scoreTypeEngList = ["scoreact", "scorestory", "scoredirector", "scoreost", "scorevisual", "scorefresh"]
    for sth,ste in zip(scoreTypeHanList,scoreTypeEngList):
        if sth == scoreTypeHan:
            return ste
    return "scoreall"


@register.filter(name='order_is')
def order_is(myUrl,opt):
    curOpt = myUrl.split("/")[2]
    if curOpt == opt:
        return "btn-outline-danger"
    else:
        return "btn-outline-dark"


@register.filter(name='currentUrl')
def currentUrl(myUrl,check):
    if str(myUrl).startswith(check):
        return True
    return False

@register.filter(name='iternum')
def iternum(num):
    return range(num)

@register.filter(name='parentsUrls')
def parentsUrls(myUrl):
    elems = myUrl.split("/")
    return "/".join(elems[:2])+"/"


@register.filter(name='iterInt')
def iterInt(num):
    if num == None:
        return range(0)
    return range(int(num/2)//10)


@register.filter(name='iterFloat')
def iterFloat(num):
    if num == None:
        return range(0)
    halfNum = int(num / 2)
    if halfNum%10 >= 5:
        return range(1)
    else:
        return range(0)

@register.filter(name='getDecScore')
def getDecScore(num):
    return int(float(num))

@register.filter(name='div')
def div( value, arg ):
    '''
        Divides the value; argument is the divisor.
        Returns empty string on any error.
        '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value // arg
    except: pass
    return ''

@register.filter(name='getFullStar')
def getFullStar(num):
    num = int(num*10)
    tens = num//10;
    units = num - tens*10
    if units > 7:
        return tens+1
    else:
        return tens

@register.filter(name='getHalfStar')
def getHalfStar(num):
    num = int(num*10)
    tens = num//10;
    units = num - tens*10
    if units >= 4 and units <= 7:
        return 1
    else:
        return 0

@register.filter(name='addstr')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter(name='incrPage')
def incrPage(url):
    elems = url.split("/")
    newElem = []
    for ele in elems:
        if re.match("[p]+[1-9]+",ele):
            newElem.append("p"+str(int(ele[1:])+1))
        else:
            newElem.append(ele)
    return "/".join(newElem)

@register.filter(name='decrPage')
def decrPage(url):
    elems = url.split("/")
    newElem = []
    for ele in elems:
        if re.match("[p]+[1-9]+",ele):
            newp = int(ele[1:])-1
            if newp >= 1:
                newElem.append("p"+str(newp))
            else:
                newElem.append("p1")
        else:
            newElem.append(ele)
    return "/".join(newElem)

@register.filter(name='andorquestion')
def andorquestion(url):
    if str(url).endswith("/"):
        return url+"?"
    else:
        startend = [(m.start(0), m.end(0)) for m in re.finditer(r"&page=\d+", url)]
        if len(startend):
            startend = startend[0]
            url = url[:startend[0]]
        return url + "&"


