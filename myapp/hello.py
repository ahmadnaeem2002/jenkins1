import fire

def hello(name="World"):
  return "Hello From Naeem%s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
