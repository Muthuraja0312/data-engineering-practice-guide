1. Fibonacci series
def fab(n):
  a,b=0,1
  series=[]
  for _ in range(n):
    series.append(a)
    a,b = b,a+b
  return(series)
print(fab(10))
