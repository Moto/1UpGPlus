import base64

of = file('sounds.js', 'w')

def encode(fn):
    fp = file(fn, "rb")
    bin = fp.read()
    b64 = base64.encodestring(bin).split()
    return b64

def wrapdata(data):
	data = str.join("' + \n'", data)
	data = "'" + data
	return data

tmpl = '''
'<audio ' +
  'id="%(ID)s" ' +
  'type="audio/mpeg" ' +
  'src="data:audio/mpeg;base64,' +
%(DATA)s">' +
'</audio>'
'''

of.write("g_oneup_sounds = \n")

data = wrapdata(encode("1up-anlg.mp3"))

of.write(tmpl % { 'ID': 'oneup_sound_anlg', 'DATA': data})

data = wrapdata(encode("1up-dig.mp3"))
of.write(" + \n")

of.write(tmpl % { 'ID': 'oneup_sound_dig', 'DATA': data})
of.write(" ; \n")

of.write("g_icon_15rgy = \n")

tmpl_img = '''
'.%(CLASS_ID)s { ' +
  'background: ' + 
  'url(data:image/png;base64,' +
%(DATA)s) ' + 
'!important; }'
'''

data = wrapdata(encode("icon-15g.png"))
of.write(tmpl_img % {'CLASS_ID': 'eswd', 'DATA': data})
of.write(" + \n")

of.write(tmpl_img % {'CLASS_ID': 'eswd:hover', 'DATA': data})
of.write(" + \n")

data = wrapdata(encode("icon-15g-inv.png"))
of.write(tmpl_img % {'CLASS_ID': 'eswa', 'DATA': data})
of.write(" ; \n")

of.close()
