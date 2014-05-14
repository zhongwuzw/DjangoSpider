from JobSpider.forms import UpLoadFileForm
import pickle
class Foo:
    attr = 'a class attr'
    
t = UpLoadFileForm()
print t.as_p()
pickle_string = pickle.dumps(Foo)
print pickle_string