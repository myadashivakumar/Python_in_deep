
class Test:

  def puts(self, *args):
     print " ".join(args)


t = Test()
t.puts("hi")
t .puts("hi","hello")
t .puts("hi","hello","how r u")
t .puts(2,3)