import oct2py

octave = oct2py.Oct2Py()

domain = "[0:0.1:10]"
function = "sin(x)"

# define symbolic function f in octave
octave.eval_("f = @(x)" + function)
# evaluate function f in octave and receive output
result = octave.eval_("feval(f," + domain + ")")

print result
