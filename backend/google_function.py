def GCD(request):
    request_json = request.get_json()
    if request_json and 'message' in request_json:
        a = request_json['message']['n1']
        b = request_json['message']['n2']
        x = int(a)
        y = int(b)
        if (x<0 or y<0):
            return "invalid argument"
        if (x>y):
            x,y = y,x
        m=x; x=y
        while(m>0):
            y=x ; x=m ; m=y % x

        return str(x)
    else:
        return "invalid argument"
